def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    
    sum1=a+b
    sum2=b+c
    sum3=c+a

    #Invalido
    if (sum1<c) or (sum2<a) or (sum3<b):   
        return "No es un triángulo válido"
    
    #Equilatero
    if (a==b==c):
        return "El triángulo es equilátero"
    
    #Isósceles
    if (a==b or a==c or b==c):
        return "El triángulo es isósceles"
    
    #Escaleno
    return "El triángulo es escaleno"

    

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
