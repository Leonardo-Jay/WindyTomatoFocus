# -*- coding: utf-8 -*-


from PyQt5.QtCore import QCoreApplication,QMetaObject,QRect,Qt,QSize
from PyQt5.QtGui import QFont,QBrush,QColor,QCursor
from PyQt5.QtWidgets import QFrame,QLabel,QListWidget,QSizePolicy,QListWidgetItem,QListView,QCheckBox
from PyQt5.QtWidgets import QAbstractItemView,QAbstractScrollArea,QRadioButton,QToolButton
from qfluentwidgets import ComboBox
from qfluentwidgets import PushButton
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import TimePicker

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(405, 234)
        self.frame = QFrame(Dialog)
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(409, 235)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 421, 235))
        font = QFont()
        font.setFamily(u"\u7b49\u7ebf")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 40, 281, 51))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(16)
        self.label_4.setFont(font1)
        self.ComboBox = ComboBox(self.frame)
        self.ComboBox.setObjectName(u"ComboBox")
        self.ComboBox.setGeometry(QRect(130, 106, 151, 40))
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.ComboBox.setFont(font2)
        self.ComboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.ComboBox.setMouseTracking(False)
        self.ComboBox.setLayoutDirection(Qt.LeftToRight)
        self.ComboBox.setAutoFillBackground(False)
        self.ComboBox.setText(u"6\u5c0f\u65f6")
        self.ComboBox.setCheckable(False)
        self.ComboBox.setChecked(False)
        self.ComboBox.setAutoRepeat(False)
        self.ComboBox.setAutoExclusive(False)
        self.ComboBox.setAutoDefault(True)
        self.ComboBox.setFlat(False)
        self.PrimaryPushButton = PrimaryPushButton(self.frame)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        self.PrimaryPushButton.setGeometry(QRect(100, 180, 91, 32))
        self.PrimaryPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.PrimaryPushButton.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"PushButton[isPlaceholderText=true] {\n"
"    color: rgba(0, 0, 0, 0.6063);\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"DropDownToolButton, PrimaryDropDownToolButton {\n"
"    padding: 5px 31px 6px 8px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=false],\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5p"
                        "x 31px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover, ToolButton:hover, ToggleButton:hover, ToggleToolButton:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: #51c4d3;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleBu"
                        "tton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: #00a7b3;\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"

"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
""
                        "    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitToolButton:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"")
        self.PushButton = PushButton(self.frame)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setGeometry(QRect(220, 179, 93, 34))
        self.PushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.PushButton.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"PushButton[isPlaceholderText=true] {\n"
"    color: rgba(0, 0, 0, 0.6063);\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"

"PushButton:hover, ToolButton:hover, ToggleButton:hover, ToggleToolButton:hover {\n"
"	background-color: rgb(226, 226, 226);\n"
"}\n"
"\n"
"PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.1);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"")
        self.frame2 = QFrame(Dialog)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setGeometry(QRect(-10, 230, 431, 241))
        self.frame2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 30, 351, 51))
        self.label_5.setFont(font1)
        self.TimePicker = TimePicker(self.frame2)
        self.TimePicker.setObjectName(u"TimePicker")
        self.TimePicker.setGeometry(QRect(90, 110, 240, 30))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.TimePicker.setFont(font3)
        self.TimePicker.setCursor(QCursor(Qt.PointingHandCursor))
        self.PrimaryPushButton_2 = PrimaryPushButton(self.frame2)
        self.PrimaryPushButton_2.setObjectName(u"PrimaryPushButton_2")
        self.PrimaryPushButton_2.setGeometry(QRect(90, 180, 91, 32))
        self.PrimaryPushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.PrimaryPushButton_2.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"PushButton[isPlaceholderText=true] {\n"
"    color: rgba(0, 0, 0, 0.6063);\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5p"
                        "x 31px 6px 36px;\n"
"}\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: #51c4d3;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleBu"
                        "tton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: #00a7b3;\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled {\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
"    border: 1px solid rgb(205, 205, 205);\n"
"}\n"
"\n"
"SplitDropButton,\n"
"PrimarySplitDropButton {\n"
"    border-left: none;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton,\n"
"#splitToolButton,\n"
"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
""
                        "    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitToolButton:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"")
        self.PushButton_2 = PushButton(self.frame2)
        self.PushButton_2.setObjectName(u"PushButton_2")
        self.PushButton_2.setGeometry(QRect(240, 180, 93, 34))
        self.PushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.PushButton_2.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"PushButton[isPlaceholderText=true] {\n"
"    color: rgba(0, 0, 0, 0.6063);\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover, ToolButton:hover, ToggleButton:hover, ToggleToolButton:hover {\n"
"	background-color: rgb(226, 226, 226);\n"
"}\n"
"\n"
"PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.1);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"

