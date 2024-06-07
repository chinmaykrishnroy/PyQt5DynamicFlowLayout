from PyQt5.QtWidgets import QLayout, QSizePolicy, QWidget, QApplication
from PyQt5.QtCore import QRect, QSize, QPoint, Qt

class AutoGridLayout(QLayout):
    def __init__(self, parent=None, spacing=0):
        super().__init__(parent)
        self.setSpacing(spacing)
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def count(self):
        return len(self.items)

    def itemAt(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

    def takeAt(self, index):
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Horizontal | Qt.Vertical)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self._calculateSize(width).height()

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self._doLayout(rect)

    def sizeHint(self):
        return self.minimumSize()
    
    def minimumSize(self):
        size = QSize()
        for item in self.items:
            size = size.expandedTo(item.minimumSize())
        margins = self.contentsMargins()
        size += QSize(margins.left() + margins.right(), margins.top() + margins.bottom())
        return size

    def _calculateSize(self, width):
        height = 0
        row_height = 0
        column_width = 0
        columns = 0

        for item in self.items:
            if columns == 0:
                column_width = item.sizeHint().width()

            if column_width + item.sizeHint().width() > width:
                height += row_height
                row_height = item.sizeHint().height()
                columns = 1
                column_width = item.sizeHint().width()
            else:
                row_height = max(row_height, item.sizeHint().height())
                column_width += item.sizeHint().width()
                columns += 1

        height += row_height
        return QSize(width, height)

    def _doLayout(self, rect):
        if not self.items:
            return

        x = rect.x()
        y = rect.y()
        row_height = 0
        column_width = 0

        for item in self.items:
            widget = item.widget()
            next_x = x + item.sizeHint().width()

            if next_x > rect.right() and row_height > 0:
                x = rect.x()
                y += row_height
                next_x = x + item.sizeHint().width()
                row_height = 0

            item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = next_x
            row_height = max(row_height, item.sizeHint().height())

        y += row_height

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QPushButton

    app = QApplication(sys.argv)

    mainWidget = QWidget()
    layout = AutoGridLayout()

    for i in range(10):
        button = QPushButton(f"Button {i}")
        button.setStyleSheet("""
            background-color: red; color: white; padding: 8px; border-radius: 4px; border: 1px; margin: 4px 4px 4px 4px; padding: 2px 4px; font-size:16px
            """)
        layout.addWidget(button)

    mainWidget.setLayout(layout)
    mainWidget.show()

    sys.exit(app.exec_())
