__author__ = 'Geosson'
from PySide import QtGui
from PySide import QtCore
from Ui_MainWindow import Ui_Wheel

from example_tx_II_with_geosson_gui import example_tx_II_with_geosson_gui


class Wheel(QtGui.QWidget, Ui_Wheel):

    def __init__(self, parent):
        super(Wheel, self).__init__(parent)
        self.setupUi(self)
        self.up = 16777235
        self.down = 16777237
        self.left = 16777234
        self.right = 16777236
        self.keys = [self.up, self.left, self.right, self.down]
        self.command = []
        self.setupSignal()

        self.tb = example_tx_II_with_geosson_gui()
        self.tb.remotecar_RemoteCarIIBaseBand_0.set_run(False)
        print "start"
        self.tb.start()

    def setupSignal(self):
        self.button_temp = [self.upB, self.leftB, self.rightB, self.downB]
        for i in self.button_temp:
            i.pressed.connect(self.buttonPressEvent)
            i.released.connect(self.buttonReleased)

    def buttonPressEvent(self):
        key = self.keys[self.button_temp.index(self.sender())]
        if key not in self.command:
            self.command.append(key)
        self.sendInstruction(self.command)

    def buttonReleased(self):
        self.command = []
        self.sendInstruction(self.command)

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return
        key = event.key()
        if key not in self.command:
            self.command.append(key)
        self.sendInstruction(self.command)

    def keyReleaseEvent(self, event):
        if not event.isAutoRepeat():
            self.command = []
            self.sendInstruction(self.command)

    def sendInstruction(self, command):
        if len(command) == 0: 
            self.tb.remotecar_RemoteCarIIBaseBand_0.set_run(False)
            self.display_label.setText(u'stop')
            self.upB.setStyleSheet('')
            self.leftB.setStyleSheet('')
            self.rightB.setStyleSheet('')
            self.downB.setStyleSheet('')
            return
        if len(command) == 1:
            self.tb.remotecar_RemoteCarIIBaseBand_0.set_run(True)
            if self.up in command:
                self.display_label.setText('1 step up')
                self.upB.setStyleSheet("QPushButton{background-color:red}")
                self.tb.remotecar_RemoteCarIIBaseBand_0.set_command(10)
            elif self.left in command:
                self.display_label.setText('turn left')
                self.leftB.setStyleSheet("QPushButton{background-color:red}")
                self.tb.remotecar_RemoteCarIIBaseBand_0.set_command(58)
            elif self.right in command:
                self.display_label.setText('turn right')
                self.rightB.setStyleSheet("QPushButton{background-color:red}")
                self.tb.remotecar_RemoteCarIIBaseBand_0.set_command(64)
            elif self.down in command:
                self.display_label.setText('turn down')
                self.downB.setStyleSheet("QPushButton{background-color:red}")
                self.tb.remotecar_RemoteCarIIBaseBand_0.set_command(40)
            return
        if len(command) == 2:
            self.tb.remotecar_RemoteCarIIBaseBand_0.set_run(True)
            if self.up in command and self.left in command:
                self.display_label.setText('turn left-up')
                self.upB.setStyleSheet("QPushButton{background-color:red}")
                self.leftB.setStyleSheet("QPushButton{background-color:red}")
                self.tb.remotecar_RemoteCarIIBaseBand_0.set_command(28)
            elif self.up in command and self.right in command:
                self.display_label.setText('turn right-up')
                self.upB.setStyleSheet("QPushButton{background-color:red}")
                self.rightB.setStyleSheet("QPushButton{background-color:red}")
                self.tb.remotecar_RemoteCarIIBaseBand_0.set_command(34)
            elif self.down in command and self.left in command:
                self.display_label.setText('turn left-down')
                self.downB.setStyleSheet("QPushButton{background-color:red}")
                self.leftB.setStyleSheet("QPushButton{background-color:red}")
                self.tb.remotecar_RemoteCarIIBaseBand_0.set_command(52)
            elif self.down in command and self.right in command:
                self.display_label.setText('turn right-down')
                self.downB.setStyleSheet("QPushButton{background-color:red}")
                self.rightB.setStyleSheet("QPushButton{background-color:red}")
                self.tb.remotecar_RemoteCarIIBaseBand_0.set_command(46)
            return

    def closeEvent(self, event):
        print 'clean up'
        self.tb.stop()
        self.tb.wait()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    main = Wheel(None)
    main.show()
    sys.exit( app.exec_() )

