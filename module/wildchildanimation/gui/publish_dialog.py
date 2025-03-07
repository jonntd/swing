# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'publish_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wildchildanimation.gui.swing_utils import fakestr

class Ui_PublishDialog(object):
    def setupUi(self, PublishDialog):
        if not PublishDialog.objectName():
            PublishDialog.setObjectName(u"PublishDialog")
        PublishDialog.resize(629, 597)
        self.verticalLayout_6 = QVBoxLayout(PublishDialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelProject = QLabel(PublishDialog)
        self.labelProject.setObjectName(u"labelProject")
        self.labelProject.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelProject.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelProject)

        self.lineEditProject = QLineEdit(PublishDialog)
        self.lineEditProject.setObjectName(u"lineEditProject")

        self.horizontalLayout_3.addWidget(self.lineEditProject)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelEpisode = QLabel(PublishDialog)
        self.labelEpisode.setObjectName(u"labelEpisode")
        self.labelEpisode.setMinimumSize(QSize(100, 0))
        self.labelEpisode.setFont(font)

        self.horizontalLayout_5.addWidget(self.labelEpisode)

        self.lineEditFor = QLineEdit(PublishDialog)
        self.lineEditFor.setObjectName(u"lineEditFor")

        self.horizontalLayout_5.addWidget(self.lineEditFor)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelSelection = QLabel(PublishDialog)
        self.labelSelection.setObjectName(u"labelSelection")
        self.labelSelection.setMinimumSize(QSize(100, 0))
        self.labelSelection.setFont(font)

        self.horizontalLayout_6.addWidget(self.labelSelection)

        self.lineEditSelection = QLineEdit(PublishDialog)
        self.lineEditSelection.setObjectName(u"lineEditSelection")

        self.horizontalLayout_6.addWidget(self.lineEditSelection)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.labelIcon = QLabel(PublishDialog)
        self.labelIcon.setObjectName(u"labelIcon")
        self.labelIcon.setMinimumSize(QSize(120, 0))
        self.labelIcon.setFrameShape(QFrame.Box)
        self.labelIcon.setFrameShadow(QFrame.Sunken)
        self.labelIcon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.labelIcon)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.groupBoxWorkingFiles = QGroupBox(PublishDialog)
        self.groupBoxWorkingFiles.setObjectName(u"groupBoxWorkingFiles")
        self.groupBoxWorkingFiles.setFont(font)
        self.groupBoxWorkingFiles.setCheckable(True)
        self.gridLayout = QGridLayout(self.groupBoxWorkingFiles)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.groupBoxWorkingFiles)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.labelSoftware = QLabel(self.tab)
        self.labelSoftware.setObjectName(u"labelSoftware")
        self.labelSoftware.setMinimumSize(QSize(100, 0))
        self.labelSoftware.setFont(font)

        self.horizontalLayout_10.addWidget(self.labelSoftware)

        self.comboBoxSoftware = QComboBox(self.tab)
        self.comboBoxSoftware.setObjectName(u"comboBoxSoftware")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSoftware.sizePolicy().hasHeightForWidth())
        self.comboBoxSoftware.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.comboBoxSoftware)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayoutProjectFile = QHBoxLayout()
        self.horizontalLayoutProjectFile.setObjectName(u"horizontalLayoutProjectFile")
        self.radioButtonWorkingFile = QRadioButton(self.tab)
        self.radioButtonWorkingFile.setObjectName(u"radioButtonWorkingFile")
        self.radioButtonWorkingFile.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.radioButtonWorkingFile.setFont(font1)
        self.radioButtonWorkingFile.setChecked(True)

        self.horizontalLayoutProjectFile.addWidget(self.radioButtonWorkingFile)

        self.workingFileEdit = QLineEdit(self.tab)
        self.workingFileEdit.setObjectName(u"workingFileEdit")

        self.horizontalLayoutProjectFile.addWidget(self.workingFileEdit)

        self.workingFileSelectButton = QToolButton(self.tab)
        self.workingFileSelectButton.setObjectName(u"workingFileSelectButton")
        self.workingFileSelectButton.setMinimumSize(QSize(45, 0))
        self.workingFileSelectButton.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayoutProjectFile.addWidget(self.workingFileSelectButton)

        self.toolButtonWorkingFileList = QToolButton(self.tab)
        self.toolButtonWorkingFileList.setObjectName(u"toolButtonWorkingFileList")
        self.toolButtonWorkingFileList.setMinimumSize(QSize(45, 0))
        self.toolButtonWorkingFileList.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayoutProjectFile.addWidget(self.toolButtonWorkingFileList)


        self.verticalLayout_5.addLayout(self.horizontalLayoutProjectFile)

        self.horizontalLayoutProjectFile_4 = QHBoxLayout()
        self.horizontalLayoutProjectFile_4.setObjectName(u"horizontalLayoutProjectFile_4")
        self.radioButtonWorkingDir = QRadioButton(self.tab)
        self.radioButtonWorkingDir.setObjectName(u"radioButtonWorkingDir")
        self.radioButtonWorkingDir.setMinimumSize(QSize(100, 0))
        self.radioButtonWorkingDir.setFont(font1)

        self.horizontalLayoutProjectFile_4.addWidget(self.radioButtonWorkingDir)

        self.workingDirEdit = QLineEdit(self.tab)
        self.workingDirEdit.setObjectName(u"workingDirEdit")

        self.horizontalLayoutProjectFile_4.addWidget(self.workingDirEdit)

        self.workingDirSelectButton = QToolButton(self.tab)
        self.workingDirSelectButton.setObjectName(u"workingDirSelectButton")
        self.workingDirSelectButton.setMinimumSize(QSize(45, 0))
        self.workingDirSelectButton.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayoutProjectFile_4.addWidget(self.workingDirSelectButton)

        self.toolButtonWorkingDirFilter = QToolButton(self.tab)
        self.toolButtonWorkingDirFilter.setObjectName(u"toolButtonWorkingDirFilter")
        self.toolButtonWorkingDirFilter.setMinimumSize(QSize(45, 0))
        self.toolButtonWorkingDirFilter.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayoutProjectFile_4.addWidget(self.toolButtonWorkingDirFilter)


        self.verticalLayout_5.addLayout(self.horizontalLayoutProjectFile_4)

        self.labelWorkingFilesMessage = QLabel(self.tab)
        self.labelWorkingFilesMessage.setObjectName(u"labelWorkingFilesMessage")
        self.labelWorkingFilesMessage.setAutoFillBackground(True)
        self.labelWorkingFilesMessage.setStyleSheet(u"color: rgb(0, 170, 0)")
        self.labelWorkingFilesMessage.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_5.addWidget(self.labelWorkingFilesMessage)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableViewReferences = QTableView(self.tab_2)
        self.tableViewReferences.setObjectName(u"tableViewReferences")

        self.verticalLayout_3.addWidget(self.tableViewReferences)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.referencesAddPushButton = QPushButton(self.tab_2)
        self.referencesAddPushButton.setObjectName(u"referencesAddPushButton")
        self.referencesAddPushButton.setEnabled(True)
        self.referencesAddPushButton.setFont(font1)

        self.horizontalLayout_8.addWidget(self.referencesAddPushButton)

        self.referencesRemovePushButton = QPushButton(self.tab_2)
        self.referencesRemovePushButton.setObjectName(u"referencesRemovePushButton")
        self.referencesRemovePushButton.setEnabled(True)
        self.referencesRemovePushButton.setFont(font1)

        self.horizontalLayout_8.addWidget(self.referencesRemovePushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBoxWorkingFiles)

        self.groupBoxOutputFiles = QGroupBox(PublishDialog)
        self.groupBoxOutputFiles.setObjectName(u"groupBoxOutputFiles")
        self.groupBoxOutputFiles.setFont(font)
        self.groupBoxOutputFiles.setAcceptDrops(True)
        self.groupBoxOutputFiles.setFlat(False)
        self.groupBoxOutputFiles.setCheckable(True)
        self.verticalLayout = QVBoxLayout(self.groupBoxOutputFiles)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelReviewTile = QLabel(self.groupBoxOutputFiles)
        self.labelReviewTile.setObjectName(u"labelReviewTile")
        self.labelReviewTile.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.labelReviewTile)

        self.reviewTitleLineEdit = QLineEdit(self.groupBoxOutputFiles)
        self.reviewTitleLineEdit.setObjectName(u"reviewTitleLineEdit")

        self.horizontalLayout_4.addWidget(self.reviewTitleLineEdit)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelTask = QLabel(self.groupBoxOutputFiles)
        self.labelTask.setObjectName(u"labelTask")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelTask.sizePolicy().hasHeightForWidth())
        self.labelTask.setSizePolicy(sizePolicy1)
        self.labelTask.setMinimumSize(QSize(100, 0))
        self.labelTask.setFont(font)
        self.labelTask.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.labelTask)

        self.comboBoxTaskStatus = QComboBox(self.groupBoxOutputFiles)
        self.comboBoxTaskStatus.setObjectName(u"comboBoxTaskStatus")
        sizePolicy.setHeightForWidth(self.comboBoxTaskStatus.sizePolicy().hasHeightForWidth())
        self.comboBoxTaskStatus.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.comboBoxTaskStatus)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayoutProjectFile_6 = QHBoxLayout()
        self.horizontalLayoutProjectFile_6.setObjectName(u"horizontalLayoutProjectFile_6")
        self.radioButtonOutputFile = QRadioButton(self.groupBoxOutputFiles)
        self.radioButtonOutputFile.setObjectName(u"radioButtonOutputFile")
        self.radioButtonOutputFile.setMinimumSize(QSize(100, 0))
        self.radioButtonOutputFile.setFont(font1)
        self.radioButtonOutputFile.setChecked(True)

        self.horizontalLayoutProjectFile_6.addWidget(self.radioButtonOutputFile)

        self.outputFileEdit = QLineEdit(self.groupBoxOutputFiles)
        self.outputFileEdit.setObjectName(u"outputFileEdit")

        self.horizontalLayoutProjectFile_6.addWidget(self.outputFileEdit)

        self.outputFileSelectButton = QToolButton(self.groupBoxOutputFiles)
        self.outputFileSelectButton.setObjectName(u"outputFileSelectButton")
        self.outputFileSelectButton.setMinimumSize(QSize(45, 0))
        self.outputFileSelectButton.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayoutProjectFile_6.addWidget(self.outputFileSelectButton)

        self.toolButtonOutputFileList = QToolButton(self.groupBoxOutputFiles)
        self.toolButtonOutputFileList.setObjectName(u"toolButtonOutputFileList")
        self.toolButtonOutputFileList.setMinimumSize(QSize(45, 0))
        self.toolButtonOutputFileList.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayoutProjectFile_6.addWidget(self.toolButtonOutputFileList)


        self.verticalLayout.addLayout(self.horizontalLayoutProjectFile_6)

        self.horizontalLayoutProjectFile_5 = QHBoxLayout()
        self.horizontalLayoutProjectFile_5.setObjectName(u"horizontalLayoutProjectFile_5")
        self.radioButtonOutputDir = QRadioButton(self.groupBoxOutputFiles)
        self.radioButtonOutputDir.setObjectName(u"radioButtonOutputDir")
        self.radioButtonOutputDir.setMinimumSize(QSize(100, 0))
        self.radioButtonOutputDir.setFont(font1)

        self.horizontalLayoutProjectFile_5.addWidget(self.radioButtonOutputDir)

        self.outputDirEdit = QLineEdit(self.groupBoxOutputFiles)
        self.outputDirEdit.setObjectName(u"outputDirEdit")

        self.horizontalLayoutProjectFile_5.addWidget(self.outputDirEdit)

        self.outputDirSelectButton = QToolButton(self.groupBoxOutputFiles)
        self.outputDirSelectButton.setObjectName(u"outputDirSelectButton")
        self.outputDirSelectButton.setMinimumSize(QSize(45, 0))
        self.outputDirSelectButton.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayoutProjectFile_5.addWidget(self.outputDirSelectButton)

        self.toolButtonReviewFilter = QToolButton(self.groupBoxOutputFiles)
        self.toolButtonReviewFilter.setObjectName(u"toolButtonReviewFilter")
        self.toolButtonReviewFilter.setMinimumSize(QSize(45, 0))
        self.toolButtonReviewFilter.setMaximumSize(QSize(45, 16777215))
        self.toolButtonReviewFilter.setFont(font)

        self.horizontalLayoutProjectFile_5.addWidget(self.toolButtonReviewFilter)


        self.verticalLayout.addLayout(self.horizontalLayoutProjectFile_5)

        self.labelOutputFilesMessage = QLabel(self.groupBoxOutputFiles)
        self.labelOutputFilesMessage.setObjectName(u"labelOutputFilesMessage")
        self.labelOutputFilesMessage.setAutoFillBackground(True)
        self.labelOutputFilesMessage.setStyleSheet(u"color: rgb(0, 170, 0)")
        self.labelOutputFilesMessage.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.labelOutputFilesMessage)


        self.verticalLayout_6.addWidget(self.groupBoxOutputFiles)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.commentLabel = QLabel(PublishDialog)
        self.commentLabel.setObjectName(u"commentLabel")
        self.commentLabel.setMinimumSize(QSize(100, 0))
        self.commentLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.commentLabel)

        self.commentEdit = QPlainTextEdit(PublishDialog)
        self.commentEdit.setObjectName(u"commentEdit")
        self.commentEdit.setMinimumSize(QSize(0, 60))

        self.verticalLayout_4.addWidget(self.commentEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButtonOK = QPushButton(PublishDialog)
        self.pushButtonOK.setObjectName(u"pushButtonOK")

        self.horizontalLayout.addWidget(self.pushButtonOK)

        self.pushButtonCancel = QPushButton(PublishDialog)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout.addWidget(self.pushButtonCancel)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.retranslateUi(PublishDialog)

        self.tabWidget.setCurrentIndex(0)
        self.pushButtonOK.setDefault(True)


        QMetaObject.connectSlotsByName(PublishDialog)
    # setupUi

    def retranslateUi(self, PublishDialog):
        PublishDialog.setWindowTitle(fakestr(u"Publish Asset for Task", None))
        self.labelProject.setText(fakestr(u"Project:", None))
        self.labelEpisode.setText(fakestr(u"For", None))
        self.labelSelection.setText(fakestr(u"Task", None))
        self.labelIcon.setText("")
        self.groupBoxWorkingFiles.setTitle(fakestr(u"Working Files", None))
        self.labelSoftware.setText(fakestr(u"Software", None))
        self.radioButtonWorkingFile.setText(fakestr(u"Working File", None))
#if QT_CONFIG(tooltip)
        self.workingFileSelectButton.setToolTip(fakestr(u"Select Working File", None))
#endif // QT_CONFIG(tooltip)
        self.workingFileSelectButton.setText(fakestr(u"...", None))
#if QT_CONFIG(tooltip)
        self.toolButtonWorkingFileList.setToolTip(fakestr(u"Show working file selected for publishing", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonWorkingFileList.setText(fakestr(u"[files]", None))
        self.radioButtonWorkingDir.setText(fakestr(u"Working Dir", None))
#if QT_CONFIG(tooltip)
        self.workingDirSelectButton.setToolTip(fakestr(u"Select Working Directory to Zip and Upload", None))
#endif // QT_CONFIG(tooltip)
        self.workingDirSelectButton.setText(fakestr(u"...", None))
#if QT_CONFIG(tooltip)
        self.toolButtonWorkingDirFilter.setToolTip(fakestr(u"Show working files and directories selected to zip and publish", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonWorkingDirFilter.setText(fakestr(u"[filter]", None))
        self.labelWorkingFilesMessage.setText(fakestr(u"Working files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), fakestr(u"Working Files", None))
        self.referencesAddPushButton.setText(fakestr(u"&Add", None))
        self.referencesRemovePushButton.setText(fakestr(u"&Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), fakestr(u"Secondary Assets", None))
        self.groupBoxOutputFiles.setTitle(fakestr(u"Media for Review ", None))
        self.labelReviewTile.setText(fakestr(u"Title", None))
        self.labelTask.setText(fakestr(u"Status", None))
        self.radioButtonOutputFile.setText(fakestr(u"File", None))
#if QT_CONFIG(tooltip)
        self.outputFileSelectButton.setToolTip(fakestr(u"Select Output File / Preview File", None))
#endif // QT_CONFIG(tooltip)
        self.outputFileSelectButton.setText(fakestr(u"...", None))
#if QT_CONFIG(tooltip)
        self.toolButtonOutputFileList.setToolTip(fakestr(u"Show output / review files selected for publish", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonOutputFileList.setText(fakestr(u"[files]", None))
        self.radioButtonOutputDir.setText(fakestr(u"Directory", None))
#if QT_CONFIG(tooltip)
        self.outputDirSelectButton.setToolTip(fakestr(u"Select Output Directory / Preview Directory to Zip and Upload", None))
#endif // QT_CONFIG(tooltip)
        self.outputDirSelectButton.setText(fakestr(u"...", None))
#if QT_CONFIG(tooltip)
        self.toolButtonReviewFilter.setToolTip(fakestr(u"Show output / review files and directories selected for zip and publish", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonReviewFilter.setText(fakestr(u"[filter]", None))
        self.labelOutputFilesMessage.setText(fakestr(u"Output Files", None))
        self.commentLabel.setText(fakestr(u"Comments", None))
#if QT_CONFIG(tooltip)
        self.pushButtonOK.setToolTip(fakestr(u"Publish Working Files and / or Output Files", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonOK.setText(fakestr(u"Publish", None))
        self.pushButtonCancel.setText(fakestr(u"Cancel", None))
    # retranslateUi

