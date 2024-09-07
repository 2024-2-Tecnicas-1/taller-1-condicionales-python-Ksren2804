def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Division
    cociente = dividendo//divisor
    residuo = dividendo%divisor
    if (divisor==0):
        return "Operación Invalida"
    
    if (residuo == 0):
        respuestaexa = "La división es exacta. \n" \
            "Cociente: " + str(cociente) + "\n" \
            "Residuo: " + str(residuo)
        return respuestaexa
    
    if (cociente > 0 and residuo > 0):    
        respuestanoexa = "La división no es exacta. \n" \
            "Cociente: " + str(cociente) + "\n" \
            "Residuo: " + str(residuo)
        return respuestanoexa

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
