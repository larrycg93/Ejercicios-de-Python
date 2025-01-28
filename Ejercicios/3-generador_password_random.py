import random
import string

def generar_contraseña(longitud=12):
    # Definir los caracteres que se usarán en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generar la contraseña de la longitud deseada
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

    return contraseña

# Solicitar la longitud de la contraseña al usuario
longitud = int(input("Introduce la longitud de la contraseña: "))

# Generar y mostrar la contraseña
contraseña = generar_contraseña(longitud)
print(f"Contraseña generada: {contraseña}")
