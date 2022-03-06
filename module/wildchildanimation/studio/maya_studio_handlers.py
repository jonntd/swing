# -*- coding: utf-8 -*-
#
# Studio Handler callback methods from Treehouse Swing
#

from email.mime import audio, image
import time
import os
import glob
import sys
import traceback

from PySide2 import QtCore

from wildchildanimation.gui.background_workers import TaskFileInfoThread

from wildchildanimation.gui.maya_resource_loader import ResourceLoaderDialogGUI
from wildchildanimation.gui.publish import PublishDialogGUI
from wildchildanimation.gui.settings import SwingSettings

_maya_loaded = False    
try:
    import maya.cmds as cmds
    import maya.mel as mel
    import maya.OpenMaya as om
    import maya.OpenMayaUI as omui

    import pymel.core as pm
    from pymel.util import putEnv

    from PySide2 import QtWidgets    
    from shiboken2 import wrapInstance

    _maya_loaded = True
except:
    pass

from wildchildanimation.gui.downloads import DownloadDialogGUI
from wildchildanimation.gui.search import SearchFilesDialog
from wildchildanimation.gui.swing_create import SwingCreateDialog
from wildchildanimation.gui.swing_utils import fcount, fcount_name, friendly_string, write_log
from wildchildanimation.maya.swing_maya import SwingMaya

from wildchildanimation.studio.studio_interface import StudioInterface

from wildchildanimation.gui.swing_playblast import SwingPlayblastUi
from wildchildanimation.gui.swing_sequence_playblast import SwingSequencePlayblastUi
from wildchildanimation.maya.swing_export import SwingExportDialog
from wildchildanimation.gui.entity_info import EntityInfoDialog
from wildchildanimation.maya.maya_scene_data import SceneData

def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    if main_window_ptr:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    print("running console mode")
    return None

