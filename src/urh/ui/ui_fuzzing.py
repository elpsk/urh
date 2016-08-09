# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FuzzingDialog(object):
    def setupUi(self, FuzzingDialog):
        FuzzingDialog.setObjectName("FuzzingDialog")
        FuzzingDialog.resize(840, 810)
        self.gridLayout_5 = QtWidgets.QGridLayout(FuzzingDialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lFuzzingLabel = QtWidgets.QLabel(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lFuzzingLabel.sizePolicy().hasHeightForWidth())
        self.lFuzzingLabel.setSizePolicy(sizePolicy)
        self.lFuzzingLabel.setObjectName("lFuzzingLabel")
        self.gridLayout_5.addWidget(self.lFuzzingLabel, 0, 0, 1, 1)
        self.comboBoxFuzzingLabel = QtWidgets.QComboBox(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxFuzzingLabel.sizePolicy().hasHeightForWidth())
        self.comboBoxFuzzingLabel.setSizePolicy(sizePolicy)
        self.comboBoxFuzzingLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxFuzzingLabel.setEditable(True)
        self.comboBoxFuzzingLabel.setObjectName("comboBoxFuzzingLabel")
        self.gridLayout_5.addWidget(self.comboBoxFuzzingLabel, 0, 1, 1, 1)
        self.lSourceBlock = QtWidgets.QLabel(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSourceBlock.sizePolicy().hasHeightForWidth())
        self.lSourceBlock.setSizePolicy(sizePolicy)
        self.lSourceBlock.setObjectName("lSourceBlock")
        self.gridLayout_5.addWidget(self.lSourceBlock, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lPreBits = QtWidgets.QLabel(FuzzingDialog)
        self.lPreBits.setObjectName("lPreBits")
        self.horizontalLayout_2.addWidget(self.lPreBits)
        self.lFuzzedBits = QtWidgets.QLabel(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lFuzzedBits.sizePolicy().hasHeightForWidth())
        self.lFuzzedBits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lFuzzedBits.setFont(font)
        self.lFuzzedBits.setAlignment(QtCore.Qt.AlignCenter)
        self.lFuzzedBits.setObjectName("lFuzzedBits")
        self.horizontalLayout_2.addWidget(self.lFuzzedBits)
        self.lPostBits = QtWidgets.QLabel(FuzzingDialog)
        self.lPostBits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lPostBits.setObjectName("lPostBits")
        self.horizontalLayout_2.addWidget(self.lPostBits)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.lFuzzingReferenceBlock = QtWidgets.QLabel(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lFuzzingReferenceBlock.sizePolicy().hasHeightForWidth())
        self.lFuzzingReferenceBlock.setSizePolicy(sizePolicy)
        self.lFuzzingReferenceBlock.setObjectName("lFuzzingReferenceBlock")
        self.gridLayout_5.addWidget(self.lFuzzingReferenceBlock, 2, 0, 1, 1)
        self.spinBoxFuzzBlock = QtWidgets.QSpinBox(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxFuzzBlock.sizePolicy().hasHeightForWidth())
        self.spinBoxFuzzBlock.setSizePolicy(sizePolicy)
        self.spinBoxFuzzBlock.setMaximum(999999999)
        self.spinBoxFuzzBlock.setObjectName("spinBoxFuzzBlock")
        self.gridLayout_5.addWidget(self.spinBoxFuzzBlock, 2, 1, 1, 1)
        self.lFuzzingStart = QtWidgets.QLabel(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lFuzzingStart.sizePolicy().hasHeightForWidth())
        self.lFuzzingStart.setSizePolicy(sizePolicy)
        self.lFuzzingStart.setObjectName("lFuzzingStart")
        self.gridLayout_5.addWidget(self.lFuzzingStart, 3, 0, 1, 1)
        self.spinBoxFuzzingStart = QtWidgets.QSpinBox(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxFuzzingStart.sizePolicy().hasHeightForWidth())
        self.spinBoxFuzzingStart.setSizePolicy(sizePolicy)
        self.spinBoxFuzzingStart.setMinimum(1)
        self.spinBoxFuzzingStart.setMaximum(999999999)
        self.spinBoxFuzzingStart.setObjectName("spinBoxFuzzingStart")
        self.gridLayout_5.addWidget(self.spinBoxFuzzingStart, 3, 1, 1, 1)
        self.lFuzzingEnd = QtWidgets.QLabel(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lFuzzingEnd.sizePolicy().hasHeightForWidth())
        self.lFuzzingEnd.setSizePolicy(sizePolicy)
        self.lFuzzingEnd.setObjectName("lFuzzingEnd")
        self.gridLayout_5.addWidget(self.lFuzzingEnd, 4, 0, 1, 1)
        self.spinBoxFuzzingEnd = QtWidgets.QSpinBox(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxFuzzingEnd.sizePolicy().hasHeightForWidth())
        self.spinBoxFuzzingEnd.setSizePolicy(sizePolicy)
        self.spinBoxFuzzingEnd.setMinimum(1)
        self.spinBoxFuzzingEnd.setMaximum(999999999)
        self.spinBoxFuzzingEnd.setObjectName("spinBoxFuzzingEnd")
        self.gridLayout_5.addWidget(self.spinBoxFuzzingEnd, 4, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lFuzzedValues = QtWidgets.QLabel(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lFuzzedValues.sizePolicy().hasHeightForWidth())
        self.lFuzzedValues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lFuzzedValues.setFont(font)
        self.lFuzzedValues.setAlignment(QtCore.Qt.AlignCenter)
        self.lFuzzedValues.setObjectName("lFuzzedValues")
        self.verticalLayout.addWidget(self.lFuzzedValues)
        self.chkBRemoveDuplicates = QtWidgets.QCheckBox(FuzzingDialog)
        self.chkBRemoveDuplicates.setObjectName("chkBRemoveDuplicates")
        self.verticalLayout.addWidget(self.chkBRemoveDuplicates)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tblFuzzingValues = FuzzingTableView(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblFuzzingValues.sizePolicy().hasHeightForWidth())
        self.tblFuzzingValues.setSizePolicy(sizePolicy)
        self.tblFuzzingValues.setAlternatingRowColors(True)
        self.tblFuzzingValues.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblFuzzingValues.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblFuzzingValues.setShowGrid(False)
        self.tblFuzzingValues.setObjectName("tblFuzzingValues")
        self.tblFuzzingValues.horizontalHeader().setHighlightSections(False)
        self.tblFuzzingValues.verticalHeader().setHighlightSections(False)
        self.gridLayout_4.addWidget(self.tblFuzzingValues, 0, 0, 3, 1)
        self.btnAddRow = QtWidgets.QToolButton(FuzzingDialog)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnAddRow.setIcon(icon)
        self.btnAddRow.setObjectName("btnAddRow")
        self.gridLayout_4.addWidget(self.btnAddRow, 0, 1, 1, 1)
        self.btnDelRow = QtWidgets.QToolButton(FuzzingDialog)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.btnDelRow.setIcon(icon)
        self.btnDelRow.setObjectName("btnDelRow")
        self.gridLayout_4.addWidget(self.btnDelRow, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_5.addLayout(self.verticalLayout, 5, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBoxAddRange = QtWidgets.QGroupBox(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxAddRange.sizePolicy().hasHeightForWidth())
        self.groupBoxAddRange.setSizePolicy(sizePolicy)
        self.groupBoxAddRange.setObjectName("groupBoxAddRange")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxAddRange)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lStart = QtWidgets.QLabel(self.groupBoxAddRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lStart.sizePolicy().hasHeightForWidth())
        self.lStart.setSizePolicy(sizePolicy)
        self.lStart.setObjectName("lStart")
        self.gridLayout_2.addWidget(self.lStart, 0, 0, 1, 1)
        self.sBAddRangeStart = QtWidgets.QSpinBox(self.groupBoxAddRange)
        self.sBAddRangeStart.setObjectName("sBAddRangeStart")
        self.gridLayout_2.addWidget(self.sBAddRangeStart, 0, 1, 1, 1)
        self.lEnd = QtWidgets.QLabel(self.groupBoxAddRange)
        self.lEnd.setObjectName("lEnd")
        self.gridLayout_2.addWidget(self.lEnd, 1, 0, 1, 1)
        self.sBAddRangeEnd = QtWidgets.QSpinBox(self.groupBoxAddRange)
        self.sBAddRangeEnd.setObjectName("sBAddRangeEnd")
        self.gridLayout_2.addWidget(self.sBAddRangeEnd, 1, 1, 1, 1)
        self.lStep = QtWidgets.QLabel(self.groupBoxAddRange)
        self.lStep.setObjectName("lStep")
        self.gridLayout_2.addWidget(self.lStep, 2, 0, 1, 1)
        self.sBAddRangeStep = QtWidgets.QSpinBox(self.groupBoxAddRange)
        self.sBAddRangeStep.setMinimum(1)
        self.sBAddRangeStep.setObjectName("sBAddRangeStep")
        self.gridLayout_2.addWidget(self.sBAddRangeStep, 2, 1, 1, 1)
        self.btnAddRange = QtWidgets.QPushButton(self.groupBoxAddRange)
        self.btnAddRange.setObjectName("btnAddRange")
        self.gridLayout_2.addWidget(self.btnAddRange, 3, 0, 1, 2)
        self.horizontalLayout_4.addWidget(self.groupBoxAddRange)
        self.groupBox = QtWidgets.QGroupBox(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxLowerBound = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxLowerBound.setChecked(True)
        self.checkBoxLowerBound.setObjectName("checkBoxLowerBound")
        self.gridLayout.addWidget(self.checkBoxLowerBound, 0, 0, 1, 1)
        self.spinBoxLowerBound = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxLowerBound.setObjectName("spinBoxLowerBound")
        self.gridLayout.addWidget(self.spinBoxLowerBound, 0, 1, 1, 1)
        self.checkBoxUpperBound = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxUpperBound.setChecked(True)
        self.checkBoxUpperBound.setObjectName("checkBoxUpperBound")
        self.gridLayout.addWidget(self.checkBoxUpperBound, 1, 0, 1, 1)
        self.spinBoxUpperBound = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxUpperBound.setObjectName("spinBoxUpperBound")
        self.gridLayout.addWidget(self.spinBoxUpperBound, 1, 1, 1, 1)
        self.lNumberBoundaries = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lNumberBoundaries.sizePolicy().hasHeightForWidth())
        self.lNumberBoundaries.setSizePolicy(sizePolicy)
        self.lNumberBoundaries.setObjectName("lNumberBoundaries")
        self.gridLayout.addWidget(self.lNumberBoundaries, 2, 0, 1, 1)
        self.spinBoxBoundaryNumber = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxBoundaryNumber.setMinimum(1)
        self.spinBoxBoundaryNumber.setObjectName("spinBoxBoundaryNumber")
        self.gridLayout.addWidget(self.spinBoxBoundaryNumber, 2, 1, 1, 1)
        self.btnAddBoundaries = QtWidgets.QPushButton(self.groupBox)
        self.btnAddBoundaries.setObjectName("btnAddBoundaries")
        self.gridLayout.addWidget(self.btnAddBoundaries, 3, 0, 1, 2)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBoxxRandom = QtWidgets.QGroupBox(FuzzingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxxRandom.sizePolicy().hasHeightForWidth())
        self.groupBoxxRandom.setSizePolicy(sizePolicy)
        self.groupBoxxRandom.setObjectName("groupBoxxRandom")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxxRandom)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lNumRandom = QtWidgets.QLabel(self.groupBoxxRandom)
        self.lNumRandom.setObjectName("lNumRandom")
        self.gridLayout_3.addWidget(self.lNumRandom, 0, 0, 1, 1)
        self.spinBoxNumberRandom = QtWidgets.QSpinBox(self.groupBoxxRandom)
        self.spinBoxNumberRandom.setMinimum(1)
        self.spinBoxNumberRandom.setMaximum(999999999)
        self.spinBoxNumberRandom.setObjectName("spinBoxNumberRandom")
        self.gridLayout_3.addWidget(self.spinBoxNumberRandom, 0, 1, 1, 1)
        self.lRandomMin = QtWidgets.QLabel(self.groupBoxxRandom)
        self.lRandomMin.setObjectName("lRandomMin")
        self.gridLayout_3.addWidget(self.lRandomMin, 1, 0, 1, 1)
        self.spinBoxRandomMinimum = QtWidgets.QSpinBox(self.groupBoxxRandom)
        self.spinBoxRandomMinimum.setObjectName("spinBoxRandomMinimum")
        self.gridLayout_3.addWidget(self.spinBoxRandomMinimum, 1, 1, 1, 1)
        self.lRandomMax = QtWidgets.QLabel(self.groupBoxxRandom)
        self.lRandomMax.setObjectName("lRandomMax")
        self.gridLayout_3.addWidget(self.lRandomMax, 2, 0, 1, 1)
        self.spinBoxRandomMaximum = QtWidgets.QSpinBox(self.groupBoxxRandom)
        self.spinBoxRandomMaximum.setObjectName("spinBoxRandomMaximum")
        self.gridLayout_3.addWidget(self.spinBoxRandomMaximum, 2, 1, 1, 1)
        self.btnAddRandom = QtWidgets.QPushButton(self.groupBoxxRandom)
        self.btnAddRandom.setObjectName("btnAddRandom")
        self.gridLayout_3.addWidget(self.btnAddRandom, 3, 0, 1, 2)
        self.horizontalLayout_4.addWidget(self.groupBoxxRandom)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 6, 0, 1, 2)
        self.btnSaveAndClose = QtWidgets.QPushButton(FuzzingDialog)
        self.btnSaveAndClose.setObjectName("btnSaveAndClose")
        self.gridLayout_5.addWidget(self.btnSaveAndClose, 7, 0, 1, 2)

        self.retranslateUi(FuzzingDialog)
        QtCore.QMetaObject.connectSlotsByName(FuzzingDialog)

    def retranslateUi(self, FuzzingDialog):
        _translate = QtCore.QCoreApplication.translate
        FuzzingDialog.setWindowTitle(_translate("FuzzingDialog", "Fuzzing"))
        self.lFuzzingLabel.setText(_translate("FuzzingDialog", "Fuzzing Label:"))
        self.lSourceBlock.setText(_translate("FuzzingDialog", "Source Block:"))
        self.lPreBits.setText(_translate("FuzzingDialog", "1111"))
        self.lFuzzedBits.setText(_translate("FuzzingDialog", "1010"))
        self.lPostBits.setText(_translate("FuzzingDialog", "010101"))
        self.lFuzzingReferenceBlock.setText(_translate("FuzzingDialog", "Block to fuzz:"))
        self.lFuzzingStart.setText(_translate("FuzzingDialog", "Fuzzing Label Start Index:"))
        self.lFuzzingEnd.setText(_translate("FuzzingDialog", "Fuzzing Label End Index:"))
        self.lFuzzedValues.setText(_translate("FuzzingDialog", "Fuzzed Values"))
        self.chkBRemoveDuplicates.setText(_translate("FuzzingDialog", "Remove Duplicates"))
        self.btnAddRow.setText(_translate("FuzzingDialog", "..."))
        self.btnDelRow.setText(_translate("FuzzingDialog", "..."))
        self.groupBoxAddRange.setTitle(_translate("FuzzingDialog", "Add Range"))
        self.lStart.setText(_translate("FuzzingDialog", "Start (Decimal):"))
        self.lEnd.setText(_translate("FuzzingDialog", "End (Decimal):"))
        self.lStep.setText(_translate("FuzzingDialog", "Step (Decimal):"))
        self.btnAddRange.setText(_translate("FuzzingDialog", "Add to Fuzzed Values"))
        self.groupBox.setTitle(_translate("FuzzingDialog", "Add Boundaries"))
        self.checkBoxLowerBound.setText(_translate("FuzzingDialog", "Lower Bound"))
        self.checkBoxUpperBound.setText(_translate("FuzzingDialog", "Upper Bound"))
        self.lNumberBoundaries.setText(_translate("FuzzingDialog", "Border Values:"))
        self.btnAddBoundaries.setText(_translate("FuzzingDialog", "Add to Fuzzed Values"))
        self.groupBoxxRandom.setTitle(_translate("FuzzingDialog", "Add random values from range"))
        self.lNumRandom.setText(_translate("FuzzingDialog", "Number:"))
        self.lRandomMin.setText(_translate("FuzzingDialog", "Range Minimum:"))
        self.lRandomMax.setText(_translate("FuzzingDialog", "Range Maximum:"))
        self.btnAddRandom.setText(_translate("FuzzingDialog", "Add to Fuzzed Values"))
        self.btnSaveAndClose.setText(_translate("FuzzingDialog", "Save and Close"))

from urh.ui.views.FuzzingTableView import FuzzingTableView
