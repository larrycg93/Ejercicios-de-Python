def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "No se puede dividir por cero."
    else:
        return x / y

# menú de la calculadora
def calculadora():
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # solicitud de operacion
    operacion = input("Selecciona la operación (1/2/3/4): ")

    # Solicitar los números
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Por favor, ingresa números válidos.")
        return

    # operación seleccionada
    if operacion == '1':
        print(f"{num1} + {num2} = {sumar(num1, num2)}")
    elif operacion == '2':
        print(f"{num1} - {num2} = {restar(num1, num2)}")
    elif operacion == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif operacion == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")

# ejecucion
calculadora()
