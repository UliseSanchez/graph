# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 655)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionID_ascendente = QAction(MainWindow)
        self.actionID_ascendente.setObjectName(u"actionID_ascendente")
        self.actionDistancia_descendente = QAction(MainWindow)
        self.actionDistancia_descendente.setObjectName(u"actionDistancia_descendente")
        self.actionVelocidad_ascendente = QAction(MainWindow)
        self.actionVelocidad_ascendente.setObjectName(u"actionVelocidad_ascendente")
        self.actionPuntos_cercanos = QAction(MainWindow)
        self.actionPuntos_cercanos.setObjectName(u"actionPuntos_cercanos")
        self.actionPuntos = QAction(MainWindow)
        self.actionPuntos.setObjectName(u"actionPuntos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.id_label = QLabel(self.groupBox)
        self.id_label.setObjectName(u"id_label")

        self.gridLayout_2.addWidget(self.id_label, 0, 0, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.id_spinBox, 0, 1, 1, 1)

        self.origen_x_label = QLabel(self.groupBox)
        self.origen_x_label.setObjectName(u"origen_x_label")

        self.gridLayout_2.addWidget(self.origen_x_label, 1, 0, 1, 1)

        self.origen_x_spinBox = QSpinBox(self.groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.origen_x_spinBox, 1, 1, 1, 1)

        self.origen_y_label = QLabel(self.groupBox)
        self.origen_y_label.setObjectName(u"origen_y_label")

        self.gridLayout_2.addWidget(self.origen_y_label, 2, 0, 1, 1)

        self.origen_y_spinBox = QSpinBox(self.groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.origen_y_spinBox, 2, 1, 1, 1)

        self.destino_x_label = QLabel(self.groupBox)
        self.destino_x_label.setObjectName(u"destino_x_label")

        self.gridLayout_2.addWidget(self.destino_x_label, 3, 0, 1, 1)

        self.destino_x_spinBox = QSpinBox(self.groupBox)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.destino_x_spinBox, 3, 1, 1, 1)

        self.destino_y_label = QLabel(self.groupBox)
        self.destino_y_label.setObjectName(u"destino_y_label")

        self.gridLayout_2.addWidget(self.destino_y_label, 4, 0, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.groupBox)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.destino_y_spinBox, 4, 1, 1, 1)

        self.velocidad_label = QLabel(self.groupBox)
        self.velocidad_label.setObjectName(u"velocidad_label")

        self.gridLayout_2.addWidget(self.velocidad_label, 5, 0, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(100)

        self.gridLayout_2.addWidget(self.velocidad_spinBox, 5, 1, 1, 1)

        self.red_label = QLabel(self.groupBox)
        self.red_label.setObjectName(u"red_label")

        self.gridLayout_2.addWidget(self.red_label, 6, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.red_spinBox, 6, 1, 1, 1)

        self.green_label = QLabel(self.groupBox)
        self.green_label.setObjectName(u"green_label")

        self.gridLayout_2.addWidget(self.green_label, 7, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.green_spinBox, 7, 1, 1, 1)

        self.blue_label = QLabel(self.groupBox)
        self.blue_label.setObjectName(u"blue_label")

        self.gridLayout_2.addWidget(self.blue_label, 8, 0, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.blue_spinBox, 8, 1, 1, 1)

        self.agregar_inicio_particula_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_particula_pushButton.setObjectName(u"agregar_inicio_particula_pushButton")

        self.gridLayout_2.addWidget(self.agregar_inicio_particula_pushButton, 9, 0, 1, 2)

        self.agregar_final_particula_pushButton = QPushButton(self.groupBox)
        self.agregar_final_particula_pushButton.setObjectName(u"agregar_final_particula_pushButton")

        self.gridLayout_2.addWidget(self.agregar_final_particula_pushButton, 10, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.salida = QPlainTextEdit(self.groupBox_2)
        self.salida.setObjectName(u"salida")

        self.gridLayout_6.addWidget(self.salida, 0, 0, 1, 1)

        self.mostrar_particula_pushButton = QPushButton(self.groupBox_2)
        self.mostrar_particula_pushButton.setObjectName(u"mostrar_particula_pushButton")

        self.gridLayout_6.addWidget(self.mostrar_particula_pushButton, 1, 0, 1, 1)

        self.mostrar_grafo_pushButton = QPushButton(self.groupBox_2)
        self.mostrar_grafo_pushButton.setObjectName(u"mostrar_grafo_pushButton")

        self.gridLayout_6.addWidget(self.mostrar_grafo_pushButton, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 11, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_Visualizar = QWidget()
        self.tab_Visualizar.setObjectName(u"tab_Visualizar")
        self.gridLayout = QGridLayout(self.tab_Visualizar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.limpiar_pushButton = QPushButton(self.tab_Visualizar)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_Visualizar)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar_pushButton = QPushButton(self.tab_Visualizar)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_Visualizar, "")
        self.tab_Tabla = QWidget()
        self.tab_Tabla.setObjectName(u"tab_Tabla")
        self.gridLayout_4 = QGridLayout(self.tab_Tabla)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabla = QTableWidget(self.tab_Tabla)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_Tabla)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_Tabla)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_Tabla)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_Tabla, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuOrdenar = QMenu(self.menubar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuOrdenar.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuOrdenar.addAction(self.actionID_ascendente)
        self.menuOrdenar.addAction(self.actionDistancia_descendente)
        self.menuOrdenar.addAction(self.actionVelocidad_ascendente)
        self.menuAlgoritmos.addAction(self.actionPuntos_cercanos)
        self.menuVer.addAction(self.actionPuntos)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionID_ascendente.setText(QCoreApplication.translate("MainWindow", u"ID (ascendente)", None))
        self.actionDistancia_descendente.setText(QCoreApplication.translate("MainWindow", u"Distancia (descendente)", None))
        self.actionVelocidad_ascendente.setText(QCoreApplication.translate("MainWindow", u"Velocidad (ascendente)", None))
        self.actionPuntos_cercanos.setText(QCoreApplication.translate("MainWindow", u"Puntos Cercanos", None))
        self.actionPuntos.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.origen_x_label.setText(QCoreApplication.translate("MainWindow", u"Origen X:", None))
        self.origen_y_label.setText(QCoreApplication.translate("MainWindow", u"Origen Y:", None))
        self.destino_x_label.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.destino_y_label.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.velocidad_label.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.red_label.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.green_label.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.blue_label.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.agregar_inicio_particula_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.agregar_final_particula_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.mostrar_particula_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar particulas", None))
        self.mostrar_grafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar grafo", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Visualizar), QCoreApplication.translate("MainWindow", u"Visualizador", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identificador de p\u00e1rticula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Tabla), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
    # retranslateUi

