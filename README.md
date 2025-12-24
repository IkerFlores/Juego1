# Juego1
Para poder realizar el juego de piedra papel o tijera vamos a necesitar una libreria llamada random como lo podemos ver en la primera linea.
Posterior a esto necesitamos que la computadora conozca las reglas del juego para que luego se pueda elegir algun ganador o si es el caso un empate.
en la linea numero 2 vamos a poner la funcion la cual lleva el nombre elegirGanador la cual y definimos las variables que vamos a ocupar
luego mediante un if hay que poner en primera instancia el empate para seguir, para esto elegimos el operador == el cual significa que es igual
despues mediante un elif de por medio vamos a organizarnos y poner en 3 lineas los 3 casos diferentes que existen en el juego
el primero dice que si el jugador tiene por opcion piedra y la computadora tiene por opcion tijera el jugador va a ganar
en el segundo dice que si el jugador tiene por opcion tijera y la computadora tiene por opcion papel el jugador gana
y por ultimo si el jugador tiene por opcion papel y la computadora piedra el jugador de nuevo gana
todo esto dentro del elif para que cuando se termine el or que es el que da varias opciones para este elif se pueda terminar con un return el cual deje un mensaje de ganador
en cada opcion del jugador se escribe con una coma alta en cada lado de la palabra en cuestion para aclarar que es un string (cadena de texto) el que estamos cuestionando, segun lo que elija el jugador al momento de ingresar
se utiliza tambien la palabra and (&&) para validar los dos ingresos de opciones que se tienen
el "or" que se utiliza quiere decir que es un "o" en termino coloquial esto sirve para tener en cuenta que hay mas tipo de opciones que hay que validar, pero esto fuera del parentesis para que no nos de error
por ultimo se termina con un else el cual menciona que si ninguna de las opciones anteriormente escritas se cumple vamos a hacer que nos retorne con el mensaje de "La computadora ha ganado" para entender que el jugador perdio contra la computadora
aun falta la funcion principar la cual establezca el numero de rondas y el marcador que se lleva, para tener la jugada aleatoria por parte de la computadora, y una opcion que el jugador quiera salir del programa

