def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    from time import localtime
    t= localtime()
    estedia = t.tm_mday
    estemes = t.tm_mon
    esteanno = t.tm_year

    #calcular edad
    edadanno= esteanno-anno

    #Saber si este año ya cumplio, primero los meses luego el dia
    if(estemes,estedia)<(mes,dia):
        edadanno -=1
    return f"Usted tiene {edadanno} años";

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
