# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subjects_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SubjectsList(object):
    def setupUi(self, SubjectsList, prologInterface):
        SubjectsList.setObjectName("SubjectsList")
        SubjectsList.resize(1000, 600)
        SubjectsList.setMinimumSize(QtCore.QSize(1000, 600))
        SubjectsList.setMaximumSize(QtCore.QSize(1000, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("padre-pio.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubjectsList.setWindowIcon(icon)
        SubjectsList.setStyleSheet("background-color: rgb(193, 9, 42);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(SubjectsList)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(SubjectsList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 147, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(SubjectsList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(850, 200))
        self.tableWidget.setMaximumSize(QtCore.QSize(850, 200))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 2, 1, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(64, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 147, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 4, 0, 1, 1)
        self.aggiungi_materia = QtWidgets.QPushButton(SubjectsList)
        self.aggiungi_materia.setMinimumSize(QtCore.QSize(150, 50))
        self.aggiungi_materia.setMaximumSize(QtCore.QSize(150, 50))
        self.aggiungi_materia.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px;")
        self.aggiungi_materia.setObjectName("aggiungi_materia")
        self.gridLayout.addWidget(self.aggiungi_materia, 4, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(539, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 2, 1, 2)
        self.elimina_materia = QtWidgets.QPushButton(SubjectsList)
        self.elimina_materia.setMinimumSize(QtCore.QSize(150, 50))
        self.elimina_materia.setMaximumSize(QtCore.QSize(150, 50))
        self.elimina_materia.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px;")
        self.elimina_materia.setObjectName("elimina_materia")
        self.gridLayout.addWidget(self.elimina_materia, 4, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(64, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 5, 1, 1)

        self.retranslateUi(SubjectsList)
        QtCore.QMetaObject.connectSlotsByName(SubjectsList)

    def retranslateUi(self, SubjectsList):
        _translate = QtCore.QCoreApplication.translate
        SubjectsList.setWindowTitle(_translate("SubjectsList", "Subjects List"))
        self.label.setText(_translate("SubjectsList", "Insert/delete subject"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SubjectsList", "Subject"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SubjectsList", "Prof"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SubjectsList", "Course"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SubjectsList", "Semester"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SubjectsList", "Year"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SubjectsList", "Weekly Lessons"))
        self.aggiungi_materia.setText(_translate("SubjectsList", "Add"))
        self.elimina_materia.setText(_translate("SubjectsList", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubjectsList = QtWidgets.QWidget()
    ui = Ui_SubjectsList()
    ui.setupUi(SubjectsList)
    SubjectsList.show()
    sys.exit(app.exec_())
