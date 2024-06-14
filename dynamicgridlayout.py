import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QScrollArea, QVBoxLayout
import random, webbrowser

class DynamicGridLayout(QGridLayout):
    def __init__(self, parent=None, min_col_width=360, min_row_height=116):
        super().__init__(parent)
        self.min_col_width = min_col_width
        self.min_row_height = min_row_height
        self.items = []
        self.num_cols = 0

    def addWidget(self, widget, rowSpan=1, colSpan=1, alignment=None):
        item = (widget, rowSpan, colSpan, alignment)
        self.items.append(item)
        super().addWidget(widget, 0, 0, rowSpan, colSpan)
        self.update_layout()

    def update_layout(self):
        if not self.parentWidget():
            return

        width = self.parentWidget().width()
        new_num_cols = max(1, width // self.min_col_width)
        item_width = width // new_num_cols

        if new_num_cols != self.num_cols:
            self.num_cols = new_num_cols

        row = col = 0
        for widget, rowSpan, colSpan, alignment in self.items:
            widget.setFixedHeight(item_width * self.min_row_height // self.min_col_width)
            super().addWidget(widget, row, col, rowSpan, colSpan)
            col += 1
            if col >= self.num_cols:
                col = 0
                row += 1

class ExampleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("* {\n"
        "    border: none;\n"
        "    padding: 0px;\n"
        "    margin: 0px;\n"
        "    background-color: transparent;\n"
        "    font-family: \"Segoe UI\";\n"
        "    font-size: 16px;\n"
        "}\n"
        "\n"
        "/*216869*/\n"
        "\n"
        "QPushButton {\n"
        "    color: white;  /*Off White Palette Color*/\n"
        "}\n"
        "\n"
        "QLabel {\n"
        "    color: white;  /*Off White Palette Color*/\n"
        "}\n"
        "\n"
        "#scroll_area {\n"
        "    background: white;\n"
        "}\n"
        "\n"
        "#videoContainer {\n"
        "    background: teal;\n"
        "}\n"
        "\n"
        "#videoThumbnailFrame {\n"
        "    background-color: red;\n"
        "}\n"
        "\n"
        "#viewsLabel {\n"
        "    font-size: 12px;\n"
        "    font-family: \"Roboto\", \"Arial\", \"sans-serif\";\n"
        "}\n"
        "\n"
        "#videoTitleLabel {\n"
        "    font-size: 14px;\n"
        "    font-family: \"Roboto\", \"Arial\", \"sans-serif\";\n"
        "    padding-left: 1px;\n"
        "}\n"
        "\n"
        "#videoDurationLabel {\n"
        "    font-size: 12px;\n"
        "    font-family: \"Roboto\", \"Arial\", \"sans-serif\";\n"
        "    padding: 2px 4px;\n"
        "    background : rgba(0,0,0, 0.5);\n"
        "    border-radius: 4px;\n"
        "    margin-bottom: 4px;\n"
        "    \n"
        "}\n"
        "\n"
        "#channelNameLabel {\n"
        "    font-size: 12px;\n"
        "    font-family: \"Roboto\", \"Arial\", \"sans-serif\";\n"
        "}\n"
        "\n"
        "#videoThumbnailBtn:hover {\n"
        "    background-color: #111111; \n"
        "}\n"
        "\n"
        "#videoThumbnailBtn:pressed {\n"
        "    background-color: #222222;\n"
        "}")
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.content_widget = QWidget()
        self.grid_layout = DynamicGridLayout(self.content_widget)
        self.grid_layout.setSpacing(4)
        self.content_widget.setLayout(self.grid_layout)

        self.scroll_area.setWidget(self.content_widget)

        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll_area)
        self.setLayout(layout)


        info = {
            "title": "FlowLayout PyQt Example",
            "url": "https://www.example.com/",
            "duration": "98:98",
            "channel": "Chinmay K Roy",
            "views": "700B views • 5 seconds ago"
        }
        video_info_list = []
        video_info_list.append(info)
        for _ in range(random.randint(50, 200)):
            random_element = {
                "title": f"Video {_}",
                "url": f"https://www.example.com/{_}",
                "duration": f"{random.randint(1, 120)}:{random.randint(0, 59)}",
                "channel": f"Channel {_}",
                "views": f"{random.randint(1, 1000)} views • {random.randint(2, 60)} years ago"
            }
            video_info_list.append(random_element)
        self.addVideo(video_info_list)

    def addVideo(self, video_info_list):
        for video_info in video_info_list:
            self.videoContainer = QtWidgets.QFrame()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.videoContainer.sizePolicy().hasHeightForWidth())
            self.videoContainer.setSizePolicy(sizePolicy)
            self.videoContainer.setMinimumSize(QtCore.QSize(0, 116))
            self.videoContainer.setMaximumSize(QtCore.QSize(16777215, 234))
            self.videoContainer.setStyleSheet("")
            self.videoContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.videoContainer.setFrameShadow(QtWidgets.QFrame.Raised)
            self.videoContainer.setObjectName("videoContainer")
            self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.videoContainer)
            self.horizontalLayout_12.setContentsMargins(2, 2, 2, 2)
            self.horizontalLayout_12.setSpacing(2)
            self.horizontalLayout_12.setObjectName("horizontalLayout_12")
            self.videoThumbnailFrame = QtWidgets.QFrame(self.videoContainer)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.videoThumbnailFrame.sizePolicy().hasHeightForWidth())
            self.videoThumbnailFrame.setSizePolicy(sizePolicy)
            self.videoThumbnailFrame.setMinimumSize(QtCore.QSize(168, 94))
            self.videoThumbnailFrame.setMaximumSize(QtCore.QSize(360, 270))
            self.videoThumbnailFrame.setStyleSheet("")
            self.videoThumbnailFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.videoThumbnailFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.videoThumbnailFrame.setObjectName("videoThumbnailFrame")
            self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.videoThumbnailFrame)
            self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_14.setSpacing(0)
            self.verticalLayout_14.setObjectName("verticalLayout_14")
            self.videoThumbnailBtn = QtWidgets.QPushButton(self.videoThumbnailFrame)
            self.videoThumbnailBtn.setMinimumSize(QtCore.QSize(164, 98))
            self.videoThumbnailBtn.setMaximumSize(QtCore.QSize(360, 270))
            self.videoThumbnailBtn.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("youtube.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.videoThumbnailBtn.setIcon(icon)
            self.videoThumbnailBtn.setIconSize(QtCore.QSize(168, 94))
            self.videoThumbnailBtn.setObjectName("videoThumbnailBtn")
            self.verticalLayout_14.addWidget(self.videoThumbnailBtn)
            self.horizontalLayout_12.addWidget(self.videoThumbnailFrame)
            self.videoInfoFrame = QtWidgets.QFrame(self.videoContainer)
            self.videoInfoFrame.setMinimumSize(QtCore.QSize(164, 94))
            self.videoInfoFrame.setMaximumSize(QtCore.QSize(16777215, 270))
            self.videoInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.videoInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.videoInfoFrame.setObjectName("videoInfoFrame")
            self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.videoInfoFrame)
            self.verticalLayout_13.setContentsMargins(10, 10, 0, 0)
            self.verticalLayout_13.setSpacing(0)
            self.verticalLayout_13.setObjectName("verticalLayout_13")
            self.videoTitleLabel = QtWidgets.QLabel(self.videoInfoFrame)
            self.videoTitleLabel.setWordWrap(True)
            self.videoTitleLabel.setObjectName("videoTitleLabel")
            self.verticalLayout_13.addWidget(self.videoTitleLabel)
            self.channelFrame = QtWidgets.QFrame(self.videoInfoFrame)
            self.channelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.channelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.channelFrame.setObjectName("channelFrame")
            self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.channelFrame)
            self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_21.setSpacing(8)
            self.horizontalLayout_21.setObjectName("horizontalLayout_21")
            self.channelIconBtn = QtWidgets.QPushButton(self.channelFrame)
            self.channelIconBtn.setMinimumSize(QtCore.QSize(12, 12))
            self.channelIconBtn.setMaximumSize(QtCore.QSize(32, 32))
            self.channelIconBtn.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("chrome.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.channelIconBtn.setIcon(icon1)
            self.channelIconBtn.setObjectName("channelIconBtn")
            self.horizontalLayout_21.addWidget(self.channelIconBtn, 0, QtCore.Qt.AlignHCenter)
            self.channelNameLabel = QtWidgets.QLabel(self.channelFrame)
            self.channelNameLabel.setWordWrap(True)
            self.channelNameLabel.setObjectName("channelNameLabel")
            self.horizontalLayout_21.addWidget(self.channelNameLabel)
            self.verticalLayout_13.addWidget(self.channelFrame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.viewsAgeFrame = QtWidgets.QFrame(self.videoInfoFrame)
            self.viewsAgeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.viewsAgeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.viewsAgeFrame.setObjectName("viewsAgeFrame")
            self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.viewsAgeFrame)
            self.horizontalLayout_22.setContentsMargins(4, 2, 0, 4)
            self.horizontalLayout_22.setSpacing(0)
            self.horizontalLayout_22.setObjectName("horizontalLayout_22")
            self.viewsLabel = QtWidgets.QLabel(self.viewsAgeFrame)
            self.viewsLabel.setWordWrap(True)
            self.viewsLabel.setObjectName("viewsLabel")
            self.horizontalLayout_22.addWidget(self.viewsLabel)
            self.verticalLayout_13.addWidget(self.viewsAgeFrame, 0, QtCore.Qt.AlignTop)
            self.downloadRedirectFrame = QtWidgets.QFrame(self.videoInfoFrame)
            self.downloadRedirectFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.downloadRedirectFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.downloadRedirectFrame.setObjectName("downloadRedirectFrame")
            self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.downloadRedirectFrame)
            self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_23.setSpacing(0)
            self.horizontalLayout_23.setObjectName("horizontalLayout_23")
            self.videoDurationLabel = QtWidgets.QLabel(self.downloadRedirectFrame)
            self.videoDurationLabel.setObjectName("videoDurationLabel")
            self.horizontalLayout_23.addWidget(self.videoDurationLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_23.addItem(spacerItem)
            self.verticalLayout_13.addWidget(self.downloadRedirectFrame)
            self.verticalLayout_13.setStretch(1, 2)
            self.verticalLayout_13.setStretch(2, 2)
            self.horizontalLayout_12.addWidget(self.videoInfoFrame)
            self.horizontalLayout_12.setStretch(0, 3)
            self.horizontalLayout_12.setStretch(1, 4)
            self.grid_layout.addWidget(self.videoContainer)
            self.videoThumbnailBtn.clicked.connect(self.openurl)
            _translate = QtCore.QCoreApplication.translate
            self.videoTitleLabel.setText(_translate("MainWindow", video_info["title"]))
            self.channelNameLabel.setText(_translate("MainWindow", video_info["channel"]))
            self.viewsLabel.setText(_translate("MainWindow", video_info["views"]))
            self.videoDurationLabel.setText(_translate("MainWindow", video_info["duration"])) 

    def openurl(self): webbrowser.open_new_tab("https://github.com/chinmaykrishnroy/PyQt5DynamicFlowLayout")

    def showEvent(self, event):
        super().showEvent(event)
        self.grid_layout.update_layout()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.grid_layout.update_layout()

app = QApplication(sys.argv)
window = ExampleWidget()
window.setWindowTitle('Dynamic Grid Layout Example')
window.resize(800, 600)
window.show()
sys.exit(app.exec_())
