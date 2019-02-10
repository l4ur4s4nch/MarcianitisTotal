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

        marcianito1_00_img = pygame.transform.scale(marcianito1_00_img, (64, 64))

        marcianito1_00_w, marcianito1_00_h = marcianito1_00_img.get_rect().size[0], marcianito1_00_img.get_rect().size[1]

    elif elemento_archivo[0] == "marcianito2_00":
        marcianito2_00_img = pygame.image.load(elemento_archivo[1])

        marcianito2_00_img = pygame.transform.scale(marcianito2_00_img, (64, 64))

        marcianito2_00_w, marcianito2_00_h = marcianito2_00_img.get_rect().size[0], marcianito2_00_img.get_rect().size[1]

    elif elemento_archivo[0] == "marcianito3_00":
        marcianito3_00_img = pygame.image.load(elemento_archivo[1])

        marcianito3_00_img = pygame.transform.scale(marcianito3_00_img, (64, 64))

        marcianito3_00_w, marcianito3_00_h = marcianito3_00_img.get_rect().size[0], marcianito3_00_img.get_rect().size[1]

    elif elemento_archivo[0] == "nave_nodriza":
        nave_nodriza_img= pygame.image.load(elemento_archivo[1])

        nave_nodriza_img = pygame.transform.scale(nave_nodriza_img, (64, 64))

        nave_nodriza_w, nave_nodriza_h = nave_nodriza_img.get_rect().size[0], nave_nodriza_img.get_rect().size[1]

    elif elemento_archivo[0] == "fondo":
        fondo_img= pygame.image.load(elemento_archivo[1])

        fondo_img = pygame.transform.scale(fondo_img, (width, height))

    i+=1

end_game = False
nave_x = 0
mar_x = 0
nodriza_x = 0
direccion_mar = 1

#Bucle del juego
while not end_game:

    #Cada cuanto se refesca
    fpsClock.tick(30)

    #Obtener todos los eventos que recibe pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = True

    #Crear una lista con todas las teclas presionadas
    keys = pygame.key.get_pressed()
    #Movimiento de la nave
    if keys[pygame.K_LEFT]:
        nave_x -= 5
        if nave_x <= 0:
            nave_x = 0
    if keys[pygame.K_RIGHT]:
        nave_x += 5
        if nave_x >= width - nave_w:
            nave_x = width - nave_w

    #Movimiento marcianitos
    if mar_x < 0 or mar_x > width - marcianito1_00_w:
        direccion_mar *= -1

    mar_x += 2 * direccion_mar

    #Movimiento nodriza
    nodriza_x += 4 * direccion_mar

    #Cargar el fondo de la pantalla
    screen.blit(fondo_img, (0, 0))


    #Cargar imágenes por pantalla
    screen.blit(nave_nodriza_img, (nodriza_x, 0))
    screen.blit(nave_img, (nave_x, height - nave_h))
    screen.blit(marcianito1_00_img, (mar_x, 120))

    pygame.display.update()

pygame.quit()
