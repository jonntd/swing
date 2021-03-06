from __future__ import print_function
import traceback
import gazu
import sys
import os
import requests
import shutil

from zipfile import ZipFile

from requests_toolbelt.streaming_iterator import StreamingIterator
from requests_toolbelt import (
    MultipartEncoder,
    MultipartEncoderMonitor
)

import hashlib

# ==== auto Qt load ====
try:
    from PySide2 import QtCore
    from PySide2.QtCore import Signal as pyqtSignal
    qtMode = 0
except ImportError:
    from PyQt5 import QtCore
    from QtCore import pyqtSignal

from datetime import datetime

def write_log(*args):
    log = "{} swing: ".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"))
    for log_data in args:
        log += " {}".format(log_data)
    print(log)

class LoadedSignal(QtCore.QObject):
    loaded = QtCore.Signal(object)        

class ProjectLoaderThread(QtCore.QRunnable):

    def __init__(self, parent):
        super(ProjectLoaderThread, self).__init__(self, parent)
        self.callback = LoadedSignal()

    def run(self):
        results = {}
        try:
            try:
                projects = gazu.project.all_open_projects()
                task_types = gazu.task.all_task_types()

                results["projects"] = projects
                results["task_types"] = task_types

            except:
                traceback.print_exc(file=sys.stdout)
            # done
        finally:
            self.callback.loaded.emit(results)

class ProjectHierarchyLoaderThread(QtCore.QRunnable):

    def __init__(self, parent, project):
        super(ProjectHierarchyLoaderThread, self).__init__(self, parent)
        self.project = project
        self.callback = LoadedSignal()        

    def run(self):
        try:
            try:
                episodes = gazu.shot.all_episodes_for_project(self.project)
                if len(episodes) == 0:
                    episode = {
                        "name": "All",
                        "id": 0,
                        "sequences": gazu.shot.all_sequences_for_project(self.project)
                    }
                    episodes = [ episode ]
                else:
                    for ep in episodes:
                        ep["sequences"] = gazu.shot.all_sequences_for_episode(ep)

                for ep in episodes:
                    for seq in ep["sequences"]:
                        seq["shots"] = gazu.shot.all_shots_for_sequence(seq)

                results = {
                    "results": episodes
                }                        
            except:
                traceback.print_exc(file=sys.stdout)
            # done
        finally:
            self.callback.loaded.emit(episodes)

class EntityFileLoader(QtCore.QRunnable):

    def __init__(self, parent, entity, working_dir):
        super(EntityFileLoader, self).__init__(self, parent)
        self.entity = entity
        self.working_dir = working_dir
        self.callback = LoadedSignal()        

    def run(self):
        try:
            results = {
                "output_files": [],
                "working_files": []
            }                        

            try:
                if self.entity["type"] == "Shot":
                    casting = gazu.casting.get_shot_casting(self.entity)
                else:
                    casting = gazu.casting.get_asset_casting(self.entity)
                    
                #for item in casting:
                #    file_list += reportdata.load_working_files(item["asset_id"])            
                
                output_files = gazu.files.all_output_files_for_entity(self.entity)
                working_files = gazu.files.get_all_working_files_for_entity(self.entity)

                # load casted files
                for item in casting:

                    for file_item in gazu.files.all_output_files_for_entity(item["asset_id"]):
                        if file_item not in output_files:
                            output_files.append(file_item)

                    for file_item in gazu.files.get_all_working_files_for_entity(item["asset_id"]):
                        if file_item not in working_files:
                            working_files.append(file_item)

                results = {
                    "output_files": output_files,
                    "working_files": working_files
                }                        
            except:
                traceback.print_exc(file=sys.stdout)
            # done
        finally:
            self.callback.loaded.emit(results)                        
              
class AssetTypeLoaderThread(QtCore.QRunnable):

    def __init__(self, parent, project):
        super(AssetTypeLoaderThread, self).__init__(self, parent)
        self.project = project
        self.callback = LoadedSignal()        

    def run(self):
        results = gazu.asset.all_asset_types_for_project(self.project)

        self.callback.loaded.emit(results)        

class AssetLoaderThread(QtCore.QRunnable):

    def __init__(self, parent, project, asset_type):
        super(AssetLoaderThread, self).__init__(self, parent)
        self.project = project
        self.asset_type = asset_type
        self.callback = LoadedSignal()        

    def run(self):
        results = gazu.asset.all_assets_for_project_and_type(self.project, self.asset_type)

        self.callback.loaded.emit(results)          

class EntityLoaderThread(QtCore.QRunnable):

    def __init__(self, parent, entity_id):
        super(EntityLoaderThread, self).__init__(self, parent)
        self.entity_id = entity_id
        self.callback = LoadedSignal()        

    def run(self):
        results = {}

        entity = gazu.entity.get_entity(self.entity_id)
        results["entity"] = entity
        results["type"] = entity["type"]

        if entity["type"] == "Shot":
            results["item"] = gazu.shot.get_shot(self.entity_id)
            results["project"] = gazu.project.get_project(results["item"]["project_id"])
            results["url"] = gazu.shot.get_shot_url(results["item"])
            results["casting"] = gazu.casting.get_shot_casting(results["item"])
        else:
            results["item"] = gazu.asset.get_asset(self.entity_id)
            results["project"] = gazu.project.get_project(results["item"]["project_id"])
            results["url"] = gazu.asset.get_asset_url(results["item"])
            results["casting"] = gazu.casting.get_asset_casting(results["item"])

        self.callback.loaded.emit(results)      

