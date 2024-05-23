# Hola
(Diagrama de clases)
https://app.moqups.com/NoAlp3kSULaLU9grtF6EYpqLPCVswbdZ/view/page/a8bfb0d3e?ui=0
(Video)
https://youtu.be/PanE6ik5K4g?feature=shared

Documentacion código taller 3 

Primera parte :

Se importan todas las librerías que vamos a utilizar con el código IMPORT 
Por ejemplo :

import dicom2nifti
import nibabel as nib
from nilearn import plotting, image
import pydicom

Segunda parte:

Creación de la clase y sus respectivas funciones que nos darán los datos necesarios para solventar el problema, en este caso llamamos a la clase y sus funciones:

class obtenerdatos():
clas=obtenerdatos()
clas.Verificar()
clas.buscarestudio()
clas.eliminarestudio()
clas.consultardatos()
clas.Anonimizar()
clas.NIFTI()

Definimos VERIFICAR, con el código el cual nos dará la opción de poner el archivo de estudio que queramos verificar si está en los respectivos pacientes:
ESdesc=input("Ingresa el nombre del estuido : ")
      desc= pydicom.dcmread(r""+ESdesc+"")
      if desc.PatientID == self.ID1 :
            print("Estudio ya registrado en el paciente con ID",self.ID1)  
      elif desc.PatientID == self.ID2 :
            print("Estudio ya registrado en el paciente con ID",self.ID2)
      elif desc.PatientID == self.ID3 :
            print("Estudio ya registrado en el paciente con ID",self.ID3)
      else :
          x=input("Estudio no registrado , desea agregarlo ?")


Definimos buscar estudio , el cual nos permitirá poner el ID del paciente al cual queramos buscar su respetivo estudio , si el estudio se encuentra en el archivo del paciente , saldrá un mensaje de confirmación , sino saldrá uno de negación :


ESconoci=input("Ingresa el estudio que deseas consultar si pertenece a la base de datos : ")
        conoci= pydicom.dcmread(r''+ESconoci+'')
        if conoci.PatientID == self.ID1 :
            print("Estudio encontrado en el paciente con ID",self.ID1)   
            
        elif conoci.PatientID == self.ID2 :
            print("Estudio encontrado en el paciente con ID",self.ID2)
            
        elif conoci.PatientID == self.ID3 :
            print("Estudio encontrado en el paciente con ID",self.ID3)
        else :
            print("ESTUDIO NO ENCONTRADO EN LA BASE DE DATOS")


Definimos ELIMINAR ESTUDIO el cual nos permitirá igualmente poner el ID del paciente al cual queramos eliminar un estudio de su base de datos , ahora según el estudio que queramos eliminar , lo indicaremos y este será correctamente eliminado del archivo del paciente :


ESelimin=input("Ingresa el ID del paciente al que le deseas eliminar los estudios :")
        if ESelimin == self.ID1 :
            estuelim=input("Que estudio desea eliminar del paciente con ID"+self.ID1)
            for estu in listdir(r'C:\Users\Juan Pablo JimenezS\Downloads\profesora\0001'):
                try :
                    remove(r""+estuelim+"")
                except FileNotFoundError:
                    pass


Definimos CONSULTAR DATOS , el cual nos permitirá según el ID del paciente que indiquemos , verificar cierta información que neceitemos de este , como su ID , TIEMPO DEL ESTUDIO , MODALIDAD , y CANTIDAD DE ESTUDIOS :


if IDpaciente == self.ID1 :
            consul=input("Que desa consultar del pacinete con ID"+IDpaciente+'\n 1°)Fecha'+' \n 2°)Modalidad \n'+' 3°)Descripción'+' \n 4°)Dimensiones imagen '+'\n5°)Cantidad de estudios') 
            if consul == "1" :
                print("El tiempo del estudio es ",datos1.StudyTime)
            elif consul =="2" :
                print("La modalidad del estudio es ",datos1.Modality)
            elif consul == "3" :
                print("La descripcion del estudio es ",datos1.SeriesDescription)


Definimos ANONIMIZAR , el cual nos permitirá según el ID del paciente que necesitemos anonimizar su ID y MODALIDAD  del estudio nos devolverá su nuevo estudio anonimizado con esos valores y en un nuevo archivo :


idcom=input("Indique el ID del paciente que desea anonimizar su NOMBRE y MODALIDAD :")
   if idcom==self.ID1:
        for i in eleanonim:
             datos1[i].value=None
         datos1.save_as('ANONIMO.dcm')
         print("CAMBIOS REALIZADOS CORRECTAMENTE")


La ultima función seria la de GRAFICAR , la cual aparte de graficar sus respectivos estudiso de diferentes maneras como SOLA , 3 VISTAS y MOSAICO , también cambiara y avizara al usuario sobre los cambios hechos en la carpeta de DICOM a NIFTI :


x=input("Indique el ID del paciente al que quiere imprimir los estudios : "+"\nDIGITE NO PARA CANCELAR RECODIFICACIÓN")
        if x=="NO":
            print("RECODIFICACIÓN CANCELADA")
        if x == self.ID1 :
            if self.nifti1==0:
                self.nifti1=self.nifti1+1
                nifti_directory = r"C:\Users\Juan Pablo Jimenez S\Downloads\profesora\nifti_001"    
                dicom_directory = r"C:\Users\Juan Pablo Jimenez S\Downloads\profesora\0001"
                dicom2nifti.convert_directory(dicom_directory,nifti_directory)


Por ultimo definimos el MENU PRINCIPAL  , el cual nos dara la respectiva información de todas las funciones y permitirá al usuario desear que función quiere realizar , también con la opción de SALIR de este menú principa si ya termino de realizar todos los cambios y acciones que deseo:


while True :
    x=int(input("indique que desea realizar"+"\n1°Verificar Estudio"+"\n2°Buscar Estudio"+"\n3°Eliminar Estudio"+"\n4°Consultar Datos"+"\n5°Anonimizar Estudio"+"\n6°Graficar"+"\n7°Salir"))
    ir x==1 :
        clas=obtenerdatos()
        clas.Verificar()
    if x==2 :
        clas=obtenerdatos()
        clas.buscarestudio()
    if x==3 :
        clas=obtenerdatos()
        clas.eliminarestudio()
    if x==4 :
        clas=obtenerdatos()
        clas.consultardatos()
    if x==5 :
        clas=obtenerdatos()
        clas.Anonimizar()
    if x==6 :
        clas=obtenerdatos()
    if x==7:
        break
       

