import string
from collections import Counter

def limpiar_texto(texto):
    """Convierte el texto a minúsculas y elimina puntuación."""
    return texto.lower().translate(str.maketrans('', '', string.punctuation))

def contar_palabras(texto):
    """Cuenta la frecuencia de palabras en un texto."""
    palabras = limpiar_texto(texto).split()
    return Counter(palabras), len(palabras)

def contar_lineas_y_parrafos(texto):
    """Cuenta líneas y párrafos en un texto."""
    lineas = texto.splitlines()
    return len(lineas), sum(1 for linea in lineas if linea.strip())

def leer_archivo(nombre_archivo):
    """Lee un archivo y devuelve su contenido."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def procesar_texto(texto):
    """Procesa un texto, mostrando el conteo de palabras, líneas y párrafos."""
    palabras, total_palabras = contar_palabras(texto)
    lineas, parrafos = contar_lineas_y_parrafos(texto)

    print("\nConteo de palabras:")
    print(", ".join(f"{palabra}: {conteo}" for palabra, conteo in palabras.items()))
    print(f"\nTotal de palabras: {total_palabras}")
    print(f"Total de líneas: {lineas}")
    print(f"Total de párrafos: {parrafos}")

def main():
    opcion = input("¿Quieres analizar un archivo o ingresar texto manualmente? (archivo/texto): ").strip().lower()

    if opcion == 'archivo':
        nombre_archivo = input("Ingresa el nombre del archivo: ").strip()
        texto = leer_archivo(nombre_archivo)
        if texto:
            procesar_texto(texto)
    elif opcion == 'texto':
        texto_usuario = input("Ingresa el texto: ").strip()
        procesar_texto(texto_usuario)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()

