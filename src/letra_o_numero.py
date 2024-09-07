nume_y_let = {}

def evaluar():
    global nume_y_let
    # Inicializar el diccionario con letras y números

    # Letras Mayúsculas
    for i in range(65, 91):  # Del 65 al 90 son las letras mayúsculas en ASCII
        nume_y_let[chr(i)] = "Es letra mayúscula"

    # Letras Minúsculas
    for i in range(97, 123):  # Del 97 al 122 son las letras minúsculas en ASCII
        nume_y_let[chr(i)] = "Es letra minúscula"

    # Números
    for i in range(48, 58):  # Del 48 al 57 son los números en ASCII
        nume_y_let[chr(i)] = "Es número"

def determinar_nume_y_let(caracter):
    if caracter in nume_y_let:
        return nume_y_let[caracter]  # Retorna el mensaje basado en el diccionario
    else:
        return f"No es letra ni número"

if __name__ == '__main__':
    evaluar()  # Inicializar el diccionario global
    print("Caracter:", end='')
    caracter = input().strip()
        
    respuesta = determinar_nume_y_let(caracter)
    print(respuesta)