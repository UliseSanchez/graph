from PySide2.QtCore import Slot
from PySide2.QtWidgets import QFileDialog, QGraphicsScene, QMainWindow, QMessageBox, QTableWidgetItem
from PySide2.QtGui import QPen, QColor, QTransform
from admin_particula import Administrador_Particulas
from algoritmos import obtener_puntos, puntos_mas_cercanos
from particula import Particula
from ui_mainwindow import Ui_MainWindow
from pprint import pprint


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()        
        self.particulas = Administrador_Particulas()
        self.ui.agregar_inicio_particula_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_final_particula_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_particula_pushButton.clicked.connect(self.click_mostrar)
        self.ui.mostrar_grafo_pushButton.clicked.connect(self.click_mostrar_grafo)

        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)
        self.ui.graphicsView.setScene(self.scene)

        self.ui.actionID_ascendente.triggered.connect(self.ordenar_id)
        self.ui.actionDistancia_descendente.triggered.connect(self.ordenar_distancia)
        self.ui.actionVelocidad_ascendente.triggered.connect(self.ordenar_velocidad)
        
        self.ui.actionPuntos_cercanos.triggered.connect(self.mostrar_puntos_cercanos)
        self.ui.actionPuntos.triggered.connect(self.dibujar_puntos)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8) 

    @Slot()
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.guardar_Archivo(ubicacion):
                QMessageBox.information(
                self,
                "Exito",
                "Se ha creado correctamente el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot()
    def action_Abrir_Archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir_Archivo(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se ha abierto correctamente el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo abrir el archivo " + ubicacion
            )
    @Slot( )
    def click_agregar(self):
        id = str(self.ui.id_spinBox.value())
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        green = self.ui.green_spinBox.value()
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y,velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula)
        self.particulas.agregar_particula_grafo(particula)
    
    @Slot( )
    def click_agregar_final(self):
        id = str(self.ui.id_spinBox.value())
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        green = self.ui.green_spinBox.value()
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y,velocidad, red, green, blue)
        self.particulas.agregar_final(particula)
        self.particulas.agregar_particula_grafo(particula)
            
    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.particulas:
            if id == str(particula.id):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)
                self.ui.tabla.setColumnCount(10)
                id_widget = QTableWidgetItem(str(particula.id))
                origen_widget = QTableWidgetItem(str(particula.origen))
                destino_widget = QTableWidgetItem(str(particula.destino))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                color_widget = QTableWidgetItem(str(particula.color))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_widget) 
                self.ui.tabla.setItem(0, 2, destino_widget) 
                self.ui.tabla.setItem(0, 3, velocidad_widget) 
                self.ui.tabla.setItem(0, 4, distancia_widget)
                self.ui.tabla.setItem(0, 5, color_widget)
                encontrado = True
                return 
            
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el identificador " {id} " no fue encontrado'
            )
   
    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(6)
        titulos = [ "ID", "Origen", "Destino", "Velocidad", "Distancia","Color"]
        self.ui.tabla.setHorizontalHeaderLabels(titulos)
        self.ui.tabla.setRowCount(len(self.particulas))

        row = 0
        for particula in self.particulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_widget = QTableWidgetItem(str(particula.origen))
            destino_widget = QTableWidgetItem(str(particula.destino))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            distancia_widget = QTableWidgetItem(str(particula.distancia))
            color_widget = QTableWidgetItem(str(particula.color))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_widget) 
            self.ui.tabla.setItem(row, 2, destino_widget) 
            self.ui.tabla.setItem(row, 3, velocidad_widget) 
            self.ui.tabla.setItem(row, 4, distancia_widget)
            self.ui.tabla.setItem(row, 5, color_widget)
            row += 1

    @Slot( )
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))
    
    @Slot( )
    def click_mostrar_grafo(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas.mostrar_grafo()))
        print(str(self.particulas.mostrar_grafo()))

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def ordenar_id(self):
        self.particulas.ordenar_por_id()
        
    @Slot()
    def ordenar_distancia(self):
        self.particulas.ordenar_por_distancia()
    
    @Slot()
    def ordenar_velocidad(self):
        self.particulas.ordenar_por_velocidad()

    @Slot( )
    def dibujar(self):
        pen = QPen()
        pen.setWidth(4)
        for particula in self.particulas:
            color = QColor(particula.color[0],particula.color[1],particula.color[2])
            pen.setColor(color)
            x_origen = particula.origen[0]
            y_origen = particula.origen[1]
            x_destino = particula.destino[0]
            y_destino = particula.destino[1]
            self.scene.addEllipse(x_origen, y_origen,6, 6, pen)
            self.scene.addEllipse(x_destino, y_destino,6, 6, pen)
            self.scene.addLine(x_origen+3, y_origen+3, x_destino+3, y_destino+3, pen)    

    @Slot()
    def mostrar_puntos_cercanos(self):        
        resultado = puntos_mas_cercanos(self.particulas)
        pen = QPen()
        pen.setWidth(2)
        contador = 0
        colores = self.obtener_colores()
        for punto1, punto2 in resultado:
            x1 = punto1[0]
            y1 = punto1[1]
            x2 = punto2[0]
            y2 = punto2[1]
            pen.setColor(colores[contador])
            contador += 1
            self.scene.addLine(x1, y1, x2, y2, pen)
            self.scene.addRect(x1, y1, 6, 6, pen)
            self.scene.addRect(x2, y2, 6, 6, pen)

    @Slot()
    def dibujar_puntos(self):
        puntos = obtener_puntos(self.particulas)
        contador = 0
        pen = QPen()
        pen.setWidth(2)
        colores = self.obtener_colores()
        for punto in puntos:
            x = punto[0]
            y = punto[1]
            pen.setColor(colores[contador])
            contador += 1
            self.scene.addRect(x, y, 6, 6,pen)

    def obtener_colores(self):
        colores = []
        for particula in self.particulas:
            color = QColor(particula.color[0],particula.color[1],particula.color[2])
            colores.append(color)
            colores.append(color)
        return colores

