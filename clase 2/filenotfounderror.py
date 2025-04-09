nombre_archivo = "archivo.txt"

try:
    with open (nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print(f"El archivo no existe." + "Se creara otro")

    try:
        with open (nombre_archivo, "w") as archivo:
            archivo.write("Contenido nuevo")
    except Exception as e :
        print("Error al crear el archivo")
except Exception as e:
    print(f"Error inesperado :{e}")   