class TaskFileInfoThread(QtCore.QRunnable):

    def __init__(self, parent, task, project_root):
        super(TaskFileInfoThread, self).__init__(self, parent)
        self.parent = parent
        self.task = task
        self.project_root = project_root
        self.callback = LoadedSignal()        
    
    def run(self):
        task = gazu.task.get_task(self.task)
        project = gazu.project.get_project(self.task["project_id"])
        working_dir = gazu.files.build_working_file_path(task)

        if project["file_tree"]:
            file_tree = project["file_tree"]
            if "working" in file_tree and file_tree["working"]["mountpoint"]:
                mount_point = file_tree["working"]["mountpoint"]
                working_dir = os.path.normpath(working_dir.replace(mount_point, self.project_root))


        results = {
            "task": task,
            "working_dir": working_dir,
            "project": project
        }

        self.callback.loaded.emit(results)        

class TaskLoaderThread(QtCore.QRunnable):

    def __init__(self, parent, project, email):
        super(TaskLoaderThread, self).__init__(self, parent)
        self.parent = parent
        self.project = project
        self.email = email
        self.callback = LoadedSignal()        

    #def due_date(self, elem):
    #    if "due_date" in elem and elem["due_date"]:
    #        return arrow.get(elem["due_date"], "YYYY-MM-DDTHH:mm:ss")
    #    return 0

    def run(self):
        person = gazu.person.get_person_by_email(self.email)
        tasks = gazu.task.all_tasks_for_person(person)
        results = []
        for item in tasks:
            if item["project_id"] == self.project["id"]:
                results.append(item)
        self.callback.loaded.emit(results)

class SoftwareLoader(QtCore.QRunnable):

    def __init__(self, parent):
        super(SoftwareLoader, self).__init__(self, parent)
        self.parent = parent
        self.callback = LoadedSignal()        

    def run(self):
        software = gazu.files.all_softwares()

        results = {
            "software": software
        }
        self.callback.loaded.emit(results)        

class DownloadSignal(QtCore.QObject):

    # setting up custom signal
    done = QtCore.Signal(object)        
    progress = QtCore.Signal(object)

class FileDownloader(QtCore.QRunnable):

    def __init__(self, parent, working_dir, file_id, url, target, email, password, skip_existing = True, extract_zips = False):
        super(FileDownloader, self).__init__(self, parent)
        self.parent = parent
        self.working_dir = working_dir
        self.file_id = file_id
        self.url = url
        self.target = target
        self.email = email
        self.password = password
        self.skip_existing = skip_existing
        self.extract_zips = extract_zips
        self.callback = DownloadSignal()

    def progress(self, count):
        results = {
            "status": "ok",
            "message": "downloading",
            "file_id": self.file_id,
            "target": self.target,
            "working_dir": self.working_dir,
            "size": count
        }
        self.callback.progress.emit(results)

    def run(self):
        filename, file_extension = os.path.splitext(self.target)
        ###
        if self.skip_existing:
            # check if the target 
            if os.path.exists(self.target):
                write_log("Target exists {}".format(self.target))

                size = os.path.getsize(self.target)                
                status = {
                    "status": "skipped",
                    "message": "Skipped existing file",
                    "file_id": self.file_id,
                    "target": self.target,
                    "working_dir": self.working_dir,
                    "size": size
                }
                self.callback.done.emit(status)
                return

            if os.path.exists(os.path.join(self.working_dir, filename)):
                write_log("Target exists {}".format(os.path.join(self.working_dir, filename)))

                size = os.path.getsize(self.target)                
                status = {
                    "status": "skipped",
                    "message": "Skipped existing file",
                    "file_id": self.file_id,
                    "target": self.target,
                    "working_dir": self.working_dir,
                    "size": size
                }
                self.callback.done.emit(status)
                return                

        params = { 
            "username": self.email,
            "password": self.password
        } 

        target_dir = os.path.dirname(self.target)
        if not os.path.exists(target_dir):
            try:
                os.makedirs(target_dir)   
                print("Made dir: {}".format(target_dir))     
            except:
                pass

        count = 0
        rq = requests.post(self.url, data = params, stream = True)
        if rq.status_code == 200:
            with open(self.target, 'wb') as out:
                for bits in rq.iter_content(1024 * 1024):
                    out.write(bits)        
                    count += len(bits)
                    self.progress(count)
        else:
            status = {
                "status": "error",
                "message": "Error downloading file",
                "file_id": self.file_id,
                "target": target_dir,
                "working_dir": self.working_dir,
                "size": 0
            }   
            self.callback.done.emit(status)            
            return False        
                    
        try:
            os.sync()
        except:
            pass

        size = os.path.getsize(self.target)
        ###
        if self.extract_zips and file_extension in [ ".zip" ]:
            zip_root = os.path.normpath(os.path.join(self.working_dir, filename))

            status = {
                "status": "ok",
                "message": "Extracting zip",
                "file_id": self.file_id,
                "target": zip_root,
                "working_dir": self.working_dir,
                "size": size
            }   
            self.callback.progress.emit(status)
            # def makedirs(name, mode=0o777, exist_ok=False):
            try:
                os.makedirs(zip_root)
            except:
                pass

            if self.extract_zip(self.target, zip_root):
                status = {
                    "status": "ok",
                    "message": "Extracted zip",
                    "file_id": self.file_id,
                    "target": zip_root,
                    "working_dir": self.working_dir,
                    "size": size
                }   
                self.callback.progress.emit(status)  
            else:
                status = {
                    "status": "error",
                    "message": "Error extracting zip",
                    "file_id": self.file_id,
                    "target": zip_root,
                    "working_dir": self.working_dir,
                    "size": size
                }   
                self.callback.progress.emit(status)                               

        status = {
            "status": "ok",
            "message": "Download complete",
            "file_id": self.file_id,
            "target": self.target,
            "working_dir": self.working_dir,
            "size": size            
        }

        self.callback.done.emit(status)        

    def extract_zip(self, archive, directory):
        try:
            os.chdir(directory)
            with ZipFile(archive, 'r') as zipObj:
                # Extract all the contents of zip file in current directory
                zipObj.extractall()
                #shutil.unpack_archive(archive)        
            return True
        except:
            traceback.print_exc(file=sys.stdout)
            return False
            # extract all items in 64bit
        # open zip file in read binary


