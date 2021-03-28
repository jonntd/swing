# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entity_info_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EntityInfoDialog(object):
    def setupUi(self, EntityInfoDialog):
        if not EntityInfoDialog.objectName():
            EntityInfoDialog.setObjectName(u"EntityInfoDialog")
        EntityInfoDialog.resize(1060, 809)
        EntityInfoDialog.setSizeGripEnabled(True)
        self.verticalLayout = QVBoxLayout(EntityInfoDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutProject = QHBoxLayout()
        self.horizontalLayoutProject.setObjectName(u"horizontalLayoutProject")
        self.labelProject = QLabel(EntityInfoDialog)
        self.labelProject.setObjectName(u"labelProject")
        self.labelProject.setMinimumSize(QSize(100, 0))
        self.labelProject.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayoutProject.addWidget(self.labelProject)

        self.lineEditProject = QLineEdit(EntityInfoDialog)
        self.lineEditProject.setObjectName(u"lineEditProject")
        self.lineEditProject.setEnabled(False)

        self.horizontalLayoutProject.addWidget(self.lineEditProject)


        self.verticalLayout.addLayout(self.horizontalLayoutProject)

        self.horizontalLayoutEntity = QHBoxLayout()
        self.horizontalLayoutEntity.setObjectName(u"horizontalLayoutEntity")
        self.verticalLayoutEntity = QVBoxLayout()
        self.verticalLayoutEntity.setObjectName(u"verticalLayoutEntity")
        self.horizontalLayoutName = QHBoxLayout()
        self.horizontalLayoutName.setObjectName(u"horizontalLayoutName")
        self.labelEntity = QLabel(EntityInfoDialog)
        self.labelEntity.setObjectName(u"labelEntity")
        self.labelEntity.setMinimumSize(QSize(100, 0))
        self.labelEntity.setMaximumSize(QSize(100, 22))

        self.horizontalLayoutName.addWidget(self.labelEntity)

        self.lineEditEntity = QLineEdit(EntityInfoDialog)
        self.lineEditEntity.setObjectName(u"lineEditEntity")
        self.lineEditEntity.setEnabled(False)
        self.lineEditEntity.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayoutName.addWidget(self.lineEditEntity)

        self.toolButtonWeb = QToolButton(EntityInfoDialog)
        self.toolButtonWeb.setObjectName(u"toolButtonWeb")
        self.toolButtonWeb.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayoutName.addWidget(self.toolButtonWeb)


        self.verticalLayoutEntity.addLayout(self.horizontalLayoutName)

        self.textEdit = QTextEdit(EntityInfoDialog)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayoutEntity.addWidget(self.textEdit)


        self.horizontalLayoutEntity.addLayout(self.verticalLayoutEntity)

        self.labelPreview = QLabel(EntityInfoDialog)
        self.labelPreview.setObjectName(u"labelPreview")
        self.labelPreview.setMinimumSize(QSize(160, 160))
        self.labelPreview.setAutoFillBackground(True)
        self.labelPreview.setStyleSheet(u"")
        self.labelPreview.setFrameShape(QFrame.Box)
        self.labelPreview.setFrameShadow(QFrame.Raised)
        self.labelPreview.setAlignment(Qt.AlignCenter)

        self.horizontalLayoutEntity.addWidget(self.labelPreview)


        self.verticalLayout.addLayout(self.horizontalLayoutEntity)

        self.horizontalLayoutTask = QHBoxLayout()
        self.horizontalLayoutTask.setObjectName(u"horizontalLayoutTask")
        self.label = QLabel(EntityInfoDialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayoutTask.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutTask.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayoutTask)

        self.lineTable = QFrame(EntityInfoDialog)
        self.lineTable.setObjectName(u"lineTable")
        self.lineTable.setFrameShape(QFrame.HLine)
        self.lineTable.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.lineTable)

        self.horizontalLayoutFiles = QHBoxLayout()
        self.horizontalLayoutFiles.setObjectName(u"horizontalLayoutFiles")
        self.tableViewFiles = QTableView(EntityInfoDialog)
        self.tableViewFiles.setObjectName(u"tableViewFiles")
        self.tableViewFiles.setSizeIncrement(QSize(0, 10))
        self.tableViewFiles.setBaseSize(QSize(0, 10))

        self.horizontalLayoutFiles.addWidget(self.tableViewFiles)


        self.verticalLayout.addLayout(self.horizontalLayoutFiles)

        self.lineButtons = QFrame(EntityInfoDialog)
        self.lineButtons.setObjectName(u"lineButtons")
        self.lineButtons.setFrameShape(QFrame.HLine)
        self.lineButtons.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.lineButtons)

        self.horizontalLayoutButtons = QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName(u"horizontalLayoutButtons")
        self.pushButtonDownload = QPushButton(EntityInfoDialog)
        self.pushButtonDownload.setObjectName(u"pushButtonDownload")

        self.horizontalLayoutButtons.addWidget(self.pushButtonDownload)

        self.pushButtonPublish = QPushButton(EntityInfoDialog)
        self.pushButtonPublish.setObjectName(u"pushButtonPublish")
        self.pushButtonPublish.setEnabled(False)

        self.horizontalLayoutButtons.addWidget(self.pushButtonPublish)

        self.comboBoxTasks = QComboBox(EntityInfoDialog)
        self.comboBoxTasks.setObjectName(u"comboBoxTasks")
        self.comboBoxTasks.setEnabled(False)
        self.comboBoxTasks.setMinimumSize(QSize(200, 0))

        self.horizontalLayoutButtons.addWidget(self.comboBoxTasks)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutButtons.addItem(self.horizontalSpacer)

        self.pushButtonClose = QPushButton(EntityInfoDialog)
        self.pushButtonClose.setObjectName(u"pushButtonClose")

        self.horizontalLayoutButtons.addWidget(self.pushButtonClose)


        self.verticalLayout.addLayout(self.horizontalLayoutButtons)


        self.retranslateUi(EntityInfoDialog)

        QMetaObject.connectSlotsByName(EntityInfoDialog)
    # setupUi

    def retranslateUi(self, EntityInfoDialog):
        EntityInfoDialog.setWindowTitle(QCoreApplication.translate("EntityInfoDialog", u"Entity Information", None))
        self.labelProject.setText(QCoreApplication.translate("EntityInfoDialog", u"Project", None))
        self.labelEntity.setText(QCoreApplication.translate("EntityInfoDialog", u"Entity", None))
#if QT_CONFIG(tooltip)
        self.toolButtonWeb.setToolTip(QCoreApplication.translate("EntityInfoDialog", u"Open in Kitsu", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonWeb.setText(QCoreApplication.translate("EntityInfoDialog", u"...", None))
        self.labelPreview.setText("")
        self.label.setText(QCoreApplication.translate("EntityInfoDialog", u"File List", None))
        self.pushButtonDownload.setText(QCoreApplication.translate("EntityInfoDialog", u"Download", None))
        self.pushButtonPublish.setText(QCoreApplication.translate("EntityInfoDialog", u"Publish", None))
        self.pushButtonClose.setText(QCoreApplication.translate("EntityInfoDialog", u"Close", None))
    # retranslateUi

