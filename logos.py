#!/usr/bin/env python3
from PIL import Image
import glob
import os


#***************Funcion de pegar imagenes juntas***************/
def AddLogo(mfname, lfname, outfname , tlogo):

    mimage = Image.open(mfname)
    limage = Image.open(lfname)

    # resize logo
    wsize = int(mimage.size[0]* float(tlogo)/float(100))
    wpercent = (wsize / float(limage.size[0]))
    hsize = int(float(limage.size[1]) * float(wpercent))
    limage_2 = limage.resize((wsize,hsize),Image.ANTIALIAS)

    #medir logotipo y definir posicion
    box_2 = mimage.size[0]-limage_2.size[0],mimage.size[1]-limage_2.size[1]

    #Codigo para generar dos nuevas imagenes y poder blendearlas
    newimg1 = Image.new('RGBA', size=(mimage.size[0],mimage.size[1]), color =(0,0,0,0))
    newimg1.paste(mimage, (0,0))

    newimg2 = Image.new('RGBA', size=(mimage.size[0],mimage.size[1]) ,color = (0,0,0,0))
    newimg2.paste(limage_2, box_2)

    # right bottom corner
    print ("Processando Imagen " + mfname)
    hola = Image.alpha_composite(newimg1,newimg2)
    hola.save(outfname)
#********************************************************#

#**************Carpeta**************#

nueva_carpeta = "imagenes con logotipo"
if not os.path.exists(nueva_carpeta):
    os.makedirs(nueva_carpeta)

carpeta = input("Nombre de la Carpeta con imagenes a convertir: ")
tamlogo = input("Tamano de logotipo en porcentaje: ")
carpetas = glob.glob(carpeta+"/*")
logotipo = glob.glob("*.png")

contador = 0
for i in carpetas:
    archivo = carpetas[contador]
    archivo = archivo[archivo.find("/")+1:]
    principio = archivo[:archivo.find(".")]
    output = principio + "_logo.png"
    AddLogo(carpeta+"/"+archivo, logotipo[0] , "imagenes con logotipo/"+output,tamlogo)
    contador += 1
print ("Todos los archivos se convirtieron con exito")

#**************archivo***************#
