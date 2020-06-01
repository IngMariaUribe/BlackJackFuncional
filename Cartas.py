"""
Juan David Rosero Torres 20181020071
Maria Fernanda Uribe 20172020110
Yeimer Serrano Navarro 20181020060
"""

from random import shuffle

# Imprime la baraja de cartas de manera ordenada
def baraja():
    return [(n, p) for n in (['A', 'J', 'Q', 'K']+[str(x) for x in range(2, 10)]) for p in ['♠', '♥', '♣', '♦']]

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
    if jugador == [] and repartidor == []:
        jugar(mazo[4:], jugador+[mazo[0]] + [mazo[1]], repartidor+[mazo[2]] + [mazo[3]],True)        
        pass
    else:    
        if len(jugador)==2 and  len(repartidor)==2 and juegaJugador==True:
            print("Así inicia el juego:")
            print("Mano del jugador ",jugador)
            print(oculta(repartidor))
            print (10*"_")

        if(len(jugador)>2):
          print("Mano del jugador ",jugador)

        if(valor_mano_recargador(jugador)>=21 or juegaJugador==False):
              casaplay(mazo,jugador, repartidor,True)          
              pass
        else:
                if(int(input("Presione 1 para tomar carta o 0 si desea plantarse "))==1 and juegaJugador==True):
                  return jugar(mazo[1:], jugador+[mazo[0]], repartidor, True)
                else:
                  return jugar(mazo[:], jugador, repartidor, False)
           
def ganador(jugador, repartidor):
    print ("_"*15)
    if valor_mano_recargador(jugador) == 21 and valor_mano_recargador(repartidor) < 21:
        print("Ganaste")
    elif valor_mano_recargador(repartidor) == 21 and valor_mano_recargador(jugador) < 21:
        print("Gana la casa")
    elif valor_mano_recargador(jugador) > 21:
        print("Gana la casa")
    elif valor_mano_recargador(repartidor) > 21:
        print("Ganaste")
    elif 21 - valor_mano_recargador(jugador) < 21 - valor_mano_recargador(repartidor):
        print("Ganaste")
    elif 21 - valor_mano_recargador(repartidor) < 21 - valor_mano_recargador(jugador):
        print("Gana la casa")
    elif valor_mano_recargador(jugador) == valor_mano_recargador(repartidor):
        print("Gana la casa")

    print ("Asi quedo el juego:")
    print ("Casa: ",repartidor)
    print ("Jugador", jugador)
       
def oculta(mazo):     
    if mazo==[]:
        pass
    else:
        return "Mano casa: ",mazo[0],[(n, p) for n in (['|%|']) for p in range(1,len(mazo))]      

def casaplay(mazo, jugador, casa,estado):

    if(estado==True):
            if(valor_mano_recargador(casa)<21):
              if(valor_mano_recargador(jugador)==21): 
                return casaplay(mazo[1:], jugador, casa+[mazo[0]], True)
              if(valor_mano_recargador(jugador)>21): 
                if( valor_mano_recargador(casa)<=11):            
                    return casaplay(mazo[1:], jugador, casa+[mazo[0]], True)
                else:
                    ganador(jugador, casa)
                    pass
              if(valor_mano_recargador(jugador)<21): 
                if(valor_mano_recargador(casa)<=16):
                    return casaplay(mazo[1:], jugador, casa+[mazo[0]], True)
                else:
                    ganador(jugador, casa)
                    pass
            else:
              ganador(jugador, casa)
              pass

    else:
      print("Algo anda mal...")

    

jugar(mezclar(baraja()), [], [], True)

