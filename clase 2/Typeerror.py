numero = 10
cadena = "5"

try:
    resultado = numero + int(cadena)  
    print("Resultado:", resultado)

except TypeError:
    print("Error: Operación no válida entre tipos.")