from random import shuffle

# Imprime la baraja de cartas de manera ordenada
def baraja():
    return [(n, p) for n in (['A', 'J', 'Q', 'K']+[str(x) for x in range(2, 11)]) for p in ['♠', '♥', '♣', '♦']]

#Mezcla la baraja
def mezclar(baraja):
    shuffle(baraja)
    return baraja

#sacar cartas
def sacar_cartas(mazo):
    if mazo == []:
        pass
    else:
        sacar_cartas(mazo[1:])
        
#Definir peso de una carta
def valor_carta(carta):
    if carta[0] in ['J', 'Q', 'K']:
        return 10
    elif carta[0] == 'A':
        return 1
    else:
        return int(carta[0])

#Definir el peso de la mano
def valor_mano(mano):
    if mano == []:
        return 0
    return valor_carta(mano[0]) + valor_mano(mano[1:])

#Definir peso de la mano del repartidor
def valor_mano_recargador(mano):
    if valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:
        return valor_mano(mano) + 10
    else:
        return valor_mano(mano)
    
#Definir juego
def jugar(mazo, jugador, repartidor):
    print("Mano del jugador ", " "*5, jugador, " "*6,valor_mano_recargador(jugador))
    print("Mano del repartidor ", " "*2, repartidor, " "*6,valor_mano_recargador(repartidor))
    
    if len(mazo) > 2 and valor_mano_recargador(jugador) < 21 and valor_mano_recargador(repartidor) < 21:
        return jugar(mazo[2:], jugador+[mazo[0]], repartidor+[mazo[1]])
    ganador(jugador, repartidor)
    
def ganador(jugador, repartidor):
    if valor_mano_recargador(jugador) == 21 and valor_mano_recargador(repartidor) < 21:
        print("Gana jugador")
    elif valor_mano_recargador(repartidor) == 21 and valor_mano_recargador(jugador) < 21:
        print("Gana repartidor")
    elif valor_mano_recargador(jugador) > 21:
        print("Pierde jugador, gana repartidor")
    elif valor_mano_recargador(repartidor) > 21:
        print("Gana jugador, pierde repartidor")
    elif 21 - valor_mano_recargador(jugador) < 21 - valor_mano_recargador(repartidor):
        print("Gana jugador")
    elif 21 - valor_mano_recargador(repartidor) < 21 - valor_mano_recargador(jugador):
        print("Gana repartidor")
    elif valor_mano_recargador(jugador) == valor_mano_recargador(repartidor):
        print("Empate")


jugar(mezclar(baraja()), [], [])
