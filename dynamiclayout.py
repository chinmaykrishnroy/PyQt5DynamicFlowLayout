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
