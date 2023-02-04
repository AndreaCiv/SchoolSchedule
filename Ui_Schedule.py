# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schedule.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui

from PyQt5 import QtWidgets

from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QAbstractItemView
from SubjectsListView import SubjectsListView

class Ui_Schedule(object):
    def setupUi(self, Schedule, prologInterface):
        self.prologInterface = prologInterface

        self.possible_schedules = None
        self.numero_calendario = 0

        Schedule.setObjectName("Schedule")
        Schedule.setWindowModality(QtCore.Qt.WindowModal)
        Schedule.resize(1000, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Schedule.sizePolicy().hasHeightForWidth())
        Schedule.setSizePolicy(sizePolicy)
        Schedule.setMinimumSize(QtCore.QSize(1000, 600))
        Schedule.setMaximumSize(QtCore.QSize(1000, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("padre-pio.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Schedule.setWindowIcon(icon)
        Schedule.setStyleSheet("background-color: rgb(193, 9, 42);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"")
        Schedule.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(Schedule)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.seleziona_corso = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seleziona_corso.sizePolicy().hasHeightForWidth())
        self.seleziona_corso.setSizePolicy(sizePolicy)
        self.seleziona_corso.setMinimumSize(QtCore.QSize(150,40))
        #self.seleziona_corso.setMaximumSize(QtCore.QSize(16777215, 19))
        self.seleziona_corso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.seleziona_corso.setObjectName("seleziona_corso")

        self.seleziona_corso.activated.connect(self.populate_seleziona_anno)

        self.verticalLayout_2.addWidget(self.seleziona_corso)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.seleziona_anno = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seleziona_anno.sizePolicy().hasHeightForWidth())
        self.seleziona_anno.setSizePolicy(sizePolicy)
        self.seleziona_anno.setMinimumSize(QtCore.QSize(150,40))
        self.seleziona_anno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.seleziona_anno.setObjectName("seleziona_anno")

        self.seleziona_anno.activated.connect(self.populate_seleziona_semestre)


        self.verticalLayout_3.addWidget(self.seleziona_anno)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.seleziona_semestre = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seleziona_semestre.sizePolicy().hasHeightForWidth())
        self.seleziona_semestre.setSizePolicy(sizePolicy)
        self.seleziona_semestre.setMinimumSize(QtCore.QSize(150,40))

        self.seleziona_semestre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.seleziona_semestre.setObjectName("seleziona_semestre")
        self.verticalLayout_4.addWidget(self.seleziona_semestre)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.calcola_orario = QtWidgets.QPushButton(self.centralwidget)
        self.calcola_orario.setMinimumSize(QtCore.QSize(150, 50))
        self.calcola_orario.setMaximumSize(QtCore.QSize(150, 50))
        self.calcola_orario.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px;")
        self.calcola_orario.setObjectName("calcola_orario")
        self.calcola_orario.clicked.connect(self.crea_orario_prima_volta)
        self.horizontalLayout.addWidget(self.calcola_orario)
        spacerItem5 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(64, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(850, 200))
        self.tableWidget.setMaximumSize(QtCore.QSize(850, 200))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
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
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.gridLayout.addWidget(self.tableWidget, 3, 1, 1, 4)
        spacerItem8 = QtWidgets.QSpacerItem(64, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 4, 0, 3, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 4, 1, 3, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 4, 4, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 5, 3, 1, 1)
        self.cambia_orario = QtWidgets.QPushButton(self.centralwidget)
        self.cambia_orario.setMinimumSize(QtCore.QSize(150, 50))
        self.cambia_orario.setMaximumSize(QtCore.QSize(150, 50))
        self.cambia_orario.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px;")
        self.cambia_orario.setObjectName("cambia_orario")
        self.cambia_orario.clicked.connect(self.cambia_orario_funzione)
        self.gridLayout.addWidget(self.cambia_orario, 5, 4, 1, 1)

        self.modifica_materie = QtWidgets.QPushButton(self.centralwidget)
        self.modifica_materie.setMinimumSize(QtCore.QSize(150, 50))
        self.modifica_materie.setMaximumSize(QtCore.QSize(150, 50))
        self.modifica_materie.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px;")
        self.modifica_materie.setObjectName("modifica_materie")
        self.modifica_materie.clicked.connect(self.open_subjects_list)
        self.gridLayout.addWidget(self.modifica_materie, 5, 1, 1, 1)


        spacerItem13 = QtWidgets.QSpacerItem(64, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 5, 5, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem14, 6, 4, 1, 1)
        Schedule.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Schedule)
        self.statusbar.setObjectName("statusbar")
        Schedule.setStatusBar(self.statusbar)

        self.retranslateUi(Schedule)
        QtCore.QMetaObject.connectSlotsByName(Schedule)

        self.populate_seleziona_corso()
        self.populate_seleziona_anno()
        self.populate_seleziona_semestre()

    def open_subjects_list(self):
        self.vista_lista_materie = SubjectsListView(self.prologInterface, self.populate_seleziona_corso)
        self.vista_lista_materie.show_subject_list_view()

    def populate_seleziona_corso(self):
        courses = self.prologInterface.get_courses()
        self.seleziona_corso.clear()
        for course in courses:
            self.seleziona_corso.addItem(course)
        self.populate_seleziona_anno()

    def populate_seleziona_anno(self):
        self.seleziona_anno.clear()
        course = self.seleziona_corso.currentText()
        years = self.prologInterface.get_years_by_course(course)
        for year in years:
            self.seleziona_anno.addItem(str(year))
        self.populate_seleziona_semestre()

    def populate_seleziona_semestre(self):
        self.seleziona_semestre.clear()
        course = self.seleziona_corso.currentText()
        year = self.seleziona_anno.currentText()
        semesters = self.prologInterface.get_semesters_by_course_and_year(course,year)
        for semester in semesters:
            self.seleziona_semestre.addItem(str(semester))

    def retranslateUi(self, Schedule):
        _translate = QtCore.QCoreApplication.translate
        Schedule.setWindowTitle(_translate("Schedule", "Schedule for you"))
        self.label.setText(_translate("Schedule", "Select Course"))
        #self.seleziona_corso.setItemText(0, _translate("Schedule", "Ingegneria Informatica"))
        #self.seleziona_corso.setItemText(1, _translate("Schedule", "Ingeneria Elettronica"))
        self.label_2.setText(_translate("Schedule", "Select year"))
        #self.seleziona_anno.setItemText(0, _translate("Schedule", "1"))
        #self.seleziona_anno.setItemText(1, _translate("Schedule", "2"))
        self.label_3.setText(_translate("Schedule", "Select semester"))
        #self.seleziona_semestre.setItemText(0, _translate("Schedule", "1"))
        #self.seleziona_semestre.setItemText(1, _translate("Schedule", "2"))
        #self.seleziona_semestre.setItemText(2, _translate("Schedule", "3"))
        self.calcola_orario.setText(_translate("Schedule", "Calculate Schedule"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Schedule", "8:30-10:30"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Schedule", "10:30-12:30"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Schedule", "14:30-16:30"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Schedule", "16:30-18:30"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Schedule", "Monday"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Schedule", "Thursday"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Schedule", "Wednesday"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Schedule", "Tuesday"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Schedule", "Friday"))
        self.cambia_orario.setText(_translate("Schedule", "Change Schedule"))
        self.modifica_materie.setText(_translate("Schedule", "Modify Subjects"))

    # Funzione da connettere al bottone calcola orario
    # Calcola l'orario e lo visualizza sull'interfaccia grafica
    def crea_orario_prima_volta(self):
        course = self.seleziona_corso.currentText()
        year = int(self.seleziona_anno.currentText())
        semester = int(self.seleziona_semestre.currentText())
        possible_schedules = self.prologInterface.create_semester_schedule(course, year, semester)
        self.possible_schedules = possible_schedules
        self.numero_calendario = 0
        first_schedule = self.possible_schedules[0]
        for i in range(0,4):
            for j in range(0,5):
                self.tableWidget.setItem(i,j, QTableWidgetItem())
        self.visualizza_orario(first_schedule)

    # Funzione da connettere al pulsante cambia orario
    # Scorre i possibili orari e li visualizza, restituisce un messaggio di errore se non è stato ancora calcolato alcun
    # orario o se non ci sono altri orari disponibili
    def cambia_orario_funzione(self):
        if self.possible_schedules == None:
            QMessageBox.critical(None,"Error", "No schedule has been calculated yet",QMessageBox.Ok, QMessageBox.Ok)
            return
        if self.numero_calendario == len(self.possible_schedules)-1:
            QMessageBox.critical(None,"Error", "There are no more schedules available", QMessageBox.Ok,QMessageBox.Ok)
            return
        for i in range(0,4):
            for j in range(0,5):
                self.tableWidget.setItem(i,j, QTableWidgetItem())
        self.numero_calendario = self.numero_calendario + 1
        self.visualizza_orario(self.possible_schedules[self.numero_calendario])


    def visualizza_orario(self, schedule):
        for session in schedule.schedule:
            item = QTableWidgetItem()
            item.setText(session.subject)
            item.setTextAlignment(Qt.AlignCenter)
            coordinates = session.get_coordinates()
            self.tableWidget.setItem(coordinates[0], coordinates[1], item)
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)


