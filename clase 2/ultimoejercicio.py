numero1=""
numero2=""
print("Introduce el primer número: ")
numero1=input()
print("Introduce el segundo número: ")
numero2=input()
try:
    print(int(numero1)/int(numero2))

except ValueError as e:
    print(f"Uno de los numeros son invalidos: {e}")


except ZeroDivisionError:
    print("No se puede dividir entre 0")