# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'swing_sequence_playblast_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wildchildanimation.gui.swing_utils import fakestr

class Ui_SequencePlayblastDialog(object):
    def setupUi(self, SequencePlayblastDialog):
        if not SequencePlayblastDialog.objectName():
            SequencePlayblastDialog.setObjectName(u"SequencePlayblastDialog")
        SequencePlayblastDialog.resize(635, 490)
        SequencePlayblastDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(SequencePlayblastDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayoutPathing = QVBoxLayout()
        self.verticalLayoutPathing.setObjectName(u"verticalLayoutPathing")
        self.horizontalLayoutFile = QHBoxLayout()
        self.horizontalLayoutFile.setObjectName(u"horizontalLayoutFile")
        self.filename_label = QLabel(SequencePlayblastDialog)
        self.filename_label.setObjectName(u"filename_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filename_label.sizePolicy().hasHeightForWidth())
        self.filename_label.setSizePolicy(sizePolicy)
        self.filename_label.setMinimumSize(QSize(100, 0))
        self.filename_label.setMaximumSize(QSize(80, 16777215))
        self.filename_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayoutFile.addWidget(self.filename_label)

        self.output_filename_le = QLineEdit(SequencePlayblastDialog)
        self.output_filename_le.setObjectName(u"output_filename_le")

        self.horizontalLayoutFile.addWidget(self.output_filename_le)

        self.output_dir_path_select_btn = QToolButton(SequencePlayblastDialog)
        self.output_dir_path_select_btn.setObjectName(u"output_dir_path_select_btn")
        self.output_dir_path_select_btn.setMinimumSize(QSize(40, 0))
        self.output_dir_path_select_btn.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayoutFile.addWidget(self.output_dir_path_select_btn)

        self.force_overwrite_cb = QCheckBox(SequencePlayblastDialog)
        self.force_overwrite_cb.setObjectName(u"force_overwrite_cb")

        self.horizontalLayoutFile.addWidget(self.force_overwrite_cb)

        self.output_dir_path_show_folder_btn = QPushButton(SequencePlayblastDialog)
        self.output_dir_path_show_folder_btn.setObjectName(u"output_dir_path_show_folder_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.output_dir_path_show_folder_btn.sizePolicy().hasHeightForWidth())
        self.output_dir_path_show_folder_btn.setSizePolicy(sizePolicy1)
        self.output_dir_path_show_folder_btn.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayoutFile.addWidget(self.output_dir_path_show_folder_btn)


        self.verticalLayoutPathing.addLayout(self.horizontalLayoutFile)


        self.verticalLayout_2.addLayout(self.verticalLayoutPathing)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SequencePlayblastDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(SequencePlayblastDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_8.addWidget(self.label_9)

        self.select_shots_btn = QPushButton(SequencePlayblastDialog)
        self.select_shots_btn.setObjectName(u"select_shots_btn")

        self.horizontalLayout_8.addWidget(self.select_shots_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(SequencePlayblastDialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.resolution_select_cmb = QComboBox(SequencePlayblastDialog)
        self.resolution_select_cmb.setObjectName(u"resolution_select_cmb")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.resolution_select_cmb.sizePolicy().hasHeightForWidth())
        self.resolution_select_cmb.setSizePolicy(sizePolicy2)
        self.resolution_select_cmb.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.resolution_select_cmb)

        self.resolution_width_sb = QSpinBox(SequencePlayblastDialog)
        self.resolution_width_sb.setObjectName(u"resolution_width_sb")
        self.resolution_width_sb.setMinimumSize(QSize(80, 0))
        self.resolution_width_sb.setMaximumSize(QSize(100, 16777215))
        self.resolution_width_sb.setFrame(True)
        self.resolution_width_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.resolution_width_sb.setMinimum(1)
        self.resolution_width_sb.setMaximum(9999)

        self.horizontalLayout_3.addWidget(self.resolution_width_sb)

        self.label_7 = QLabel(SequencePlayblastDialog)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMaximumSize(QSize(16, 16777215))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.resolution_height_sb = QSpinBox(SequencePlayblastDialog)
        self.resolution_height_sb.setObjectName(u"resolution_height_sb")
        self.resolution_height_sb.setMinimumSize(QSize(80, 0))
        self.resolution_height_sb.setMaximumSize(QSize(100, 16777215))
        self.resolution_height_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.resolution_height_sb.setMinimum(1)
        self.resolution_height_sb.setMaximum(9999)

        self.horizontalLayout_3.addWidget(self.resolution_height_sb)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(SequencePlayblastDialog)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setMaximumSize(QSize(80, 16777215))
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.encoding_container_cmb = QComboBox(SequencePlayblastDialog)
        self.encoding_container_cmb.setObjectName(u"encoding_container_cmb")
        sizePolicy2.setHeightForWidth(self.encoding_container_cmb.sizePolicy().hasHeightForWidth())
        self.encoding_container_cmb.setSizePolicy(sizePolicy2)
        self.encoding_container_cmb.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.encoding_container_cmb)

        self.encoding_video_codec_cmb = QComboBox(SequencePlayblastDialog)
        self.encoding_video_codec_cmb.setObjectName(u"encoding_video_codec_cmb")
        sizePolicy2.setHeightForWidth(self.encoding_video_codec_cmb.sizePolicy().hasHeightForWidth())
        self.encoding_video_codec_cmb.setSizePolicy(sizePolicy2)
        self.encoding_video_codec_cmb.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.encoding_video_codec_cmb)

        self.encoding_video_codec_settings_btn = QPushButton(SequencePlayblastDialog)
        self.encoding_video_codec_settings_btn.setObjectName(u"encoding_video_codec_settings_btn")

        self.horizontalLayout_5.addWidget(self.encoding_video_codec_settings_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(SequencePlayblastDialog)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setMaximumSize(QSize(80, 16777215))
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.visibility_cmb = QComboBox(SequencePlayblastDialog)
        self.visibility_cmb.setObjectName(u"visibility_cmb")
        sizePolicy2.setHeightForWidth(self.visibility_cmb.sizePolicy().hasHeightForWidth())
        self.visibility_cmb.setSizePolicy(sizePolicy2)
        self.visibility_cmb.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_6.addWidget(self.visibility_cmb)

        self.visibility_customize_btn = QPushButton(SequencePlayblastDialog)
        self.visibility_customize_btn.setObjectName(u"visibility_customize_btn")
        self.visibility_customize_btn.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_6.addWidget(self.visibility_customize_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBoxEncodeAudio = QCheckBox(SequencePlayblastDialog)
        self.checkBoxEncodeAudio.setObjectName(u"checkBoxEncodeAudio")
        self.checkBoxEncodeAudio.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBoxEncodeAudio)

        self.ornaments_cb = QCheckBox(SequencePlayblastDialog)
        self.ornaments_cb.setObjectName(u"ornaments_cb")
        sizePolicy2.setHeightForWidth(self.ornaments_cb.sizePolicy().hasHeightForWidth())
        self.ornaments_cb.setSizePolicy(sizePolicy2)
        self.ornaments_cb.setMinimumSize(QSize(100, 0))
        self.ornaments_cb.setChecked(True)

        self.verticalLayout_4.addWidget(self.ornaments_cb)

        self.overscan_cb = QCheckBox(SequencePlayblastDialog)
        self.overscan_cb.setObjectName(u"overscan_cb")
        self.overscan_cb.setChecked(True)

        self.verticalLayout_4.addWidget(self.overscan_cb)

        self.viewer_cb = QCheckBox(SequencePlayblastDialog)
        self.viewer_cb.setObjectName(u"viewer_cb")
        sizePolicy2.setHeightForWidth(self.viewer_cb.sizePolicy().hasHeightForWidth())
        self.viewer_cb.setSizePolicy(sizePolicy2)
        self.viewer_cb.setMinimumSize(QSize(100, 0))
        self.viewer_cb.setChecked(True)

        self.verticalLayout_4.addWidget(self.viewer_cb)


        self.horizontalLayout_10.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBoxBurnCaption = QCheckBox(SequencePlayblastDialog)
        self.checkBoxBurnCaption.setObjectName(u"checkBoxBurnCaption")
        self.checkBoxBurnCaption.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBoxBurnCaption)

        self.checkBoxTimeCode = QCheckBox(SequencePlayblastDialog)
        self.checkBoxTimeCode.setObjectName(u"checkBoxTimeCode")
        self.checkBoxTimeCode.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBoxTimeCode)

        self.checkBoxFrameNumber = QCheckBox(SequencePlayblastDialog)
        self.checkBoxFrameNumber.setObjectName(u"checkBoxFrameNumber")
        self.checkBoxFrameNumber.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBoxFrameNumber)

        self.checkBoxArtistName = QCheckBox(SequencePlayblastDialog)
        self.checkBoxArtistName.setObjectName(u"checkBoxArtistName")
        self.checkBoxArtistName.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBoxArtistName)


        self.horizontalLayout_10.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.groupBox = QGroupBox(SequencePlayblastDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 75))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBoxBuildSequence = QCheckBox(self.groupBox)
        self.checkBoxBuildSequence.setObjectName(u"checkBoxBuildSequence")
        self.checkBoxBuildSequence.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBoxBuildSequence)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.output_edit = QPlainTextEdit(SequencePlayblastDialog)
        self.output_edit.setObjectName(u"output_edit")

        self.verticalLayout.addWidget(self.output_edit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.refresh_btn = QPushButton(SequencePlayblastDialog)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout.addWidget(self.refresh_btn)

        self.clear_btn = QPushButton(SequencePlayblastDialog)
        self.clear_btn.setObjectName(u"clear_btn")

        self.horizontalLayout.addWidget(self.clear_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.playblast_btn = QPushButton(SequencePlayblastDialog)
        self.playblast_btn.setObjectName(u"playblast_btn")

        self.horizontalLayout.addWidget(self.playblast_btn)

        self.close_btn = QPushButton(SequencePlayblastDialog)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(SequencePlayblastDialog)

        self.playblast_btn.setDefault(True)


        QMetaObject.connectSlotsByName(SequencePlayblastDialog)
    # setupUi

    def retranslateUi(self, SequencePlayblastDialog):
        SequencePlayblastDialog.setWindowTitle(fakestr(u"Playblaster", None))
        self.filename_label.setText(fakestr(u"Target Dir", None))
        self.output_filename_le.setText("")
        self.output_filename_le.setPlaceholderText(fakestr(u"{scene}", None))
#if QT_CONFIG(tooltip)
        self.output_dir_path_select_btn.setToolTip(fakestr(u"Select Output Directory", None))
#endif // QT_CONFIG(tooltip)
        self.output_dir_path_select_btn.setText(fakestr(u"...", None))
        self.force_overwrite_cb.setText(fakestr(u"Force overwrite", None))
#if QT_CONFIG(tooltip)
        self.output_dir_path_show_folder_btn.setToolTip(fakestr(u"Show in Folder", None))
#endif // QT_CONFIG(tooltip)
        self.output_dir_path_show_folder_btn.setText(fakestr(u"Go", None))
        self.label.setText(fakestr(u"Options", None))
        self.label_9.setText(fakestr(u"Shots", None))
        self.select_shots_btn.setText(fakestr(u"Select ...", None))
        self.label_3.setText(fakestr(u"Resolution:", None))
        self.label_7.setText(fakestr(u" x ", None))
        self.label_5.setText(fakestr(u"Encoding:", None))
        self.encoding_video_codec_settings_btn.setText(fakestr(u"Settings ...", None))
        self.label_6.setText(fakestr(u"Visibility:", None))
        self.visibility_customize_btn.setText(fakestr(u"Customise ...", None))
        self.checkBoxEncodeAudio.setText(fakestr(u"Encode Audio", None))
        self.ornaments_cb.setText(fakestr(u"Ornaments", None))
        self.overscan_cb.setText(fakestr(u"Overscan", None))
        self.viewer_cb.setText(fakestr(u"Show in Viewer", None))
        self.checkBoxBurnCaption.setText(fakestr(u"Burn caption", None))
        self.checkBoxTimeCode.setText(fakestr(u"Burn time code", None))
        self.checkBoxFrameNumber.setText(fakestr(u"Burn frame number", None))
        self.checkBoxArtistName.setText(fakestr(u"Burn Artist Name", None))
        self.groupBox.setTitle(fakestr(u"Sequence", None))
        self.checkBoxBuildSequence.setText(fakestr(u"Build Sequence from Shots", None))
        self.refresh_btn.setText(fakestr(u"Refresh", None))
        self.clear_btn.setText(fakestr(u"Clear", None))
        self.playblast_btn.setText(fakestr(u"Playblast", None))
        self.close_btn.setText(fakestr(u"Close", None))
    # retranslateUi

