import random # importamos libreria random para que la computadora nos de respuestas aleatorias
def elegirGanador(opcionJugador, opcionCompu):
    if opcionJugador == opcionCompu:#utilizamos un if para saber primero si hay un empate entre las opciones
        return "Hay un empate"
    elif (opcionJugador == 'piedra' and opcionCompu == 'tijera') or \
        (opcionJugador == 'tijera' and opcionCompu == 'papel') or \
        (opcionJugador == 'papel' and opcionCompu == 'piedra') :
        return "El jugador ha ganado"
    else:
        return "La Computadora ha ganado"
    

        