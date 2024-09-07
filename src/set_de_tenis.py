def evaluar(num_victorias_a, num_victorias_b):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
#Inválido
    if  (num_victorias_a ==8 and num_victorias_b ==6) or \
        (num_victorias_b ==8 and num_victorias_a ==6) or \
        (num_victorias_a ==7 and num_victorias_b <5) or \
        (num_victorias_b ==7 and num_victorias_a <5) or\
        (num_victorias_a < 0 or num_victorias_b < 0) or\
        (num_victorias_b >7 and num_victorias_a >7):
            return "Inválido"
#Ganó A
    if  (num_victorias_a == 7 and num_victorias_b ==6)or \
        (num_victorias_a >= 6 and num_victorias_a >= num_victorias_b + 2):
            return "Ganó A"

#Ganó B
    if  (num_victorias_b == 7 and num_victorias_a ==6)or \
        (num_victorias_b >= 6 and num_victorias_b >= num_victorias_a + 2):
            return "Ganó B"
    
#Aún no termina
    if  (num_victorias_a ==5 and num_victorias_b == 6) or\
        (num_victorias_b ==5 and num_victorias_a == 6)or \
        (num_victorias_a <6 and num_victorias_b <6) or \
        (num_victorias_a ==6 and num_victorias_b ==6):
            return "Aún no termina"
    

if __name__ == '__main__':
    print("Los juegos ganados por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganados por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
