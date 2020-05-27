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

#Definir peso de la mano del reparridor
def valor_mano_recargador(mano):
    if valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:
        return valor_mano(mano) + 10
    else:
        return valor_mano(mano)
    0
#Definir juego
def jugar(mazo, jugador, repartidor,juegaJugador):
    print("Mano del jugador ",jugador)
    print("Mano del repartidor ",repartidor)
    if(valor_mano_recargador(jugador)>21 or valor_mano_recargador(repartidor)>21):
        pass
    else:
        #Determinar si el jugador sigue o se plata
        if(juegaJugador==True):
            if(int(input("Presione 1 si desea tomar otra carta o 0 si desea plantarse "))==1):
                if( valor_mano_recargador(repartidor)<15):
                    if(len(mazo)>=2):
                        return jugar(mazo[2:], jugador+[mazo[0]], repartidor+[mazo[1]], True)
                    else:
                        print("No hay cartas Suficientes")
                        pass
                else:
                    return jugar(mazo[1:], jugador+[mazo[0]], repartidor, True)
            else:
                if(valor_mano_recargador(repartidor)<15):
                    if(len(mazo)>=1):
                        return jugar(mazo[1:], jugador, repartidor+[mazo[0]], False)
                    else:
                        print("No hay cartas suficientes")
                        pass
                else:
                    pass
        elif(valor_mano_recargador(repartidor)<15 and juegaJugador==False):
            if(len(mazo)>=1):
                return jugar(mazo[1:], jugador, repartidor+[mazo[0]], False)
            else:
                print("No hay cartas Suficientes")
                pass
        else:
            pass
  
jugar(mezclar(baraja()), [], [], True)
print("Se acabó el juego :v")
