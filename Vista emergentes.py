#importamos las librerías necesarias
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi;

'''
QMainWindow: Es una clase que proporciona una ventana principal para aplicaciones GUI.

loadUi: Esta función permite cargar un archivo .ui creado con Qt Designer. 
El archivo .ui define la estructura y diseño de la interfaz gráfica.
'''

#Creamos una clase ventana, que se hereda de la clase "QMainWindow"
class Ventana(QMainWindow):
    def __init__(self): #Constructor de la clase
        #Inicializa la ventana
        QMainWindow.__init__(self)
        loadUi(r"C:\Users\DRA01\Desktop\Tema 4\Info-2\Unidad 4\Ventana principal.ui",self) #Lee el archivo de QtDesigner
        
        self.setWindowTitle("Ventana Principal") #Añadimos un título a nuestra ventana
        self.setup()
        
        #Conectar botón a función
    def setup(self):

        self.Yuyis.clicked.connect(self.funcion) #cuando el botón se presiona, se ejecutará el método funcion().

        

    def funcion(self):
        self.ventana_secundaria=ventanaSecundaria()
        self.ventana_secundaria.show()

class ventanaSecundaria(QDialog):
    def __init__(self): #Constructor de la clase
        #Inicializa la ventana
        QDialog.__init__(self)
        loadUi(r"C:\Users\DRA01\Desktop\Tema 4\Info-2\Unidad 4\Ventana emergente.ui",self) #Lee el archivo de QtDesigner
        
        self.setWindowTitle("Ventana Emergente") #Añadimos un título a nuestra ventana
        self.setup()

    def setup(self):

        self.buttonBox.accepted.connect(self.funcion) #cuando el botón se presiona, se ejecutará el método funcion().
        self.buttonBox.rejected.connect(lambda:self.close()) #cuando el botón se presiona, se ejecutará el método funcion().

    def funcion(self):
        pass


# se crea la instancia de la aplicación
app = QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())