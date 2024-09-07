def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos
    modulo4 = anno%4
    modulo400 = anno%400
    modulo100= anno%100
    
    if modulo4 == 0:
        if modulo100 == 0:
            if modulo400 == 0:
                return f"{anno} es bisiesto"
            else:
                 return f"{anno} no es bisiesto"
        else:
            return f"{anno} es bisiesto"
    else:
        return  f"{anno} no es bisiesto"


if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
