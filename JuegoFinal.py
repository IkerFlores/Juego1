import random # importamos libreria random para que la computadora nos de respuestas aleatorias
def elegirGanador(opcionJugador, opcionCompu):
    if opcionJugador == opcionCompu:#utilizamos un if para saber primero si hay un empate entre las opciones
        return "Hay un empate"
    elif (opcionJugador == 'piedra' and opcionCompu == 'tijera') or \
        (opcionJugador == 'tijera' and opcionCompu == 'papel') or \
        (opcionJugador == 'papel' and opcionCompu == 'piedra') :# en estas 3 lineas se pone las reglas del juego de piedra papel o tijera
        return "El jugador ha ganado"
    else:
        return "La Computadora ha ganado"# estos son mensajes para saber cual es el resultado
    
def jugar():
    opciones = ['piedra', 'papel', 'tijera']# aqui definimos la funcion de jugar la cual nva a ser la principal
    puntuacionJugador = 0#inicializamos en cero las puntuaciones para tener un juego parcial
    puntuacionCompu = 0
    print("Bienvenido al juego de piedra papel o tijera")
    print("El mejor de 3 ganará la partida, escribe salir si no deseas jugar")
    while puntuacionJugador < 2 and puntuacionCompu < 2:# mediante un while se repite si no llegan a dos victorias
        print(f"\nMarcador: Jugador {puntuacionJugador} - {puntuacionCompu} Computadora")#mostramos el marcador en cada ronda
        opcionJugadoor = input ("Elige entre piedra, papel o tijera: ").lower()#pedimos eleccion

        if opcionJugadoor == 'salir':#opcion salir
            print (f"\nTe has rendido. Resultado: Jugador {puntuacionJugador} - {puntuacionCompu} Computadora.")
            return# en esta parte se termina la funcion jugar
        if opcionJugadoor not in opciones:#verficacion de la opcion
            print("Error! Ingresa nuevamente una opcion.")
            continue #vuelve al while
        opcionComputadora = random.choice(opciones)#la opcion de la computadora
        print(f"La Computadora eligió: {opcionComputadora}")#se lee
        resultado = elegirGanador ( opcionJugadoor, opcionComputadora)
        if resultado == "El jugador ha ganado":
            puntuacionJugador += 1#se suma un punto al que gano
            print("Felicidades has ganado esta ronda")
        elif resultado == "La Computadora ha ganado":
            puntuacionCompu +=1
            print("Has perdido esta ronda")
        else:
            print("Hay un empate")#aqui no se suman puntos

    print("\n............................")
    if puntuacionJugador == 2:#se ve ganador de las rondas al mejor de 3
        print(f"Ganaste la partida {puntuacionJugador} a {puntuacionCompu}") 
    else: 
        print(f"La computadora ganó {puntuacionCompu} a {puntuacionJugador}")
    print("............................")   
jugar() # se llama a la funcion para ejecutar
