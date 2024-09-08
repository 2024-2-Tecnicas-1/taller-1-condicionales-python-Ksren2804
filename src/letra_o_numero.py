def evaluar(caracter):
    # Verificar si es un número
    if '0' <= caracter <= '9':
        return "Es número"
    
    # Verificar si es una letra mayúscula
    elif 'A' <= caracter <= 'Z':
        return "Es letra mayúscula"
    
    # Verificar si es una letra minúscula
    elif 'a' <= caracter <= 'z':
        return "Es letra minúscula"
    # Si no es letra ni número
    else:
        return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)