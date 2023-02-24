import conversion


def solicitar_datos_a_usuario():
    bases_soportadas = ["2", "8", "10", "16", ]
    base_origen = input("""
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal
Elige la base desde donde conviertes: [2, 8, 10, 16]: """)
    if base_origen not in bases_soportadas:
        print("La base que ingresaste no está soportada")
        return
    numero = input(
        ("Vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")
    base_destino = input("""
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal
Elige la base a la que conviertes: [2, 8, 10, 16]: """)
    if base_destino not in bases_soportadas:
        print("La base de destino no está soportada")
        return
    return (base_origen, numero, base_destino)


def obtener_numero_decimal(base_origen, numero):
    if base_origen == "2":
        return conversion.binario_a_decimal(numero)
    elif base_origen == "8":
        return conversion.octal_a_decimal(numero)
    elif base_origen == "10":
        return int(numero)
    elif base_origen == "16":
        return conversion.hexadecimal_a_decimal(numero)


def convertir(numero, base_destino):
    if base_destino == "2":
        return conversion.decimal_a_binario(numero)
    elif base_destino == "8":
        return conversion.decimal_a_octal(numero)
    elif base_destino == "10":
        return int(numero)
    elif base_destino == "16":
        return conversion.decimal_a_hexadecimal(numero)


if __name__ == '__main__':
    datos = solicitar_datos_a_usuario()
   
    if datos:
        base_origen, numero, base_destino = datos
        
        numero_decimal = obtener_numero_decimal(base_origen, numero)
        
        resultado = convertir(numero_decimal , base_destino)
        print(resultado)
       
    )