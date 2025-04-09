diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
try:
    valor = diccionario["clave4"]
except KeyError:
    print("La clave no existe en el diccionario.")