class MayaStudioHandler(SwingMaya, StudioInterface):

    NAME = "MayaStudioHandler"
    VERSION = "0.0.10"
    SUPPORTED_TYPES = [".ma", ".mb", ".fbx", ".obj", ".mov", ".mp4", ".wav", ".jpg", ".png", ".abc" ]

    def __init__(self):
        super(MayaStudioHandler, self).__init__()

        self.log_output("{} v{}".format(self.NAME, self.VERSION))

    def get_param(self, option, value):
        ### runs a custom value request against the local dcc
        if option == "frame_range":

            if value == "Render":
                start_frame = int(cmds.getAttr("defaultRenderGlobals.startFrame"))
                end_frame = int(cmds.getAttr("defaultRenderGlobals.endFrame"))
            elif value == "Playback":
                start_frame = int(cmds.playbackOptions(q=True, minTime=True))
                end_frame = int(cmds.playbackOptions(q=True, maxTime=True))
            elif value == "Animation":
                start_frame = int(cmds.playbackOptions(q=True, animationStartTime=True))
                end_frame = int(cmds.playbackOptions(q=True, animationEndTime=True))
            else:
                raise RuntimeError("Invalid frame range preset: {0}".format(value))

            return (start_frame, end_frame)

        raise None

    def set_globals(self, **kwargs):
        write_log("on_globals")

        if "project" in kwargs:
            putEnv("project", kwargs["project"])

        if "episode" in kwargs:
            putEnv("episode", kwargs["episode"])

        if "sequence" in kwargs:
            putEnv("sequence", kwargs["sequence"])

        if "task_type_name" in kwargs:
            putEnv("task_type_name", kwargs["task_type_name"])

        if "shot" in kwargs:
            putEnv("shot", kwargs["shot"])

        if "asset" in kwargs:
            putEnv("asset", kwargs["asset"])

        if "frame_in" in kwargs:
            putEnv("frame_in", kwargs["frame_in"])

        if "frame_out" in kwargs:
            putEnv("frame_out", kwargs["frame_out"])

        if "frame_count" in kwargs:
            putEnv("frame_count", kwargs["frame_count"])

        return True

    #
    # returns a list of unresolved files in a scene
    def list_unresolved(self):
        self.log_output("searching for unresolved references")
        refs = cmds.file(query = True, list = True, unresolvedName = True)

        self.log_output("searching for unresolved references {}".format(refs))
        return refs

    # tries to import the file specified in source into the currently open scene
    def load_file(self, **kwargs):
        source = kwargs["source"]
        force = kwargs["force"]

        self.log_output("load_file '{}'".format(source))
        #working_dir = kwargs["working_dir"]

        #self.log_output("load_file:: {0} to {1}".format(source, working_dir))
        #self.log_output("Source  {0}".format(working_dir))
        #self.log_output("Working Dir {0}".format(working_dir))

        filename, file_extension = os.path.splitext(source)

        if file_extension in MayaStudioHandler.SUPPORTED_TYPES:
            prompt_val = cmds.file(prompt=True, q=True)
            try:
                if not force and cmds.file(q = True, modified = True):
                    if QtWidgets.QMessageBox.question(None, 'Unsaved changes', 'Current scene has unsaved changes. Continue?') == QtWidgets.QMessageBox.StandardButton.Yes:
                        force = True
                    else:
                        self.log_output("Aborted load file")
                        return

                cmds.file(source, open = True, ignoreVersion = True, prompt = False, force = force)
            except:
                traceback.print_exc(file=sys.stdout)
                self.log_error("Error processing importing reference {}".format(source))
                return False
            finally:
                cmds.file(prompt = prompt_val)

        else:
            self.log_error("File extension not valid {0}".format(file_extension))                

        self.log_output("load_file {} completed".format(source))
        return True

    # tries to import the file specified in source into the currently open scene
    def import_file(self, **kwargs):
        source = kwargs["source"]
        self.log_output("import_file '{}'".format(source))
        #working_dir = kwargs["working_dir"]

        #self.log_output("import_file:: {0} to {1}".format(source, working_dir))
        #self.log_output("Source  {0}".format(working_dir))
        #self.log_output("Working Dir {0}".format(working_dir))

        filename, file_extension = os.path.splitext(source)

        if file_extension in MayaStudioHandler.SUPPORTED_TYPES:
            self.log_output("Loading file {}".format(source))
            try:
                pm.system.importFile(source)
                self.log_output("importFile {} successfully".format(filename))
            except:
                traceback.print_exc(file=sys.stdout)
                self.log_error("Error processing load file {}".format(source))
                return False
        else:
            self.log_error("File extension not valid {0}".format(file_extension))                

        self.log_output("import_file {} completed".format(source))
        return True  

    # tries to import the file specified in source into the currently open scene
    def import_reference(self, **kwargs):
        source = kwargs["source"]
        #working_dir = kwargs["working_dir"]
        namespace = kwargs["namespace"]

        self.log_output("Import Ref '{}:{}'".format(source, namespace))

        #self.log_output("load_reference:: {0}".format(source, working_dir))
        #self.log_output("Source  {0}".format(working_dir))
        #self.log_output("Working Dir {0}".format(working_dir))
        self.log_output("Namespace {0}".format(namespace))

        filename, file_extension = os.path.splitext(source)

        if file_extension in MayaStudioHandler.SUPPORTED_TYPES:
            self.log_output("import_reference {}".format(source))

            prompt_val = cmds.file(prompt=True, q=True)
            try:
                cmds.file(source, prompt = False, reference = True, ignoreVersion = True, namespace = namespace, options = "v=0;")
                self.log_output('cmds.file({0}, prompt = False, reference = True, ignoreVersion = True, namespace = {1}, options = "v=0;"'.format(source, namespace))
            except:
                traceback.print_exc(file=sys.stdout)
                self.log_error("Error processing importing reference {}".format(source))
                return False
            finally:
                cmds.file(prompt = prompt_val)

        else:
            self.log_error("File extension not valid {0}".format(file_extension))

        self.log_output("import_reference {} completed".format(source))
        return True

    def create_folder(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)  

    def last_modified(self, file_item):
        # returns last time inode changed in string
        return time.ctime(os.path.getmtime(file_item))

    #
    # Swing API Handlers
    #
    def on_task_create(self, results):
        task_dir = results["project_dir"]
        task = results["task"]
        
        working_file = friendly_string("_".join(self.get_task_sections(task)).lower())    

        #add software
        working_file_name = "{}.ma".format(working_file)
        self.createDialog = SwingCreateDialog(parent = None, task_id = task["id"], entity_id = task["entity"]["id"])

        existingFile = None
        if os.path.exists(task_dir):
            if os.path.exists(os.path.join(task_dir, working_file_name)):
                existingFile = os.path.join(task_dir, working_file_name)

                # check for incremental saves
                file_list = glob.glob("{}*.ma".format(os.path.join(task_dir, working_file)))
                if len(file_list) > 0:
                    # load last file by modified date
                    file_list.sort(key=lambda x: os.path.getmtime(x), reverse=True)
                    existingFile = file_list[0]
 
                # self.createDialog.checkBoxLoadExisting.setVisible(True)
                self.createDialog.labelFileDetails.setText("Working file [{}] found, last modified: {}".format(existingFile, self.last_modified(existingFile)))
                self.createDialog.lineEditEntity.setText(existingFile)
               
                self.createDialog.rbOpenExisting.setChecked(True)

                # self.createDialog.checkBoxLoadExisting.setVisible(True)
                # self.createDialog.labelFileDetails.setText("Existing file last modified: {}".format(self.last_modified(existingFile)))
                # self.createDialog.rbOpenExisting.setChecked(True)

        result = self.createDialog.exec_()
        if result:
            working_dir = self.createDialog.get_working_dir()
            file_name = self.createDialog.get_file_name()

            if existingFile and not self.createDialog.rbOpenExisting.isChecked():

                if QtWidgets.QMessageBox.question(None, 'Warning: Existing file found', 'If you continue, this file will be lost, are you sure?') != QtWidgets.QMessageBox.StandardButton.Yes:
                    self.log_output("Aborted load file")
                    return

            if existingFile and self.createDialog.rbOpenExisting.isChecked():
                self.load_file(source = existingFile, working_dir = working_dir, force = True)
            else:
                frame_in = self.createDialog.get_start_frame()
                frame_out = self.createDialog.get_end_frame()
                frame_rate = self.createDialog.get_frame_rate()

                project_file = os.path.join(working_dir, file_name)

                #directory = self.createDialog.working_dir        
                self.log_output("on_create {} [{}]".format(working_dir, file_name))
                self.log_output("on_create frame_in [{}]".format(frame_in))
                self.log_output("on_create frame_out [{}]".format(frame_out))
                self.log_output("on_create frame_rate [{}]".format(frame_rate))

                #self.log_output("Source  {0}".format(kwargs["source"]))
                #self.log_output("Working Dir {0}".format(kwargs["working_dir"]))
                #self.log_output("Namespace {0}".format(kwargs["namespace"]))

                fn, fext = os.path.splitext(file_name)

                if fext in MayaStudioHandler.SUPPORTED_TYPES:
                    self.log_output("Creating file {}".format(project_file))

                    prompt_val = cmds.file(prompt=True, q=True)
                    try:
                        self.create_folder(working_dir)
                        
                        cmds.file(new = True, force = True)
                        cmds.file(rename = project_file)

                        self.log_output("setting frame rate to {}".format(frame_rate))
                        frame_rate = self.set_frame_rate(frame_rate)

                        self.log_output("setting animation range from {} to {}".format(frame_in, frame_out))
                        cmds.playbackOptions(edit=True, animationStartTime = frame_in, animationEndTime = frame_out)
                        cmds.playbackOptions(edit=True, minTime = frame_in, maxTime = frame_out)

                        start = cmds.playbackOptions(q=True, min=True)
                        self.log_output("set start to {}".format(start))
                        cmds.currentTime(start, edit = True)

                        self.log_output("save file {}".format(project_file))
                        cmds.file(save = True, type='mayaAscii')

                        #playButtonStart;
                        #timeField -edit -value `currentTime -query` TimeSlider|MainTimeSliderLayout|formLayout8|timeField1;


                        self.log_output("on_create <-- {}".format(project_file))
                    except:
                        traceback.print_exc(file=sys.stdout)
                        self.log_error("Error processing creating new file {}".format(project_file))
                        return False
                    finally:
                        cmds.file(prompt = prompt_val)

                else:
                    self.log_error("File extension not valid {0}".format(fn))

            self.log_output("saving scene descriptor to json")
            SceneData().save_task_data(task)
            
            self.log_output("create_file complete")
        return True 

    def on_create(self, **kwargs):
        try:
            task = kwargs["task"]
            #task = task_info["task"]

            self.log_output("task: {}".format(task))
            self.log_output("task: {}".format(task["id"]))

            self.taskLoader = TaskFileInfoThread(parent = self, task = task["id"], project_root = SwingSettings.get_instance().swing_root())
            self.taskLoader.callback.loaded.connect(self.on_task_create)
            QtCore.QThreadPool.globalInstance().start(self.taskLoader)
        except:
            traceback.print_exc(file=sys.stdout)
            
            self.log_error("on_create: args {}".format(kwargs))


    def on_search(self, **kwargs):
        try:
            self.log_output("on_search::")
            project = kwargs["project"]

            if "text" in kwargs:
                text = kwargs["text"]
            else:
                text = ''

            if "task_types" in kwargs:
                task_types = kwargs["task_types"]
            else:
                task_types = None

            if "status_types" in kwargs:
                status_types = kwargs["status_types"]
            else:
                status_types = None
            
            self.searchDialog = SearchFilesDialog(parent = None, text = text, project = project, task_types = task_types, status_types = status_types)
            if len(text) > 0:
                self.searchDialog.process()
            result = self.searchDialog.exec_()

            if result:
                self.downloadDialog = DownloadDialogGUI(parent = None, handler = self, file_list = self.searchDialog.get_file_list())
                self.downloadDialog.show()          
        except:
            traceback.print_exc(file=sys.stdout)
            self.log_error("on_search: args {}".format(kwargs))


    def on_load(self, **kwargs):
        if len(kwargs) == 0:
            #fixme: find event calling empty kwargs
            return False

        try:
            # we need parent so dialog doesn't go awol
            # we need entity for name space management
            if "parent" in kwargs:
                parent = kwargs["parent"]
            else:
                parent = self

            if "namespace" in kwargs:
                namespace = kwargs["namespace"]
            else:
                namespace = False

            entity = kwargs["entity"]
            selected = kwargs["selected"]

            loaderDialog = ResourceLoaderDialogGUI(parent = parent, handler = self, resource = selected, entity = entity, namespace = namespace)
            loaderDialog.show()        
        except:
            traceback.print_exc(file=sys.stdout)
            self.log_error("on_load: args {}".format(kwargs))
     
    def scan_working_dir(self, directory, ext):
        print("Searching {} for {}".format(directory, ext))
        file_list = []
        file_list += filter(os.path.isfile, glob.glob(directory + '/{}'.format(ext)))

        print("Returning {}".format(len(file_list)))
        file_list = sorted(file_list, key = os.path.getmtime)
        return file_list

    def on_publish(self, **kwargs):
        try:
            print("on_publish: {}".format(kwargs))

            task = kwargs["task"]
            #task = task_info["task"]         
            #task_dir = task["project_dir"]
            task_dir = self.get_scene_path()

            task_type = task["task_type"]
            if "name" in task_type:
                task_type = task["task_type"]["name"]

            print("on_publish: task_type {}".format(task_type))
            print("on_publish: task_dir {}".format(task_dir))

            #if "task_types" in kwargs:
            #    task_types = kwargs["task_types"]
            #else:
            #    task_types = None   

            self.publishDialog = PublishDialogGUI(task = task)      
            self.publishDialog.reset_queue()      

            file_path = cmds.file(q = True, sn = True)
            self.publishDialog.set_working_file(file_path)        

            cached_dir = os.path.join(task_dir, 'cache')
            if os.path.exists(cached_dir):
                print("Checking alembics: {}".format(cached_dir))

                file_list = self.scan_working_dir(cached_dir, '*.abc')
                if len(file_list) > 0:
                    self.publishDialog.add_reference_file(file_list[0], 'Alembic')
                    self.publishDialog.load_reference_table()
                else:
                    print("No alembic files found")

            playblast_dir = None
            if "layout" in task_type.lower():
                print("Checking for playblasts")
                # get latest version from playblasts folder

                playblast_root = os.path.join(task_dir, "playblasts")
                if not os.path.exists(playblast_root):
                    print("No playblasts found")
                else:
                    print("Scanning {} for playblast directories".format(playblast_root))

                    playblast_directories = glob.glob("{}/v*".format(playblast_root))
                    print("Scanning {}".format(playblast_directories))

                    playblast_directories = filter(os.path.isdir, playblast_directories)

                    print("Found directories {}".format(playblast_directories))
                    playblast_directories = sorted(playblast_directories, key = os.path.getmtime, reverse=True)                

                    if len(playblast_directories) > 0:
                        playblast_dir = playblast_directories[0]
                    else:
                        print("No playblasts folders found")

                    shot_list = self.get_shot_list()
                    shot_playblasts = []

                    print("Checking for shots")
                    for item in shot_list:
                        shot_playblasts.append("{}.mp4".format(item["name"]))

                    print("Found {} shots in scene".format(len(shot_playblasts)))

                    # default to include all shots in camera sequencer
                    self.publishDialog.set_of_include(shot_playblasts)

                    self.publishDialog.set_output_dir(playblast_dir) 
            else:
                playblast_dir = os.path.join(task_dir, 'playblasts')
                if os.path.exists(playblast_dir):
                    print("Checking playblast_dir: {}".format(playblast_dir))
                    file_list = self.scan_working_dir(playblast_dir, '*.mp4')
                    if len(file_list) > 0:
                        self.log_output("Adding playblast: {}".format(file_list[0]))
                        self.publishDialog.set_output_file(file_list[0])

            self.publishDialog.show()     #
        except:
            traceback.print_exc(file=sys.stdout)
            self.log_error("on_publish: args {}".format(kwargs))               

    def on_export(self, **kwargs):
        try:
            task = kwargs["task"] 

            working_dir = self.get_scene_path()

            #if "task_types" in kwargs:
            #    task_types = kwargs["task_types"]
            #else:
            #    task_types = None        

            self.exportDialog = SwingExportDialog(handler = self, task = task, working_dir = working_dir)
            self.exportDialog.show()
        except:
            traceback.print_exc(file=sys.stdout)
            self.log_error("on_export: args {}".format(kwargs))               

        return True        

    def on_save(self, **kwargs):
        try:
            file_path = cmds.file(q = True, sn = True)
            file_base = os.path.basename(file_path)
            file_name, file_ext = os.path.splitext(file_base)

            request = {
                "source": file_base,
                "file_path": file_path,
                "file_name": file_name,
                "file_ext": file_ext,            
            }
            return request
        except:
            traceback.print_exc(file=sys.stdout)
            self.log_error("on_save: args {}".format(kwargs))               


    def on_entity_info(self, **kwargs):
        try:
            entity_id = kwargs["entity_id"]
            task_types = kwargs["task_types"]
            self.entityDialog = EntityInfoDialog(entity = entity_id, handler = self, task_types = task_types)
            self.entityDialog.show()              
        except:
            traceback.print_exc(file=sys.stdout)
            self.log_error("on_entity_info: args {}".format(kwargs))               

            return False 

        return True            

    def on_playblast(self, **kwargs):
        try:
            task = kwargs["task"]
            task_dir = self.get_scene_path()
            working_file = friendly_string("_".join(self.get_task_sections(task)))
            artist = self.get_user_name()
            scene_dir = self.get_scene_path()
            scene_name = self.get_scene_name()

            self.log_output("on_playblast::task {}".format(task))
            self.log_output("on_playblast::task_dir {}".format(task_dir))
            self.log_output("on_playblast::working_file {}".format(working_file))
            self.log_output("on_playblast::artist {}".format(artist))
            self.log_output("on_playblast::scene_name  {}".format(scene_name))
            self.log_output("on_playblast::scene_dir  {}".format(scene_dir))

            if len(scene_dir) == 0 or scene_name == 'untitled':
                QtWidgets.QMessageBox.warning(None, 'Playblasting unsaved changes', 'Please save the current project file or load a saved task before playblasting')
                return False

            if "layout" in working_file.lower():
                dialog = SwingSequencePlayblastUi()

                playblast_count = 1
                playblast_version_string = "v" + "{}".format(playblast_count).zfill(3)

                playblasts = os.path.join(task_dir, "playblasts", playblast_version_string)
                while os.path.exists(playblasts):
                    playblast_count += 1
                    playblast_version_string = "v" + "{}".format(playblast_count).zfill(3)

                    playblasts = os.path.join(task_dir, "playblasts", playblast_version_string)                
            else:
                dialog = SwingPlayblastUi()

                # count all media files in playblast dir
                playblast_count = 1
                if os.path.exists(task_dir):
                    playblasts = os.path.join(task_dir, "playblasts")
                    if os.path.exists(playblasts):
                        playblast_count = fcount(playblasts) + 1

            self.log_output("on_playblast::playblast_count  {}".format(playblast_count))            

            playblast_version ="{}".format(playblast_count).zfill(3)
            
            playblast_filename = "{}_v{}".format(working_file, playblast_version)
            playblast_target = os.path.join(playblasts, playblast_filename).lower()

            self.log_output("open: {} {} {}".format(playblast_version, playblast_filename, playblast_target))
            try:
                dialog.set_output_file_name(playblast_target)
                dialog.set_artist(artist)
                dialog.set_caption_text(" ".join(self.get_task_sections(task)))
                dialog.show()

                self.log_output("open: playblast")
            except:
                traceback.print_exc(file=sys.stdout)
                return False 

            return True
            # playblast  -format avi -sequenceTime 0 -clearCache 1 -viewer 1 -showOrnaments 1 -fp 4 -percent 50 -compression "none" -quality 70;
        except:
            traceback.print_exc(file=sys.stdout)
            self.log_error("on_playblast: args {}".format(kwargs))               

    def load_task(self, task_id):
        self.taskLoader = TaskFileInfoThread(parent = self, task = task_id, project_root=SwingSettings.get_instance().swing_root())
        return self.taskLoader.run()

    def on_sequencer_create_shots(self, **kwargs):
        shot_list = kwargs["shot_list"]
        image_plane = kwargs["image_plane"]
        padding = kwargs["padding"]
        frame_rate = kwargs["fps"]

        '''
                "id": item_name.split('.')[0],
                "e": False,
                "shotName": item_name,
                "track": track_no,
                "currentCamera": camera,
                "startTime": track_range.start_time.value + 1,
                "endTime": track_range.end_time_exclusive().value,
                "sequencerStartTime": track_range.start_time.value + 1,
                "sequencerEndTime": track_range.end_time_exclusive().value,
                "audio": audio_file,
                "image_plane": image_plane,
                "padding": self.spinBoxPadShots.value()
        '''

        offset = 0
        ending_at = 0
        shots_created = 0

        if self.get_frame_rate() != frame_rate:
            self.log_output("setting frame rate to {}".format(frame_rate))
            self.set_frame_rate(frame_rate)

        for shot in shot_list:
            if shot["selected"]:
                #self.log_output("Creating Shot {} {} {} {}".format(shot["id"], shot["sequencerStartTime"], shot["sequencerEndTime"], shot["currentCamera"]))
                #self.log_output("Shot Image Plane: {}".format(shot["image_plane"]))
                #self.log_output("Shot Audio: {}".format(shot["audio"]))

                cameras = cmds.camera(name=shot["currentCamera"])
                camera = cameras[0]

                cmds.shot(
                    shot["id"],
                    e=False,
                    shotName=shot["shotName"],
                    track=shot["track"],
                    currentCamera=camera,
                    startTime=shot["startTime"] + offset,
                    endTime=shot["endTime"] + offset,
                    sequenceStartTime=shot["sequencerStartTime"] + offset,
                    sequenceEndTime=shot["sequencerEndTime"] + offset
                )         

                if shot["audio"]:
                    cmds.shot(shot["id"],
                        e=True,
                        audio=shot["audio"]
                    )

                if image_plane:
                    image_plane_shape = "imgpln_{}".format(shot["shotName"]) 
                    
                    try:
                        print("Creating image plane {}:{}".format(image_plane_shape, shot["image_plane"]))
                        #ips = cmds.imagePlane(name = image_plane_shape, camera = cameras[1], fileName = shot["image_plane"])
                        ips = cmds.imagePlane(name = image_plane_shape, camera = camera, fileName = shot["image_plane"])
                        print("Created {} -> {}".format(ips[0], ips[1]))
                        
                        #camera_plane_shape = "{}Shape".format(camera)

                        print("selecting image plane {}".format(ips[0]))
                        mel.eval("select -r {} ;".format(ips[0]))

                        print("set useFrameExtension {}".format(ips[0]))
                        mel.eval('setAttr "{}.useFrameExtension" 1;'.format(ips[0]))

                        print("set alphaGain {}".format(image_plane_shape))
                        mel.eval('setAttr "{}->{}.alphaGain" {};'.format(ips[0], ips[1], image_plane["alphaGain"]))

                        print("set sizeX {}".format(image_plane_shape))
                        mel.eval('setAttr "{}->{}.sizeX" {};'.format(ips[0], ips[1], image_plane["sizeX"]))

                        print("set offsetX {}".format(image_plane_shape))
                        mel.eval('setAttr "{}->{}.offsetX" {};'.format(ips[0], ips[1], image_plane["offsetX"]))

                        print("set offsetY {}".format(image_plane_shape))
                        mel.eval('setAttr "{}->{}.offsetY" {};'.format(ips[0], ips[1], image_plane["offsetY"]))
                    except:
                        traceback.print_exc(file=sys.stdout)
                        print("Error adjusting img plane")
                    # 

                #if shot["image_plane"]:
                #    cmds.shot(shot["id"],
                #        e=True,
                #        clip=shot["image_plane"]
                #    )

                # add padding
                if padding:
                    offset += padding

                # remember max
                if (shot["sequencerEndTime"] + offset) > ending_at:
                    ending_at = shot["sequencerEndTime"] + offset

                shots_created += 1
            # shot selected
        # all shots

        if shots_created > 0:
            try:
                self.log_output("setting animation range from {} to {}".format(1, ending_at))
                cmds.playbackOptions(edit=True, animationStartTime = 1, animationEndTime = ending_at)
                cmds.playbackOptions(edit=True, minTime = 1, maxTime = ending_at)

                start = cmds.playbackOptions(q=True, min=True)
                self.log_output("set start to {}".format(start))
                cmds.currentTime(start, edit = True)

                self.log_output("set fitPanel all")
                mel.eval('sequencerPanelBarSection1Callback("FrameAllBtn", "sequenceEditorPanel1SequenceEditor", "sequenceEditorPanel1Window|sequenceEditorPanel1|sequenceBaseForm|sequenceToolbarFrame");')
                mel.eval('fitPanel -all;')
            except:
                traceback.print_exc(file=sys.stdout)
                print("Error adjusting sequencerPanelBarSection1Callback")                

        return True

    def reset_workspace_control(self):
        self.log_output("reset_workspace_control")
        try:
            from wildchildanimation.maya.maya_swing_control import SwingMayaUI
            SwingMayaUI.display()
        except:
            traceback.print_exc(file=sys.stdout)
            self.log_error("reset_workspace_control")               

'''
        # exports current selected
        source = kwargs["target"]
        working_dir = kwargs["working_dir"]
        selection = kwargs["selection"]

        target = os.path.join(working_dir, source)
        target = os.path.normpath(target)       

        if "All" in selection:
            # select all dag objects and all dependency nodes
            pm.select(all = True) 

        # https://tech-artists.org/t/solved-problem-exporting-fbx-from-maya-without-animation/8796        
        cmds.FBXResetExport()
        cmds.FBXExportHardEdges('-v', True)
        cmds.FBXExportSmoothingGroups('-v', True)
        cmds.FBXExportTangents('-v', True)
        cmds.FBXExportBakeComplexAnimation('-v', True)

        cmds.FBXExport('-file', target, '-s')

        self.log_output("fbx export {0} {1}".format(source, working_dir))        
        return True
'''