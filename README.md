# insertarlogo

## Descripcion

Script para automatizar la inserccion de un logo a varias imagenes localizadas en una carpeta especifica y con un logo en formato PNG, dandole un tamano especifico en porcentaje del 1 al 100 segun sea su logotipo.

## Requerimientos 

- Python 3
- [Requiere la libreria Pillow](https://pypi.org/project/Pillow/)


## Install

- Para instalar la librería pillow solo se entra a la terminal y se usa:
    ~~~
    ​$ pip install pillow
    ~~~

## Conocimiento

    1.-Descargar el archivo de python (logos.py).
    2.-Carpeta con las imágenes para insertar el logo.
    3.-El logo en formato .png.


-Abrimos la terminal y nos posicionamos en la carpeta principal y ejecutamos el comando.
    ~~~
    ​$ python3 logos.py
    ~~~

![This is a alt text.](/tuto/step01.png "imagen de ejemplo.")

Al utilizar este comando vamos a ver que suceden 2 cosas.

    1. Nos pide que escribamos el nombre de la carpeta que tiene nuestras imágenes.
    2. la segunda es que automáticamente hace una carpeta “imágenes con logotipo” en el directorio actual

### Escribimos el nombre de la carpeta y damos enter.
### Después nos va a pedir otro dato:
###### Tamaño de logotipo en porcentaje.

###### Tenemos que poner de 1 a 100% de que tamaño queremos que aparezca el logotipo.
###### Elegimos un valor de tamaño y damos Enter.

![This is a alt text.](/tuto/step02.png "imagen de ejemplo.")

Nos va mostrar que esta procesando las imágenes y al final nos indica que todas las imágenes fueron procesadas con éxito.

![This is a alt text.](/tuto/step03.png "imagen de ejemplo.")


Al final tenemos el resultado:

![This is a alt text.](/imagenes/imagen_01.png "imagen de ejemplo") ![This is a alt text.](/tuto/demo.png "imagen de ejemplo.")

