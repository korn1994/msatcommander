# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/msatcommander.ui'
#
# Created: Mon Mar 15 22:41:07 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_msatcommander(object):
    def setupUi(self, msatcommander):
        msatcommander.setObjectName("msatcommander")
        msatcommander.resize(522, 546)
        self.tabWidget = QtGui.QTabWidget(msatcommander)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 501, 491))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 221, 248))
        self.groupBox.setObjectName("groupBox")
        self.dinucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.dinucCheckBox.setGeometry(QtCore.QRect(10, 46, 115, 31))
        self.dinucCheckBox.setObjectName("dinucCheckBox")
        self.pentanucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.pentanucCheckBox.setGeometry(QtCore.QRect(10, 121, 120, 31))
        self.pentanucCheckBox.setObjectName("pentanucCheckBox")
        self.trinucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.trinucCheckBox.setGeometry(QtCore.QRect(10, 71, 120, 31))
        self.trinucCheckBox.setObjectName("trinucCheckBox")
        self.hexanucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.hexanucCheckBox.setGeometry(QtCore.QRect(10, 146, 120, 31))
        self.hexanucCheckBox.setObjectName("hexanucCheckBox")
        self.tetranucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.tetranucCheckBox.setGeometry(QtCore.QRect(10, 96, 120, 31))
        self.tetranucCheckBox.setObjectName("tetranucCheckBox")
        self.combineLociCheckBox = QtGui.QCheckBox(self.groupBox)
        self.combineLociCheckBox.setGeometry(QtCore.QRect(10, 215, 131, 31))
        self.combineLociCheckBox.setObjectName("combineLociCheckBox")
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(10, 180, 201, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.perfectRepeatsCheckBox = QtGui.QCheckBox(self.groupBox)
        self.perfectRepeatsCheckBox.setGeometry(QtCore.QRect(10, 190, 131, 31))
        self.perfectRepeatsCheckBox.setObjectName("perfectRepeatsCheckBox")
        self.mononucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.mononucCheckBox.setGeometry(QtCore.QRect(10, 21, 121, 31))
        self.mononucCheckBox.setObjectName("mononucCheckBox")
        self.mononucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.mononucSpinBox.setGeometry(QtCore.QRect(150, 25, 51, 25))
        self.mononucSpinBox.setMaximum(100)
        self.mononucSpinBox.setProperty("value", 10)
        self.mononucSpinBox.setObjectName("mononucSpinBox")
        self.dinucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.dinucSpinBox.setGeometry(QtCore.QRect(150, 50, 51, 25))
        self.dinucSpinBox.setMaximum(100)
        self.dinucSpinBox.setProperty("value", 8)
        self.dinucSpinBox.setObjectName("dinucSpinBox")
        self.trinucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.trinucSpinBox.setGeometry(QtCore.QRect(150, 75, 51, 25))
        self.trinucSpinBox.setMaximum(100)
        self.trinucSpinBox.setProperty("value", 8)
        self.trinucSpinBox.setObjectName("trinucSpinBox")
        self.tetranucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.tetranucSpinBox.setGeometry(QtCore.QRect(150, 100, 51, 25))
        self.tetranucSpinBox.setMaximum(100)
        self.tetranucSpinBox.setProperty("value", 6)
        self.tetranucSpinBox.setObjectName("tetranucSpinBox")
        self.pentanucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.pentanucSpinBox.setGeometry(QtCore.QRect(150, 125, 51, 25))
        self.pentanucSpinBox.setMaximum(100)
        self.pentanucSpinBox.setProperty("value", 6)
        self.pentanucSpinBox.setObjectName("pentanucSpinBox")
        self.hexanucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.hexanucSpinBox.setGeometry(QtCore.QRect(150, 150, 51, 25))
        self.hexanucSpinBox.setMaximum(100)
        self.hexanucSpinBox.setProperty("value", 6)
        self.hexanucSpinBox.setObjectName("hexanucSpinBox")
        self.combineLociDistanceSpinBox = QtGui.QSpinBox(self.groupBox)
        self.combineLociDistanceSpinBox.setGeometry(QtCore.QRect(150, 217, 51, 25))
        self.combineLociDistanceSpinBox.setMaximum(5000)
        self.combineLociDistanceSpinBox.setProperty("value", 50)
        self.combineLociDistanceSpinBox.setObjectName("combineLociDistanceSpinBox")
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 250, 221, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.designPrimersCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.designPrimersCheckBox.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.designPrimersCheckBox.setObjectName("designPrimersCheckBox")
        self.tagPrimersCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.tagPrimersCheckBox.setGeometry(QtCore.QRect(10, 50, 151, 21))
        self.tagPrimersCheckBox.setObjectName("tagPrimersCheckBox")
        self.pigtailPrimersCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.pigtailPrimersCheckBox.setGeometry(QtCore.QRect(10, 150, 171, 21))
        self.pigtailPrimersCheckBox.setObjectName("pigtailPrimersCheckBox")
        self.cagTagCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.cagTagCheckBox.setGeometry(QtCore.QRect(30, 70, 151, 21))
        self.cagTagCheckBox.setChecked(False)
        self.cagTagCheckBox.setObjectName("cagTagCheckBox")
        self.m13rCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.m13rCheckBox.setGeometry(QtCore.QRect(30, 90, 151, 21))
        self.m13rCheckBox.setChecked(False)
        self.m13rCheckBox.setObjectName("m13rCheckBox")
        self.customTagCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.customTagCheckBox.setGeometry(QtCore.QRect(30, 110, 151, 21))
        self.customTagCheckBox.setObjectName("customTagCheckBox")
        self.customTagLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.customTagLineEdit.setGeometry(QtCore.QRect(50, 130, 160, 22))
        self.customTagLineEdit.setAutoFillBackground(False)
        self.customTagLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.customTagLineEdit.setObjectName("customTagLineEdit")
        self.pigtailPrimersTagLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.pigtailPrimersTagLineEdit.setGeometry(QtCore.QRect(30, 170, 160, 22))
        self.pigtailPrimersTagLineEdit.setAutoFillBackground(False)
        self.pigtailPrimersTagLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pigtailPrimersTagLineEdit.setObjectName("pigtailPrimersTagLineEdit")
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(265, 0, 220, 81))
        self.groupBox_4.setObjectName("groupBox_4")
        self.commaSeparatedRadioButton = QtGui.QRadioButton(self.groupBox_4)
        self.commaSeparatedRadioButton.setGeometry(QtCore.QRect(20, 30, 151, 21))
        self.commaSeparatedRadioButton.setChecked(True)
        self.commaSeparatedRadioButton.setObjectName("commaSeparatedRadioButton")
        self.tabDelimitedRadioButton = QtGui.QRadioButton(self.groupBox_4)
        self.tabDelimitedRadioButton.setGeometry(QtCore.QRect(20, 50, 151, 21))
        self.tabDelimitedRadioButton.setObjectName("tabDelimitedRadioButton")
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(265, 80, 220, 112))
        self.groupBox_3.setObjectName("groupBox_3")
        self.taggedPrimersCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.taggedPrimersCheckBox.setGeometry(QtCore.QRect(20, 80, 161, 31))
        self.taggedPrimersCheckBox.setObjectName("taggedPrimersCheckBox")
        self.combinedRepeatsCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.combinedRepeatsCheckBox.setGeometry(QtCore.QRect(20, 40, 161, 31))
        self.combinedRepeatsCheckBox.setObjectName("combinedRepeatsCheckBox")
        self.primersCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.primersCheckBox.setGeometry(QtCore.QRect(20, 60, 161, 31))
        self.primersCheckBox.setObjectName("primersCheckBox")
        self.repeatsCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.repeatsCheckBox.setGeometry(QtCore.QRect(20, 20, 161, 31))
        self.repeatsCheckBox.setObjectName("repeatsCheckBox")
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_8.setGeometry(QtCore.QRect(0, 110, 161, 80))
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_9 = QtGui.QGroupBox(self.tab)
        self.groupBox_9.setGeometry(QtCore.QRect(265, 190, 220, 65))
        self.groupBox_9.setObjectName("groupBox_9")
        self.keepDatabaseCheckBox = QtGui.QCheckBox(self.groupBox_9)
        self.keepDatabaseCheckBox.setGeometry(QtCore.QRect(20, 22, 151, 21))
        self.keepDatabaseCheckBox.setObjectName("keepDatabaseCheckBox")
        self.keepDbaseSequenceRecords = QtGui.QCheckBox(self.groupBox_9)
        self.keepDbaseSequenceRecords.setGeometry(QtCore.QRect(40, 40, 171, 21))
        self.keepDbaseSequenceRecords.setObjectName("keepDbaseSequenceRecords")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_5 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 80, 190, 105))
        self.groupBox_5.setObjectName("groupBox_5")
        self.primerMinSizeSpinBox = QtGui.QSpinBox(self.groupBox_5)
        self.primerMinSizeSpinBox.setGeometry(QtCore.QRect(120, 22, 58, 25))
        self.primerMinSizeSpinBox.setMinimum(15)
        self.primerMinSizeSpinBox.setMaximum(30)
        self.primerMinSizeSpinBox.setProperty("value", 18)
        self.primerMinSizeSpinBox.setObjectName("primerMinSizeSpinBox")
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(10, 24, 111, 20))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 111, 20))
        self.label_7.setObjectName("label_7")
        self.primerOptSizeSpinBox = QtGui.QSpinBox(self.groupBox_5)
        self.primerOptSizeSpinBox.setGeometry(QtCore.QRect(120, 48, 58, 25))
        self.primerOptSizeSpinBox.setMinimum(15)
        self.primerOptSizeSpinBox.setMaximum(30)
        self.primerOptSizeSpinBox.setProperty("value", 20)
        self.primerOptSizeSpinBox.setObjectName("primerOptSizeSpinBox")
        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 76, 111, 20))
        self.label_8.setObjectName("label_8")
        self.primerMaxSizeSpinBox = QtGui.QSpinBox(self.groupBox_5)
        self.primerMaxSizeSpinBox.setGeometry(QtCore.QRect(120, 74, 58, 25))
        self.primerMaxSizeSpinBox.setMinimum(15)
        self.primerMaxSizeSpinBox.setMaximum(30)
        self.primerMaxSizeSpinBox.setProperty("value", 22)
        self.primerMaxSizeSpinBox.setObjectName("primerMaxSizeSpinBox")
        self.groupBox_6 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 0, 481, 81))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_5 = QtGui.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(10, 38, 111, 20))
        self.label_5.setObjectName("label_5")
        self.primerProductSizeTextBox = QtGui.QLineEdit(self.groupBox_6)
        self.primerProductSizeTextBox.setGeometry(QtCore.QRect(100, 40, 371, 22))
        self.primerProductSizeTextBox.setObjectName("primerProductSizeTextBox")
        self.label = QtGui.QLabel(self.groupBox_6)
        self.label.setGeometry(QtCore.QRect(100, 63, 371, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_7 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 190, 190, 105))
        self.groupBox_7.setObjectName("groupBox_7")
        self.primerMinTmSpinBox = QtGui.QSpinBox(self.groupBox_7)
        self.primerMinTmSpinBox.setGeometry(QtCore.QRect(120, 22, 58, 25))
        self.primerMinTmSpinBox.setMinimum(45)
        self.primerMinTmSpinBox.setMaximum(150)
        self.primerMinTmSpinBox.setProperty("value", 58)
        self.primerMinTmSpinBox.setObjectName("primerMinTmSpinBox")
        self.label_6 = QtGui.QLabel(self.groupBox_7)
        self.label_6.setGeometry(QtCore.QRect(10, 24, 111, 20))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtGui.QLabel(self.groupBox_7)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 111, 20))
        self.label_9.setObjectName("label_9")
        self.primerOptTmSpinBox = QtGui.QSpinBox(self.groupBox_7)
        self.primerOptTmSpinBox.setGeometry(QtCore.QRect(120, 48, 58, 25))
        self.primerOptTmSpinBox.setMinimum(45)
        self.primerOptTmSpinBox.setMaximum(150)
        self.primerOptTmSpinBox.setProperty("value", 60)
        self.primerOptTmSpinBox.setObjectName("primerOptTmSpinBox")
        self.label_10 = QtGui.QLabel(self.groupBox_7)
        self.label_10.setGeometry(QtCore.QRect(10, 76, 111, 20))
        self.label_10.setObjectName("label_10")
        self.primerMaxTmSpinBox = QtGui.QSpinBox(self.groupBox_7)
        self.primerMaxTmSpinBox.setGeometry(QtCore.QRect(120, 74, 58, 25))
        self.primerMaxTmSpinBox.setMinimum(45)
        self.primerMaxTmSpinBox.setMaximum(150)
        self.primerMaxTmSpinBox.setProperty("value", 62)
        self.primerMaxTmSpinBox.setObjectName("primerMaxTmSpinBox")
        self.groupBox_10 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_10.setGeometry(QtCore.QRect(30, 300, 190, 78))
        self.groupBox_10.setObjectName("groupBox_10")
        self.primerMinGcSpinBox = QtGui.QSpinBox(self.groupBox_10)
        self.primerMinGcSpinBox.setGeometry(QtCore.QRect(120, 21, 58, 25))
        self.primerMinGcSpinBox.setMaximum(50)
        self.primerMinGcSpinBox.setProperty("value", 30)
        self.primerMinGcSpinBox.setObjectName("primerMinGcSpinBox")
        self.label_2 = QtGui.QLabel(self.groupBox_10)
        self.label_2.setGeometry(QtCore.QRect(10, 24, 110, 20))
        self.label_2.setObjectName("label_2")
        self.primerMaxGcSpinBox = QtGui.QSpinBox(self.groupBox_10)
        self.primerMaxGcSpinBox.setGeometry(QtCore.QRect(120, 47, 58, 25))
        self.primerMaxGcSpinBox.setMinimum(50)
        self.primerMaxGcSpinBox.setMaximum(100)
        self.primerMaxGcSpinBox.setProperty("value", 70)
        self.primerMaxGcSpinBox.setObjectName("primerMaxGcSpinBox")
        self.label_3 = QtGui.QLabel(self.groupBox_10)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 110, 20))
        self.label_3.setObjectName("label_3")
        self.groupBox_11 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_11.setGeometry(QtCore.QRect(30, 380, 190, 55))
        self.groupBox_11.setObjectName("groupBox_11")
        self.primerMaxPolyXSpinBox = QtGui.QSpinBox(self.groupBox_11)
        self.primerMaxPolyXSpinBox.setGeometry(QtCore.QRect(120, 23, 58, 25))
        self.primerMaxPolyXSpinBox.setMaximum(6)
        self.primerMaxPolyXSpinBox.setProperty("value", 3)
        self.primerMaxPolyXSpinBox.setObjectName("primerMaxPolyXSpinBox")
        self.label_11 = QtGui.QLabel(self.groupBox_11)
        self.label_11.setGeometry(QtCore.QRect(10, 27, 101, 16))
        self.label_11.setObjectName("label_11")
        self.groupBox_12 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_12.setGeometry(QtCore.QRect(270, 80, 201, 181))
        self.groupBox_12.setObjectName("groupBox_12")
        self.primerMaxSelfAnySpinBox = QtGui.QSpinBox(self.groupBox_12)
        self.primerMaxSelfAnySpinBox.setGeometry(QtCore.QRect(130, 22, 58, 25))
        self.primerMaxSelfAnySpinBox.setMaximum(100)
        self.primerMaxSelfAnySpinBox.setProperty("value", 45)
        self.primerMaxSelfAnySpinBox.setObjectName("primerMaxSelfAnySpinBox")
        self.label_12 = QtGui.QLabel(self.groupBox_12)
        self.label_12.setGeometry(QtCore.QRect(10, 24, 121, 20))
        self.label_12.setObjectName("label_12")
        self.primerMaxSelfEndSpinBox = QtGui.QSpinBox(self.groupBox_12)
        self.primerMaxSelfEndSpinBox.setGeometry(QtCore.QRect(130, 48, 58, 25))
        self.primerMaxSelfEndSpinBox.setMaximum(100)
        self.primerMaxSelfEndSpinBox.setProperty("value", 40)
        self.primerMaxSelfEndSpinBox.setObjectName("primerMaxSelfEndSpinBox")
        self.label_13 = QtGui.QLabel(self.groupBox_12)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 121, 20))
        self.label_13.setObjectName("label_13")
        self.primerMaxPairAnySpinBox = QtGui.QSpinBox(self.groupBox_12)
        self.primerMaxPairAnySpinBox.setGeometry(QtCore.QRect(130, 100, 58, 25))
        self.primerMaxPairAnySpinBox.setMaximum(100)
        self.primerMaxPairAnySpinBox.setProperty("value", 45)
        self.primerMaxPairAnySpinBox.setObjectName("primerMaxPairAnySpinBox")
        self.label_14 = QtGui.QLabel(self.groupBox_12)
        self.label_14.setGeometry(QtCore.QRect(10, 102, 121, 20))
        self.label_14.setObjectName("label_14")
        self.primerMaxPairEndSpinBox = QtGui.QSpinBox(self.groupBox_12)
        self.primerMaxPairEndSpinBox.setGeometry(QtCore.QRect(130, 126, 58, 25))
        self.primerMaxPairEndSpinBox.setMaximum(100)
        self.primerMaxPairEndSpinBox.setProperty("value", 40)
        self.primerMaxPairEndSpinBox.setObjectName("primerMaxPairEndSpinBox")
        self.label_15 = QtGui.QLabel(self.groupBox_12)
        self.label_15.setGeometry(QtCore.QRect(10, 128, 121, 20))
        self.label_15.setObjectName("label_15")
        self.primerMaxSelfHairpinSpinBox = QtGui.QSpinBox(self.groupBox_12)
        self.primerMaxSelfHairpinSpinBox.setGeometry(QtCore.QRect(130, 74, 58, 25))
        self.primerMaxSelfHairpinSpinBox.setMaximum(100)
        self.primerMaxSelfHairpinSpinBox.setProperty("value", 24)
        self.primerMaxSelfHairpinSpinBox.setObjectName("primerMaxSelfHairpinSpinBox")
        self.label_16 = QtGui.QLabel(self.groupBox_12)
        self.label_16.setGeometry(QtCore.QRect(10, 76, 121, 20))
        self.label_16.setObjectName("label_16")
        self.primerMaxPairHairpinSpinBox = QtGui.QSpinBox(self.groupBox_12)
        self.primerMaxPairHairpinSpinBox.setGeometry(QtCore.QRect(130, 152, 58, 25))
        self.primerMaxPairHairpinSpinBox.setProperty("value", 24)
        self.primerMaxPairHairpinSpinBox.setObjectName("primerMaxPairHairpinSpinBox")
        self.label_17 = QtGui.QLabel(self.groupBox_12)
        self.label_17.setGeometry(QtCore.QRect(10, 154, 121, 20))
        self.label_17.setObjectName("label_17")
        self.groupBox_13 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_13.setGeometry(QtCore.QRect(270, 260, 201, 74))
        self.groupBox_13.setObjectName("groupBox_13")
        self.primerGCClampCheckBox = QtGui.QCheckBox(self.groupBox_13)
        self.primerGCClampCheckBox.setGeometry(QtCore.QRect(10, 50, 87, 20))
        self.primerGCClampCheckBox.setChecked(True)
        self.primerGCClampCheckBox.setObjectName("primerGCClampCheckBox")
        self.label_18 = QtGui.QLabel(self.groupBox_13)
        self.label_18.setGeometry(QtCore.QRect(10, 24, 120, 20))
        self.label_18.setObjectName("label_18")
        self.primerMaxEndStabilitySpinBox = QtGui.QSpinBox(self.groupBox_13)
        self.primerMaxEndStabilitySpinBox.setGeometry(QtCore.QRect(130, 22, 58, 25))
        self.primerMaxEndStabilitySpinBox.setMaximum(20)
        self.primerMaxEndStabilitySpinBox.setProperty("value", 8)
        self.primerMaxEndStabilitySpinBox.setObjectName("primerMaxEndStabilitySpinBox")
        self.tabWidget.addTab(self.tab_3, "")
        self.runButton = QtGui.QPushButton(msatcommander)
        self.runButton.setGeometry(QtCore.QRect(290, 510, 115, 32))
        self.runButton.setObjectName("runButton")
        self.cancelButton = QtGui.QPushButton(msatcommander)
        self.cancelButton.setGeometry(QtCore.QRect(400, 510, 115, 32))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(msatcommander)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), msatcommander.close)
        QtCore.QObject.connect(self.runButton, QtCore.SIGNAL("clicked()"), msatcommander.accept)
        QtCore.QObject.connect(self.primersCheckBox, QtCore.SIGNAL("clicked()"), msatcommander.checkPrimersOutput)
        QtCore.QObject.connect(self.taggedPrimersCheckBox, QtCore.SIGNAL("clicked()"), msatcommander.checkTaggedPrimersOutput)
        QtCore.QObject.connect(self.combinedRepeatsCheckBox, QtCore.SIGNAL("clicked()"), msatcommander.checkCombineRepeatsOutput)
        QtCore.QObject.connect(self.repeatsCheckBox, QtCore.SIGNAL("clicked()"), msatcommander.checkRepeatsOutput)
        QtCore.QObject.connect(self.designPrimersCheckBox, QtCore.SIGNAL("clicked(bool)"), msatcommander.clickDesignPrimersCheckBox)
        QtCore.QObject.connect(self.mononucCheckBox, QtCore.SIGNAL("clicked(bool)"), msatcommander.clickRepeatsCheckBox)
        QtCore.QObject.connect(self.tagPrimersCheckBox, QtCore.SIGNAL("clicked(bool)"), msatcommander.clickTagPrimersCheckBox)
        QtCore.QObject.connect(self.dinucCheckBox, QtCore.SIGNAL("clicked(bool)"), msatcommander.clickRepeatsCheckBox)
        QtCore.QObject.connect(self.trinucCheckBox, QtCore.SIGNAL("clicked(bool)"), msatcommander.clickRepeatsCheckBox)
        QtCore.QObject.connect(self.tetranucCheckBox, QtCore.SIGNAL("clicked(bool)"), msatcommander.clickRepeatsCheckBox)
        QtCore.QObject.connect(self.pentanucCheckBox, QtCore.SIGNAL("clicked(bool)"), msatcommander.clickRepeatsCheckBox)
        QtCore.QObject.connect(self.hexanucCheckBox, QtCore.SIGNAL("clicked(bool)"), msatcommander.clickRepeatsCheckBox)
        QtCore.QObject.connect(self.combineLociCheckBox, QtCore.SIGNAL("clicked(bool)"), msatcommander.clickCombineLociCheckBox)
        QtCore.QObject.connect(self.keepDbaseSequenceRecords, QtCore.SIGNAL("clicked(bool)"), msatcommander.checkKeepDatabaseCheckBox)
        QtCore.QObject.connect(self.keepDatabaseCheckBox, QtCore.SIGNAL("clicked(bool)"), msatcommander.clickKeepDatabaseCheckBox)
        QtCore.QMetaObject.connectSlotsByName(msatcommander)
        msatcommander.setTabOrder(self.mononucCheckBox, self.mononucSpinBox)
        msatcommander.setTabOrder(self.mononucSpinBox, self.dinucCheckBox)
        msatcommander.setTabOrder(self.dinucCheckBox, self.dinucSpinBox)
        msatcommander.setTabOrder(self.dinucSpinBox, self.trinucCheckBox)
        msatcommander.setTabOrder(self.trinucCheckBox, self.trinucSpinBox)
        msatcommander.setTabOrder(self.trinucSpinBox, self.tetranucCheckBox)
        msatcommander.setTabOrder(self.tetranucCheckBox, self.tetranucSpinBox)
        msatcommander.setTabOrder(self.tetranucSpinBox, self.pentanucCheckBox)
        msatcommander.setTabOrder(self.pentanucCheckBox, self.pentanucSpinBox)
        msatcommander.setTabOrder(self.pentanucSpinBox, self.hexanucCheckBox)
        msatcommander.setTabOrder(self.hexanucCheckBox, self.combineLociCheckBox)
        msatcommander.setTabOrder(self.combineLociCheckBox, self.tagPrimersCheckBox)
        msatcommander.setTabOrder(self.tagPrimersCheckBox, self.designPrimersCheckBox)
        msatcommander.setTabOrder(self.designPrimersCheckBox, self.pigtailPrimersCheckBox)
        msatcommander.setTabOrder(self.pigtailPrimersCheckBox, self.cagTagCheckBox)
        msatcommander.setTabOrder(self.cagTagCheckBox, self.m13rCheckBox)
        msatcommander.setTabOrder(self.m13rCheckBox, self.cancelButton)
        msatcommander.setTabOrder(self.cancelButton, self.customTagLineEdit)
        msatcommander.setTabOrder(self.customTagLineEdit, self.repeatsCheckBox)
        msatcommander.setTabOrder(self.repeatsCheckBox, self.combinedRepeatsCheckBox)
        msatcommander.setTabOrder(self.combinedRepeatsCheckBox, self.primersCheckBox)
        msatcommander.setTabOrder(self.primersCheckBox, self.taggedPrimersCheckBox)
        msatcommander.setTabOrder(self.taggedPrimersCheckBox, self.commaSeparatedRadioButton)
        msatcommander.setTabOrder(self.commaSeparatedRadioButton, self.tabDelimitedRadioButton)
        msatcommander.setTabOrder(self.tabDelimitedRadioButton, self.primerMinSizeSpinBox)
        msatcommander.setTabOrder(self.primerMinSizeSpinBox, self.primerOptSizeSpinBox)
        msatcommander.setTabOrder(self.primerOptSizeSpinBox, self.primerMaxSizeSpinBox)
        msatcommander.setTabOrder(self.primerMaxSizeSpinBox, self.primerProductSizeTextBox)
        msatcommander.setTabOrder(self.primerProductSizeTextBox, self.primerMinTmSpinBox)
        msatcommander.setTabOrder(self.primerMinTmSpinBox, self.primerOptTmSpinBox)
        msatcommander.setTabOrder(self.primerOptTmSpinBox, self.primerMaxTmSpinBox)
        msatcommander.setTabOrder(self.primerMaxTmSpinBox, self.perfectRepeatsCheckBox)
        msatcommander.setTabOrder(self.perfectRepeatsCheckBox, self.tabWidget)
        msatcommander.setTabOrder(self.tabWidget, self.runButton)
        msatcommander.setTabOrder(self.runButton, self.customTagCheckBox)
        msatcommander.setTabOrder(self.customTagCheckBox, self.hexanucSpinBox)

    def retranslateUi(self, msatcommander):
        msatcommander.setWindowTitle(QtGui.QApplication.translate("msatcommander", "msatcommander-1.0.0-alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("msatcommander", "Search Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.dinucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Dinucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.pentanucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Pentanucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.trinucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Trinucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.hexanucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Hexanucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.tetranucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Tetranucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.combineLociCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Combine Loci", None, QtGui.QApplication.UnicodeUTF8))
        self.perfectRepeatsCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Perfect Repeats", None, QtGui.QApplication.UnicodeUTF8))
        self.mononucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Mononucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("msatcommander", "Primer Design", None, QtGui.QApplication.UnicodeUTF8))
        self.designPrimersCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Design Primers", None, QtGui.QApplication.UnicodeUTF8))
        self.tagPrimersCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Tag Primers", None, QtGui.QApplication.UnicodeUTF8))
        self.pigtailPrimersCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Pigtail Primers", None, QtGui.QApplication.UnicodeUTF8))
        self.cagTagCheckBox.setText(QtGui.QApplication.translate("msatcommander", "CAG Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.m13rCheckBox.setText(QtGui.QApplication.translate("msatcommander", "M13R Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.customTagCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Custom Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.pigtailPrimersTagLineEdit.setText(QtGui.QApplication.translate("msatcommander", "GTTT", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("msatcommander", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.commaSeparatedRadioButton.setText(QtGui.QApplication.translate("msatcommander", "Comma-Separated", None, QtGui.QApplication.UnicodeUTF8))
        self.tabDelimitedRadioButton.setText(QtGui.QApplication.translate("msatcommander", "Tab-Delimited", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("msatcommander", "Output Files", None, QtGui.QApplication.UnicodeUTF8))
        self.taggedPrimersCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Tagged Primers", None, QtGui.QApplication.UnicodeUTF8))
        self.combinedRepeatsCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Combined Repeats", None, QtGui.QApplication.UnicodeUTF8))
        self.primersCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Primers", None, QtGui.QApplication.UnicodeUTF8))
        self.repeatsCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Repeats", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("msatcommander", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_9.setTitle(QtGui.QApplication.translate("msatcommander", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.keepDatabaseCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Keep Database", None, QtGui.QApplication.UnicodeUTF8))
        self.keepDbaseSequenceRecords.setText(QtGui.QApplication.translate("msatcommander", "Keep Sequence Records", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("msatcommander", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("msatcommander", "Primer Sizes (BP)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("msatcommander", "Primer Min Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("msatcommander", "Primer Opt Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("msatcommander", "Primer Max Size", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("msatcommander", "Product Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("msatcommander", "Product Size", None, QtGui.QApplication.UnicodeUTF8))
        self.primerProductSizeTextBox.setText(QtGui.QApplication.translate("msatcommander", "100-450", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("msatcommander", "Space separated list of ranges.  E.g.:  100-200 200-300 300-400", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("msatcommander", "Primer Tms (Celsius)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("msatcommander", "Primer Min Tm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("msatcommander", "Primer Opt Tm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("msatcommander", "Primer Max Tm", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_10.setTitle(QtGui.QApplication.translate("msatcommander", "GC Content (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("msatcommander", "Primer Min GC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("msatcommander", "Primer Max GC", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_11.setTitle(QtGui.QApplication.translate("msatcommander", "PolyX (BP)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("msatcommander", "Max polyX", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_12.setTitle(QtGui.QApplication.translate("msatcommander", "Complementarity (Celsius)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("msatcommander", "Max, self, any", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("msatcommander", "Max, self, end", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("msatcommander", "Max, pair, any", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("msatcommander", "Max, pair, end", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("msatcommander", "Max, self, hairpin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("msatcommander", "Max, pair, hairpin", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_13.setTitle(QtGui.QApplication.translate("msatcommander", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.primerGCClampCheckBox.setText(QtGui.QApplication.translate("msatcommander", "GC Clamp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("msatcommander", "Max End Stability", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("msatcommander", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.runButton.setText(QtGui.QApplication.translate("msatcommander", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("msatcommander", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

