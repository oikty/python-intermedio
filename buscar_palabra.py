def buscar_palabra(palabra, *args):
    return f"'{palabra}' {'está' if palabra in args else 'no está'} en la lista"

palabras = input("Ingrese palabras separadas por espacios: ").split()
busqueda = input("Ingrese palabra a buscar: ")
print(buscar_palabra(busqueda, *palabras))