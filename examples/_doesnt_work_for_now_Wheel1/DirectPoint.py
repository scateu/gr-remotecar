__author__ = 'Geosson'
from PySide import QtGui
from PySide import QtCore


class DirectPoint(QtGui.QGraphicsItem):

    BoundingRect = QtCore.QRectF(-5, -5, 10, 10)

    def __init__(self):
        super(DirectPoint, self).__init__()
        self.color = QtGui.QColor(QtCore.Qt.red)

    def boundingRect(self):
        return DirectPoint.BoundingRect

    def shape(self):
        path = QtGui.QPainterPath()
        path.addEllipse(self.boundingRect())
        return path

    def paint(self, painter, option, widget):
        painter.setBrush(self.color)
        painter.drawEllipse(-5, -5, 10, 10)

