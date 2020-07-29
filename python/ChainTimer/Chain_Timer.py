#!python2

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon

class Timer(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle("Chain Timer")


        self.resize(300, 230)
        self.i = 0
        self.stMusic = 0
        self.fade = 1
        self.cycleCount = 0
        self.allCycleCount = 0
        self.linksCount = 0
        self.targetCount = 0
        self.remainedCount = 0
        self.proJobCount = 0

        self.button = QtGui.QPushButton('Start', self)
        self.button2 = QtGui.QPushButton('Set', self)
        self.lcd = QtGui.QLCDNumber(self)
        self.edit = QtGui.QLineEdit("25", self)

        self.allLinks = QtGui.QLabel('Done: ', self)
        self.allLinksEdit = QtGui.QLineEdit('0', self)
        self.allLinksEdit.setReadOnly(True)
        self.ostLinks = QtGui.QLabel('Remained: ', self)
        self.ostLinksEdit = QtGui.QLineEdit('0', self)
        self.ostLinksEdit.setReadOnly(True)
        self.purpLinks = QtGui.QLabel('Target: ', self)
        self.purpLinksEdit = QtGui.QLineEdit('0', self)
        self.reset = QtGui.QPushButton('Reset', self)

        self.alll = QtGui.QLabel('All cycles: ', self)
        self.alllEdit = QtGui.QLineEdit('0', self)
        self.alllEdit.setReadOnly(True)
        self.proJobLabel = QtGui.QLabel('Projobano', self)
        self.proJobEdit = QtGui.QLineEdit('00:00:00', self)
        # self.proJobEdit.setReadOnly(True)
        self.space = QtGui.QLabel("                        ", self)

        self.lcd.setDigitCount(8)
        self.button.setShortcut("Ctrl+P")

        projobLayout = QtGui.QGridLayout()
        projobLayout.addWidget(self.alll, 0, 0)
        projobLayout.addWidget(self.alllEdit, 0, 1)
        projobLayout.addWidget(self.proJobLabel, 0, 2)
        projobLayout.addWidget(self.proJobEdit, 0, 3)

        alignLayout = QtGui.QGridLayout()
        alignLayout.addLayout(projobLayout, 0, 0)
        alignLayout.addWidget(self.space, 0, 1)

        resetLayout = QtGui.QGridLayout()
        resetLayout.setSpacing(5)
        resetLayout.addWidget(self.allLinks, 1, 0)
        resetLayout.addWidget(self.allLinksEdit,  1, 1)
        resetLayout.addWidget(self.ostLinks,  1, 2)
        resetLayout.addWidget(self.ostLinksEdit, 1, 3)
        resetLayout.addWidget(self.purpLinks,  1, 4)
        resetLayout.addWidget(self.purpLinksEdit,  1, 5)
        resetLayout.addWidget(self.reset,  1, 6, 1, 10)
        # resetLayout.addWidget(self.alll,  2, 0)
        # resetLayout.addWidget(self.alllEdit,  2, 1)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button2)

        mainlayout = QtGui.QVBoxLayout()
        mainlayout.addWidget(self.lcd)
        mainlayout.addLayout(layout)
        mainlayout.addWidget(self.button)
        mainlayout.addLayout(resetLayout)
        mainlayout.addLayout(alignLayout)

        self.setLayout(mainlayout)

        self.myTimer = QtCore.QTimer(self)
        self.myTimer.timeout.connect(self.countDown)

        self.myTimer2 = QtCore.QTimer(self)
        self.myTimer2.timeout.connect(self.stopMusic)

        self.myTimer3 = QtCore.QTimer(self)
        self.myTimer3.timeout.connect(self.fadeOut)

        self.myTimer4 = QtCore.QTimer(self)
        self.myTimer4.timeout.connect(self.allTime)

        self.myTimer5 = QtCore.QTimer(self)
        self.myTimer5.timeout.connect(self.proJob)
        self.myTimer5.start(1000)

        self.edit.returnPressed.connect(self.button2.click)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.pushed)
        self.connect(self.button2, QtCore.SIGNAL('clicked()'), self.settt)
        self.connect(self.reset, QtCore.SIGNAL('clicked()'), self.resetAll)

        self.output = Phonon.AudioOutput(Phonon.MusicCategory)
        self.m_media = Phonon.MediaObject()
        Phonon.createPath(self.m_media, self.output)
        self.m_media.setCurrentSource(Phonon.MediaSource("music/MyMusic.mp3"))

    def pushed(self):
        self.i += 1
        ok = self.i%2
        if ok:
            self.button.setText('Stop')
            self.startTimer()
            self.myTimer5.stop()
            self.myTimer4.start(1000)
            print "pushed Start"
        if not ok:
            self.button.setText('Start')
            self.myTimer.stop()
            self.myTimer4.stop()
            self.myTimer5.start(1000)
            self.m_media.stop()
            print "pushed Stop"

    def settt(self):
        self.fade = 1
        self.number = float(self.edit.text())
        if self.number < 1 and self.number >= 0.01:
            self.number = int(self.number*100)
        elif self.number >= 1:
            self.number = int(self.number*60)
        else:
            self.edit.setText("Wrong Value")

        hours = self.number/60/60
        minets = self.number/60 - hours*60
        sec = self.number%60

        if hours < 1:
            hours = "00"
        elif hours < 10:
            hours = "0"+str(hours)

        if minets < 1:
            minets = "00"
        elif minets < 10:
            minets = "0"+str(minets)

        if sec < 1:
            sec = "00"
        elif sec < 10:
            sec = "0"+str(sec)

        nrStr = str(hours)+':'+str(minets)+':'+str(sec)

        self.lcd.display(nrStr)

    def countDown(self):
        hours = self.number/60/60
        minets = self.number/60 - hours*60
        sec = self.number%60
        # print hours
        # print minets
        # print sec
        # print "--------"

        if hours < 1:
            hours = "00"
        elif hours < 10:
            hours = "0"+str(hours)
        # print "add zero to hours"
        # print hours
        # print minets
        # print sec
        # print "--------"

        if minets < 1:
            minets = "00"
        elif minets < 10:
            minets = "0"+str(minets)
        # print "add zero to minets"
        # print hours
        # print minets
        # print sec
        # print "--------"

        if sec < 1:
            sec = "00"
        elif sec < 10:
            sec = "0"+str(sec)
        # print "add zero to sec"
        # print hours
        # print minets
        # print sec
        # print "--------"

        time = str(hours)+':'+str(minets)+':'+str(sec)
        self.lcd.display(time)
        if self.number <= 0:
            self.myTimer.stop()
            self.m_media.play()
            self.output.setVolume(1)
            self.stopMusic()
            self.myTimer2.start(1000)
            self.stMusic = 0
        self.number -= 1

    def startTimer(self):
        self.number -= 1
        self.myTimer.start(1000)
        # print 'ok'

    def stopMusic(self):
        self.stMusic += 1
        if self.stMusic == 5:
            self.myTimer2.stop()
            self.myTimer3.start(100)
            # print "start Timer3"

    def fadeOut(self):
        self.output.setVolume(self.fade)
        if self.fade <= 0:
            self.m_media.stop()
            self.myTimer3.stop()
            # print 'Stop music'
        self.fade -= 0.1
        # print self.fade

    def allTime(self):
        self.targetCount = int(self.purpLinksEdit.text())
        self.cycleCount += 1
        isLink = self.cycleCount % 1500
        if isLink == 0:
            self.linksCount += 1
            self.allCycleCount += 1
            strLinksCount = str(self.linksCount)
            self.allLinksEdit.setText(strLinksCount)
        if self.targetCount > 0:
            self.remainedCount = self.targetCount - self.linksCount
            if  self.remainedCount >= 0:
                strRemainedCount = str(self.remainedCount)
                self.ostLinksEdit.setText(strRemainedCount)
            else:
                self.ostLinksEdit.setText("0")

    def resetAll(self):
        self.allLinksEdit.setText("0")
        self.ostLinksEdit.setText("0")
        self.purpLinksEdit.setText("0")
        self.cycleCount = 0
        self.linksCount = 0
        self.targetCount = 0
        self.remainedCount = 0
        # print "pushed"

    def proJob(self):
        toStr = str(self.allCycleCount)
        self.alllEdit.setText(toStr)
        self.proJobCount += 1
        hours = self.proJobCount/60/60
        minets = self.proJobCount/60 - hours*60
        sec = self.proJobCount%60

        if hours < 1:
            hours = "00"
        elif hours < 10:
            hours = "0"+str(hours)

        if minets < 1:
            minets = "00"
        elif minets < 10:
            minets = "0"+str(minets)

        if sec < 1:
            sec = "00"
        elif sec < 10:
            sec = "0"+str(sec)

        time = str(hours)+':'+str(minets)+':'+str(sec)
        self.proJobEdit.setText(time)

app = QtGui.QApplication(sys.argv)
# app.setStyle('cleeanlooks')
timer = Timer()
timer.show()
app.exec_()