"")

        self.retranslateUi(Dialog)
        self.PrimaryPushButton.clicked.connect(Dialog.savesettime)
        self.PrimaryPushButton_2.clicked.connect(Dialog.saveaddtime)
        self.PushButton.clicked.connect(Dialog.notsavesettime)
        self.PushButton_2.clicked.connect(Dialog.notaddtime)

        self.ComboBox.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u8bbe\u7f6e\u60a8\u4eca\u65e5\u4e13\u6ce8\u7684\u76ee\u6807\u65f6\u95f4", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.PushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u8bbe\u7f6e\u60a8\u5e0c\u671b\u624b\u52a8\u6dfb\u52a0\u7684\u5df2\u4e13\u6ce8\u65f6\u95f4", None))
        self.PrimaryPushButton_2.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.PushButton_2.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi



class settingDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(616, 244)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 0, 1041, 661))
        self.frame.setStyleSheet(u"background-color: #EBEBEB")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, -20, 131, 261))
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.listWidget = QListWidget(self.frame_6)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setForeground(brush);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 50, 121, 181))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(15)
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius:0px; \n"
"padding: 2px; \n"
"")
        self.listWidget.setFrameShape(QFrame.StyledPanel)
        self.listWidget.setLineWidth(1)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setProperty("showDropIndicator", True)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(2)
        self.listWidget.setGridSize(QSize(55, 54))
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setBatchSize(100)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setSortingEnabled(False)
        self.line = QFrame(self.frame_6)
        self.line.setObjectName(u"line")
        self.line.setWindowModality(Qt.ApplicationModal)
        self.line.setGeometry(QRect(120, 36, 1, 211))
        self.line.setStyleSheet(u"background-color: rgb(194, 194, 194);\n"
"color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(4)
        self.line.setFrameShape(QFrame.VLine)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(140, 0, 511, 241))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:0px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 141, 31))
        self.label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.duihao2 = QCheckBox(self.frame_3)
        self.duihao2.setObjectName(u"duihao2")
        self.duihao2.setGeometry(QRect(40, 120, 251, 31))
        self.duihao2.setCursor(QCursor(Qt.PointingHandCursor))
        self.duihao2.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.duihao3 = QCheckBox(self.frame_3)
        self.duihao3.setObjectName(u"duihao3")
        self.duihao3.setGeometry(QRect(40, 180, 141, 31))
        self.duihao3.setCursor(QCursor(Qt.PointingHandCursor))
        self.duihao3.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.duihao3.setTristate(False)
        self.radioButton = QRadioButton(self.frame_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(90, 80, 151, 31))
        self.radioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.radioButton2 = QRadioButton(self.frame_3)
        self.radioButton2.setObjectName(u"radioButton2")
        self.radioButton2.setGeometry(QRect(90, 50, 151, 31))
        self.radioButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton2.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 260, 511, 241))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:0px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.duihao4 = QCheckBox(self.frame_4)
        self.duihao4.setObjectName(u"duihao4")
        self.duihao4.setGeometry(QRect(90, 140, 131, 31))
        self.duihao4.setCursor(QCursor(Qt.PointingHandCursor))
        self.duihao4.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.duihao4.setTristate(False)
        self.chongzhidata = PushButton(self.frame_4)
        self.chongzhidata.setObjectName(u"chongzhidata")
        self.chongzhidata.setGeometry(QRect(70, 60, 191, 32))
        self.chongzhidata.setBaseSize(QSize(0, 0))
        self.chongzhidata.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 20, 141, 31))
        self.label_2.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 100, 141, 31))
        self.label_3.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.duihao4_2 = QCheckBox(self.frame_4)
        self.duihao4_2.setObjectName(u"duihao4_2")
        self.duihao4_2.setGeometry(QRect(90, 170, 131, 31))
        self.duihao4_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.duihao4_2.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.duihao4_2.setTristate(False)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(530, 260, 511, 241))
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:0px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 20, 181, 31))
        font1 = QFont()
        font1.setFamily(u"\u7b49\u7ebf")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 60, 161, 21))
        font2 = QFont()
        font2.setFamily(u"\u5b8b\u4f53")
        font2.setPointSize(12)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(68, 68, 68);")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 120, 161, 21))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(68, 68, 68);")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 150, 211, 21))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(68, 68, 68);")
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 90, 181, 21))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: rgb(68, 68, 68);")
        self.toolButton = QToolButton(self.frame_5)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(60, 180, 101, 31))
        self.toolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton.setContextMenuPolicy(Qt.PreventContextMenu)
        self.toolButton.setStyleSheet(u"\n"
"QToolButton { \n"
"		border: none; \n"
"		font: 12pt \"\u5b8b\u4f53\";\n"
"		text-decoration: underline;\n"
"        background-color: #FFFFFF;\n"
"        color: black;\n"
"}  \n"
"QToolButton:hover {\n"
"		color:#51c4d3;\n"
"} ")
        self.toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setArrowType(Qt.NoArrow)
        self.toolButton2 = QToolButton(self.frame_5)
        self.toolButton2.setObjectName(u"toolButton2")
        self.toolButton2.setGeometry(QRect(190, 180, 101, 31))
        self.toolButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton2.setContextMenuPolicy(Qt.PreventContextMenu)
        self.toolButton2.setStyleSheet(u"\n"
"QToolButton { \n"
"		border: none; \n"
"		font: 12pt \"\u5b8b\u4f53\";\n"
"		text-decoration: underline;\n"
"        background-color: #FFFFFF;\n"
"        color: black;\n"
"}  \n"
"QToolButton:hover {\n"
"		color:#51c4d3;\n"
"} ")
        self.toolButton2.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.toolButton2.setAutoRaise(True)
        self.toolButton2.setArrowType(Qt.NoArrow)
        self.frame_6.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_3.raise_()

        self.retranslateUi(Dialog)

        self.listWidget.setCurrentRow(0)
        self.toolButton.clicked.connect(Dialog.openvisionnote)
        self.toolButton2.clicked.connect(Dialog.opencopyright)
        self.duihao2.clicked.connect(Dialog.startup)
        self.chongzhidata.clicked.connect(Dialog.deteledatabiao)
        self.radioButton2.clicked.connect(Dialog.searchquit)
        self.radioButton.clicked.connect(Dialog.searchquit)
        self.duihao4.clicked.connect(Dialog.setwarmming)
        self.duihao4_2.clicked.connect(Dialog.setsinging)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"\u57fa\u7840\u8bbe\u7f6e", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u8ba1\u65f6\u8bbe\u7f6e", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"  \u5173\u4e8e  ", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("Dialog", u"\u5173\u95ed\u4e3b\u754c\u9762\uff1a", None))
