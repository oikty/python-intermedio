valores = input("Ingrese al menos 3 valores separados por espacios: ").split()

mensaje = "Operación exitosa" if len(valores) >= 3 else "Error: Se requieren al menos 3 argumentos"
print(mensaje)