from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint, QRect, QSize, Qt
from PyQt5.QtWidgets import QLayout

class FlowLayout(QLayout):
    def __init__(self, parent=None, orientation=Qt.Horizontal, margin=4, spacing=4):
        super().__init__(parent)
        self.orientation = orientation
        self.spacing = spacing
        self.margin = margin
        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return self.orientation == Qt.Horizontal

    def heightForWidth(self, width):
        return self.doLayout(QRect(0, 0, width, 0), True)

    def hasWidthForHeight(self):
        return self.orientation == Qt.Vertical

    def widthForHeight(self, height):
        return self.doLayout(QRect(0, 0, 0, height), True)

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        size += QSize(2 * self.margin, 2 * self.margin)
        return size

    def doLayout(self, rect, testOnly):
        margin_left, margin_top, margin_right, margin_bottom = self.margin, self.margin, self.margin, self.margin
        x = rect.x() + margin_left
        y = rect.y() + margin_top
        lineHeight = 0
        items_in_line = []
        total_width = 0
        spacing = self.spacing

        for item in self.itemList:
            item_width = item.sizeHint().width()
            item_height = item.sizeHint().height()
            aspect_ratio = item_width / item_height
            nextX = x + item_width + spacing
            if self.orientation == Qt.Horizontal:
                if nextX > rect.right() - margin_right + 1 and lineHeight > 0:
                    extra_space = rect.width() - total_width + spacing * (len(items_in_line) - 1)
                    if items_in_line and extra_space > 0:
                        extra_space_per_item = extra_space / len(items_in_line)
                        new_x = rect.x() + margin_left
                        for line_item in items_in_line:
                            line_item_width = line_item.sizeHint().width() + extra_space_per_item
                            line_item_height = line_item_width / aspect_ratio
                            if not testOnly:
                                line_item.setGeometry(QRect(QPoint(int(new_x), int(line_item.y)), QSize(int(line_item_width), int(line_item_height))))
                            new_x += line_item_width + spacing
                        x = rect.x() + margin_left
                        y += lineHeight + spacing
                        nextX = x + item_width + spacing
                        lineHeight = 0
                        items_in_line = []
                        total_width = 0
                items_in_line.append(item)
                item.x, item.y = x, y
                total_width += item_width + spacing
                if not testOnly:
                    current_width = (rect.width() - (len(items_in_line) - 1) * spacing - margin_left - margin_right) / len(items_in_line)
                    item_height = current_width / aspect_ratio
                    item.setGeometry(QRect(QPoint(int(x), int(y)), QSize(int(current_width), int(item_height))))
                x = nextX
                lineHeight = item_height
            else:
                pass
        if self.orientation == Qt.Horizontal and items_in_line:
            extra_space = rect.width() - total_width + spacing * (len(items_in_line) - 1)
            if items_in_line and extra_space > 0:
                extra_space_per_item = extra_space / len(items_in_line)
                new_x = rect.x() + margin_left
                for line_item in items_in_line:
                    line_item_width = line_item.sizeHint().width() + extra_space_per_item
                    line_item_height = line_item_width / aspect_ratio
                    if not testOnly:
                        line_item.setGeometry(QRect(QPoint(int(new_x), int(line_item.y)), QSize(int(line_item_width), int(line_item_height))))
                    new_x += line_item_width + spacing

        if self.orientation == Qt.Horizontal:
            return y + lineHeight + margin_bottom - rect.y()
        else:
            pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 574)
        MainWindow.setStyleSheet("* {\n"
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
"#mainAppBody {\n"
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
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainBodyContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet("")
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.mainAppBody = QtWidgets.QWidget(self.mainBodyContainer)
        self.mainAppBody.setStyleSheet("")
        self.mainAppBody.setObjectName("mainAppBody")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.mainAppBody)
        self.verticalLayout_10.setContentsMargins(0, 0, 10, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.mainAppStack = QtWidgets.QStackedWidget(self.mainAppBody)
        self.mainAppStack.setObjectName("mainAppStack")
        self.searchStack = QtWidgets.QWidget()
        self.searchStack.setObjectName("searchStack")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.searchStack)
        self.verticalLayout_11.setContentsMargins(2, 0, 2, 2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.searchResultFrame = QtWidgets.QFrame(self.searchStack)
        self.searchResultFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchResultFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchResultFrame.setObjectName("searchResultFrame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.searchResultFrame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 6, 4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.scrollArea = QtWidgets.QScrollArea(self.searchResultFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 568))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.videoSpaceFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoSpaceFrame.sizePolicy().hasHeightForWidth())
        self.videoSpaceFrame.setSizePolicy(sizePolicy)
        self.videoSpaceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.videoSpaceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoSpaceFrame.setObjectName("videoSpaceFrame")

        self.flowLayout = FlowLayout(self.videoSpaceFrame)
        self.flowLayout.setContentsMargins(4, 8, 4, 4)
        self.flowLayout.setSpacing(1)
        self.flowLayout.setObjectName("flowLayout")

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_11.addWidget(self.videoSpaceFrame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_10.addWidget(self.scrollArea)
        self.verticalLayout_11.addWidget(self.searchResultFrame)
        self.mainAppStack.addWidget(self.searchStack)
        self.verticalLayout_10.addWidget(self.mainAppStack)
        self.verticalLayout_9.addWidget(self.mainAppBody)
        self.horizontalLayout.addWidget(self.mainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        info = {
            "title": "FlowLayout PyQt Example",
            "url": "https://www.example.com/",
            "duration": "98:98",
            "channel": "Chinmay K Roy",
            "views": "700B views • 5 seconds ago"
        }
        video_info_list = []
        video_info_list.append(info)
        import random, webbrowser
        for _ in range(random.randint(8, 50)):
            random_element = {
                "title": f"Video {_}",
                "url": f"https://www.example.com/{_}",
                "duration": f"{random.randint(1, 120)}:{random.randint(0, 59)}",
                "channel": f"Channel {_}",
                "views": f"{random.randint(1, 1000)} views • {random.randint(2, 60)} years ago"
            }
            video_info_list.append(random_element)

        self.addVideoContainer(video_info_list)
        self.retranslateUi(MainWindow)
        self.videoThumbnailBtn.clicked.connect(self.openurl)
        self.mainAppStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def openurl(self): webbrowser.open_new_tab("https://github.com/chinmaykrishnroy/PyQt5DynamicFlowLayout")

    def addVideoContainer(self, video_info_list):
        for video_info in video_info_list:
            self.videoContainer = QtWidgets.QFrame(self.videoSpaceFrame)
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
            self.videoThumbnailBtn.clicked.connect(self.openurl)
            self.flowLayout.addWidget(self.videoContainer)
            _translate = QtCore.QCoreApplication.translate
            self.videoTitleLabel.setText(_translate("MainWindow", video_info["title"]))
            self.channelNameLabel.setText(_translate("MainWindow", video_info["channel"]))
            self.viewsLabel.setText(_translate("MainWindow", video_info["views"]))
            self.videoDurationLabel.setText(_translate("MainWindow", video_info["duration"]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dynamic Resizable Custom Flow Layout Example"))
        MainWindow.setToolTip(_translate("MainWindow", "visit https://github.com/chinmaykrishnroy for more content"))
        self.videoThumbnailBtn.setToolTip(_translate("MainWindow", "go to the video"))


if __name__ == "__main__":
    import sys, webbrowser
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
