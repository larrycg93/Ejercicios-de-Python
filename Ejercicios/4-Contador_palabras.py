import string

# Función para contar las palabras en un texto
def contar_palabras(texto):
    texto = texto.lower()  # Convertimos todo el texto a minúsculas
    texto = texto.translate(str.maketrans('', '', string.punctuation))  # Eliminamos puntuación
    palabras = texto.split()
    contador_palabras = {}
    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1
    return contador_palabras, len(palabras)

# Función para contar líneas y párrafos
def contar_lineas_y_parrafos(texto):
    lineas = texto.splitlines()
    num_lineas = len(lineas)
    parrafos = [linea for linea in lineas if linea.strip()]
    num_parrafos = len(parrafos)
    return num_lineas, num_parrafos

# Función para leer archivo y contar palabras, líneas y párrafos
def contar_palabras_en_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            return contar_palabras(texto), contar_lineas_y_parrafos(texto)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return None, None

# Función principal
def main():
    eleccion = input("¿Deseas contar las palabras de un archivo o de un texto ingresado por ti? (archivo/texto): ").strip().lower()

    if eleccion == 'archivo':
        # Pedir al usuario el nombre del archivo
        nombre_archivo = input("Ingresa el nombre del archivo de texto (con su extensión): ").strip()
        resultado_palabras, resultado_lineas_parrafos = contar_palabras_en_archivo(nombre_archivo)
        
        if resultado_palabras:
            palabras, total_palabras = resultado_palabras
            lineas, parrafos = resultado_lineas_parrafos
            print("\nConteo de palabras en el archivo:")
            print(", ".join([f"{palabra}: {conteo}" for palabra, conteo in palabras.items()]))  # Listado en una línea
            print(f"\nTotal de palabras: {total_palabras}")
            print(f"Total de líneas: {lineas}")
            print(f"Total de párrafos: {parrafos}")
                
    elif eleccion == 'texto':
        texto_usuario = input("Ingresa el texto para contar las palabras: ").strip()
        resultado_palabras, resultado_lineas_parrafos = contar_palabras(texto_usuario), contar_lineas_y_parrafos(texto_usuario)
        
        palabras, total_palabras = resultado_palabras
        lineas, parrafos = resultado_lineas_parrafos
        print("\nConteo de palabras ingresadas:")
        print(", ".join([f"{palabra}: {conteo}" for palabra, conteo in palabras.items()]))  # Listado en una línea
        print(f"\nTotal de palabras: {total_palabras}")
        print(f"Total de líneas: {lineas}")
        print(f"Total de párrafos: {parrafos}")
        
    else:
        print("Opción no válida. Por favor, ingresa 'archivo' o 'texto'.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