#if QT_CONFIG(statustip)
        self.duihao2.setStatusTip(QCoreApplication.translate("Dialog", u"\u9009\u5b9a\u540e\u5173\u95ed\u5c06\u4e0d\u5728\u9000\u51fa\u8f6f\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.duihao2.setText(QCoreApplication.translate("Dialog", u"\u8f6f\u4ef6\u5f00\u673a\u81ea\u542f\u52a8", None))
        self.duihao3.setText(QCoreApplication.translate("Dialog", u"\u81ea\u52a8\u68c0\u67e5\u66f4\u65b0", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\u6700\u5c0f\u5316\u5230\u7cfb\u7edf\u6258\u76d8", None))
        self.radioButton2.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa\u7a0b\u5e8f", None))
#if QT_CONFIG(statustip)
        self.duihao4.setStatusTip(QCoreApplication.translate("Dialog", u"\u9009\u5b9a\u540e\u5173\u95ed\u5c06\u4e0d\u5728\u9000\u51fa\u8f6f\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.duihao4.setText(QCoreApplication.translate("Dialog", u"\u5f39\u7a97\u6d88\u606f\u63d0\u9192", None))
        self.chongzhidata.setText(QCoreApplication.translate("Dialog", u"\u91cd\u7f6e\u6240\u6709\u8bb0\u5f55\u6570\u636e", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u91cd\u65b0\u8bb0\u5f55\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5012\u8ba1\u65f6\u7ed3\u675f\u540e\uff1a", None))
#if QT_CONFIG(statustip)
        self.duihao4_2.setStatusTip(QCoreApplication.translate("Dialog", u"\u9009\u5b9a\u540e\u5173\u95ed\u5c06\u4e0d\u5728\u9000\u51fa\u8f6f\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.duihao4_2.setText(QCoreApplication.translate("Dialog", u"\u94c3\u58f0\u63d0\u9192", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5173\u4e8e\u98ce\u4e2d\u756a\u8304\u4e13\u6ce8", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u5f53\u524d\u7248\u672c\uff1a0.6.1", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u4f5c\u8005\uff1aLeonardoJay", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"联系：GitHub @Leonardo-Jay", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u66f4\u65b0\u65f6\u95f4\uff1a2024.10.14", None))
        self.toolButton.setText(QCoreApplication.translate("Dialog", u"\u300a\u7248\u672c\u65e5\u5fd7\u300b", None))
        self.toolButton2.setText(QCoreApplication.translate("Dialog", u"\u300a\u7248\u6743\u58f0\u660e\u300b", None))
    # retranslateUi

