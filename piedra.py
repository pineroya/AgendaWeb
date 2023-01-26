import random
# Título generak,,,

print('Bienvenido al juego de Piedra - Papel - Tijera')

# Inicialización de variables descriptivas y contadores...
descripcion =   'Piedra', 'Papel', 'Tijera'
ganadas     =   perdidas    =   0

# Simulación de las tres rondas...
for ronda in range  (1, 4):
    print('Ronda',ronda)

    # Juega el humano...
    humano  = 0
    while   humano  <   1   or humano > 3:
        humano  =   int(input('Ingrese 1 - Piedra, 2 - Papel o 3 - Tijera: '))
        if  humano  <   1   or  humano  >   3:
            print('"Error"\n se pidió entre 1 y 3... cargue de nuevo...')
    print('Usted eligió:', descripcion  [humano - 1])

    # Juega la computadora...
    computadora =   random.randint  (1, 3)
    print('La computadora eligió:', descripcion [computadora - 1 ])

    # Determinar si hubo un ganador y mostrar...
    if humano != computadora:
        if (humano  ==  1   and computadora ==  3) \
                or (humano  ==  3   and computadora ==  2) \
                or (humano  ==  2   and computadora ==  1):
            ganador,    mensaje =   1,  'Punto para el jugador'
        else:
            ganador,    mensaje =   -1, 'Punto para la CPU'
    else:
        ganador,    mensaje =   0,  'Empate'
    print(mensaje)

    #  Llevar la cuenta de los puntos ganados o perdidos...
    if  ganador ==  1:
        ganadas += 1

    elif ganador ==  -1:
        perdidas += 1

# Determinación del resultado final del juego...
if ganadas  >=  2:
    print('Winner! Usted ganó', ganadas, 'a', perdidas)
elif perdidas >= 2:
    print('Loser... Usted perdió, fracasado de mierda', perdidas, 'a', ganadas)
else:
    print('No hay ganador... Jueguen de nuevo idiotas')


# Cierre

print('Fin del programa')

# # Titulo general...
# print('Bienvenido al juego de Piedra - Papel - Tijera')
# # Inicializacion de variables descriptivas y contadores...
# descripcion = 'Piedra', 'Papel', 'Tijera'
# ganadas = perdidas = 0
# # Simulacion de las tres rondas...
# for ronda in range(1, 4):
#  print('\nRonda', ronda)
#  # Juega el humano...
#  humano = 0
#  while humano < 1 or humano > 3:
#     humano = int(input('Ingrese 1 - Piedra, 2 - Papel o 3 - Tijera: '))
#  if humano < 1 or humano > 3:
#     print('Error... se pidió entre 1 y 3... cargue de nuevo...')
#  print('Usted eligio:', descripcion[humano - 1])
#  # Juega la computadora...
#  computadora = random.randint(1, 3)
#  print('La computadora eligió:', descripcion[computadora - 1])
#  # Determinar si hubo un ganador y mostrar...
#  if humano != computadora:
#     if (humano == 1 and computadora == 3) \
#         or (humano == 3 and computadora == 2) \
#         or (humano == 2 and computadora == 1):
#         ganador, mensaje = 1, 'Punto para el humano...'
#  else:
#     ganador, mensaje = -1, 'Punto para la computadora...'
# else:
#     ganador, mensaje = 0, 'Empate en esta ronda...'
# print(mensaje)
#  # Llevar la cuenta de los puntos ganados o perdidos...
# if ganador == 1:
#     ganadas += 1
# elif ganador == -1:
#     perdidas += 1
# # Determinacion del resultado final del juego...
# if ganadas >= 2:
#     print('\nWinner!! Usted ganó', ganadas, 'a', perdidas)
# elif perdidas >= 2:
#     print('Loser... Usted perdió', perdidas, 'a', ganadas)
# else:
#     print('\nNo hay ganador... jueguen de nuevo para decidir')
# # cierre...
# print('Fin del programa')