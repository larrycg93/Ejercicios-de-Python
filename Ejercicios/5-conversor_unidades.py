def convertir_longitud(valor, unidad_origen, unidad_destino):
    conversiones_longitud = {
        ("km", "m"): lambda v: v * 1000,
        ("m", "km"): lambda v: v / 1000,
        ("in", "cm"): lambda v: v * 2.54,
        ("cm", "in"): lambda v: v / 2.54,
        ("ft", "m"): lambda v: v * 0.3048,
        ("m", "ft"): lambda v: v / 0.3048,
        ("mi", "km"): lambda v: v * 1.60934,
        ("km", "mi"): lambda v: v / 1.60934,
    }

    if unidad_origen == "ft" and unidad_destino in ["m", "cm"]:
        pies, pulgadas = valor
        metros = pies * 0.3048 + pulgadas * 0.0254
        return metros if unidad_destino == "m" else metros * 100

    return conversiones_longitud.get((unidad_origen, unidad_destino), lambda v: None)(valor)


def convertir_peso(valor, unidad_origen, unidad_destino):
    conversiones_peso = {
        ("kg", "g"): lambda v: v * 1000,
        ("g", "kg"): lambda v: v / 1000,
        ("lb", "kg"): lambda v: v * 0.453592,
        ("kg", "lb"): lambda v: v / 0.453592,
        ("oz", "g"): lambda v: v * 28.3495,
        ("g", "oz"): lambda v: v / 28.3495,
    }

    return conversiones_peso.get((unidad_origen, unidad_destino), lambda v: None)(valor)


def convertir_temperatura(valor, unidad_origen, unidad_destino):
    conversiones_temperatura = {
        ("C", "F"): lambda v: (v * 9 / 5) + 32,
        ("F", "C"): lambda v: (v - 32) * 5 / 9,
        ("C", "K"): lambda v: v + 273.15,
        ("K", "C"): lambda v: v - 273.15,
        ("F", "K"): lambda v: (v - 32) * 5 / 9 + 273.15,
        ("K", "F"): lambda v: (v - 273.15) * 9 / 5 + 32,
    }

    return conversiones_temperatura.get((unidad_origen, unidad_destino), lambda v: None)(valor)


def solicitar_valores():
    try:
        return float(input("Ingresa el valor a convertir: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        return solicitar_valores()


def main():
    print("¡Bienvenido al conversor de unidades!")
    while True:
        print("\nMenú principal:")
        print("1. Longitud")
        print("2. Peso")
        print("3. Temperatura")
        print("4. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\nOpciones de Longitud:")
            print("1. km <-> m")
            print("2. in <-> cm")
            print("3. ft <-> m")
            print("4. mi <-> km")
            print("5. ft & in <-> m o cm")
            sub_opcion = input("Elige una opción: ").strip()

            if sub_opcion in ["1", "2", "3", "4"]:
                valor = solicitar_valores()
                unidad_origen = input("Ingresa la unidad de origen: ").strip().lower()
                unidad_destino = input("Ingresa la unidad de destino: ").strip().lower()
                resultado = convertir_longitud(valor, unidad_origen, unidad_destino)

            elif sub_opcion == "5":
                try:
                    pies, pulgadas = map(float, input("Ingresa pies y pulgadas separados por espacio: ").split())
                    unidad_destino = input("Convertir a (m/cm): ").strip().lower()
                    resultado = convertir_longitud([pies, pulgadas], "ft", unidad_destino)
                except ValueError:
                    print("Error: Ingresa valores válidos.")
                    continue
            else:
                print("Opción inválida.")
                continue

            print(f"Resultado: {resultado} {unidad_destino}" if resultado else "Conversión no válida.")

        elif opcion == "2":
            print("\nOpciones de Peso:")
            print("1. kg <-> g")
            print("2. lb <-> kg")
            print("3. oz <-> g")
            valor = solicitar_valores()
            unidad_origen = input("Ingresa la unidad de origen: ").strip().lower()
            unidad_destino = input("Ingresa la unidad de destino: ").strip().lower()
            resultado = convertir_peso(valor, unidad_origen, unidad_destino)
            print(f"Resultado: {resultado} {unidad_destino}" if resultado else "Conversión no válida.")

        elif opcion == "3":
            print("\nOpciones de Temperatura:")
            print("1. C <-> F")
            print("2. C <-> K")
            print("3. F <-> K")
            valor = solicitar_valores()
            unidad_origen = input("Ingresa la unidad de origen: ").strip().upper()
            unidad_destino = input("Ingresa la unidad de destino: ").strip().upper()
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
            print(f"Resultado: {resultado} {unidad_destino}" if resultado else "Conversión no válida.")

        elif opcion == "4":
            print("¡Gracias por usar el conversor de unidades!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