##############################################################################################################################################################################################
##############################################################################################################################################################################################
##############################################################################################################################################################################################

class UploadSignal(QtCore.QObject):

    # setting up custom signal
    done = QtCore.Signal(object)        
    progress = QtCore.Signal(object)



##############################################################################################################################################################################################
# https://github.com/vsoch/django-nginx-upload/blob/master/push.py
#
_READ_SIZE = 1024 * 1024.0

def create_callback(encoder, upload_signal, source):
    encoder_len = int(encoder.len / _READ_SIZE)
    
    upload_signal.progress.emit({
        "status": "ok",
        "message": "[0 of %s MB]" % (encoder_len),
        "source": source
    })

    def callback(monitor):
        bytes_read = int(monitor.bytes_read / _READ_SIZE)
        upload_signal.progress.emit({
            "status": "ok",
            "message": "[%s of %s MB]" % (bytes_read, encoder_len),
            "source": source
        })
    return callback

class WorkingFileUploader(QtCore.QRunnable):

    def __init__(self, parent, edit_api, task, source, file_name, software_name, comment, email, password, mode = "working"):
        super(WorkingFileUploader, self).__init__(self, parent)
        self.parent = parent
        self.url = edit_api
        self.mode = mode
        self.source = source
        self.file_name = file_name
        self.task = task
        self.software_name = software_name
        self.comment = comment
        self.email = email
        self.password = password
        self.callback = UploadSignal()

    def run(self):
        source_name, source_ext = os.path.splitext(self.source)

        # /edit/logon 
        logon_url = "{}/login/".format(self.url)
        client = requests.session()

        # Retrieve the CSRF token first
        res = client.get(logon_url).cookies
        csrf = client.get(logon_url).cookies['csrftoken']

        # http://10.147.19.55:8202/edit/login/   
        login_data = dict(username=self.email, password=self.password, csrfmiddlewaretoken=csrf, next='/')
        r = client.post(logon_url, data=login_data, headers=dict(Referer=logon_url))

        upload_to = os.path.basename(self.source)

        encoder = MultipartEncoder(fields = { 
            "task_id": self.task["id"],
            "user_id": self.email,
            "software": self.software_name,
            "mode": self.mode,
            "file_name": upload_to,
            "comment": self.comment,
            "csrfmiddlewaretoken": csrf,
            'input_file': (upload_to, open(self.source, 'rb'), 'rb')
        })

        encoder._read = encoder.read
        encoder.read = lambda size: encoder._read(int(_READ_SIZE))

        progress_callback = create_callback(encoder, self.callback, self.source)
        monitor = MultipartEncoderMonitor(encoder, progress_callback)
        headers = {'Content-Type': monitor.content_type }

        upload_url = "{}/api/upload/".format(self.url)
        try:
            r = client.post(upload_url, data=monitor, headers=headers, auth=(self.email, self.password))
            self.callback.done.emit({
                "status": "ok",
                "source": self.source,
                "message": "upload complete"
            })
            message = r.json()['message']
            # print('\n[Return status {0} {1}]'.format(r.status_code, message))
        except KeyboardInterrupt:
            print('\nUpload cancelled.')
        except Exception as e:
            print(e)
            self.callback.done.emit({
                "status": "error",
                "source": self.source,
                "message": "error uploading {}".format(e)
            })            

        return True        

