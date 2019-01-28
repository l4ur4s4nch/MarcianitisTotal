print("Ejercicio: leer archivos")

#archivoTexto = open("marcianitos.txt")
#print(archivoTexto)

#contenidoArchivo = archivoTexto.read()
#print(contenidoArchivo)

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
