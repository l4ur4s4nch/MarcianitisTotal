#print("Ejercicio: leer archivos")

#archivoTexto = open("marcianitos.txt")
#print(archivoTexto)

#contenidoArchivo = archivoTexto.read()
#print(contenidoArchivo)
'''
print(open("marcianitos.txt").read())
contenido = open("marcianitos.txt").readlines()
#print(contenido[1])
print(len(contenido))

i = 0
while i < len(contenido):
    print(contenido[i])
    i+=1

print("Terminado")
print("Ahora si está terminado")
'''
###########################################
#Para usar pygame es necesario instalarlo con anterioridad
import pygame
from pygame.locals import *

#Inicializar pygame, y el contador de fps
pygame.init()
fpsClock = pygame.time.Clock()

#Definir el tamaño de la pantalla y crearla
width = 480
height = 640

screen = pygame.display.set_mode((width, height))

#Leer el archivo txt donde está toda la información de las imágenes
archivo = open("marcianitos.txt")

#Obtener su contenido en filas, y el número de filas
contenido_archivo = archivo.readlines()
longitud_archivo = len(contenido_archivo)

#Crear todos los sprites que se van a usar, e inicializarlos como error, por si
#no se llegan a cargar

nave_img = pygame.image.load("Images_MarcianitisTotal/Error_msg.png")
marcianito1_00_img = pygame.image.load("Images_MarcianitisTotal/Error_msg.png")
marcianito2_00_img = pygame.image.load("Images_MarcianitisTotal/Error_msg.png")
marcianito3_00_img = pygame.image.load("Images_MarcianitisTotal/Error_msg.png")
nave_nodriza_img = pygame.image.load("Images_MarcianitisTotal/Error_msg.png")
fondo_img = pygame.image.load("Images_MarcianitisTotal/Error_msg.png")

i = 0
while i < longitud_archivo:
    #Divide en una lista los textos de cada línea, para permitir cargar los
    #necesarios
    elemento_archivo = contenido_archivo[i].split()

    #Si la primera palabra es ... entonces cargar ...
    #Esto carga las imagenes internamente sin colocarlas en ningún lado
    if elemento_archivo[0] == "nave":
        nave_img = pygame.image.load(elemento_archivo[1])

        nave_img = pygame.transform.scale(nave_img, (64, 64))

        nave_w, nave_h = nave_img.get_rect().size[0], nave_img.get_rect().size[1]

    elif elemento_archivo[0] == "marcianito1_00":
        marcianito1_00_img = pygame.image.load(elemento_archivo[1])

    elif elemento_archivo[0] == "marcianito2_00":
        marcianito2_00_img = pygame.image.load(elemento_archivo[1])

    elif elemento_archivo[0] == "marcianito2_00":
        marcianito2_00_img = pygame.image.load(elemento_archivo[1])

    elif elemento_archivo[0] == "nave_nodriza":
        nave_nodriza_img= pygame.image.load(elemento_archivo[1])

    elif elemento_archivo[0] == "fondo":
        fondo_img= pygame.image.load(elemento_archivo[1])

        fondo_img = pygame.transform.scale(fondo_img, (width, height))

    i+=1

#Bucle del juego
while True:
    #Cargar el fondo de la pantalla
    screen.blit(fondo_img, (0, 0))


    #Cargar imágenes por pantalla
    screen.blit(nave_nodriza_img, (0, 0))
    screen.blit(nave_img, (width - nave_w, height - nave_w))

    pygame.display.update()
    fpsClock.tick(30)
