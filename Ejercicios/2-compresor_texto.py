def comprimir_texto(texto):
    # Inicializamos una variable para guardar el resultado
    resultado = ""
    # Empezamos a recorrer el texto con un índice
    i = 0

    while i < len(texto):
        # Contamos cuántas veces se repite el carácter actual
        contador = 1
        while i + 1 < len(texto) and texto[i] == texto[i + 1]:
            i += 1
            contador += 1
        # Añadimos el carácter seguido del contador al resultado
        resultado += texto[i] + str(contador)
        i += 1  # Avanzamos al siguiente carácter

    return resultado

# Ejemplo de uso
entrada = input("Introduce el texto a comprimir: ")
salida = comprimir_texto(entrada)
print("Texto comprimido:", salida)
