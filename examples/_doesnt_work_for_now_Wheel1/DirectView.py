__author__ = 'Geosson'
from PySide import QtGui
from PySide import QtCore
from DirectPoint import DirectPoint


class DirectView(QtGui.QGraphicsView):
    def __init__(self, parent):
        super(DirectView, self).__init__(parent)
        self.left_right = 50
        self.top_bottom = 50
        self.scene_left = -100
        self.scene_right = -100
        self.scene = QtGui.QGraphicsScene(self)
        self.scene.setSceneRect(-100, -100, 200, 200)
        self.point = DirectPoint()
        self.point.setPos(0, 0)
        self.scene.addItem(self.point)
        self.setScene(self.scene)
        self.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.green))
        self.setViewportUpdateMode(QtGui.QGraphicsView.BoundingRectViewportUpdate)

    def resizeEvent(self, event):
        self.scene_left = -self.viewport().width() / 2
        self.scene_right = -self.viewport().height() / 2
        self.scene.setSceneRect(self.scene_left, self.scene_right, self.viewport().width(), self.viewport().height())

    def setPosition(self, lr, tb):
        self.left_right = int(lr * 100 / self.viewport().width())
        self.top_bottom = int(tb * 100 / self.viewport().height())
        self.point.setPos(lr + self.scene_left, tb + self.scene_right)
        self.result()

    def mousePressEvent(self, event):
        self.setPosition(event.x(), event.y())

    def mouseReleaseEvent(self, event):
        self.setPosition(self.viewport().width() / 2, self.viewport().height() / 2)

    def mouseMoveEvent(self, event):
        self.setPosition(event.x(), event.y())

    def result(self):
        print "left-right:", self.left_right, "top-bottom", self.top_bottom


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = DirectView(None)
    window.show()
    print window.width(), window.height()
    sys.exit(app.exec_())


