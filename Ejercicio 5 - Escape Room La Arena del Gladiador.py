vidaGladiador = 100
vidaEnemigo = 100
pocionesDeVida = 3
dañoAtaquePesado = 15
dañoEnemigo = 12
turnoGladiador = True
contadorTurnos = 1

print("---Bienvenido a la Arena---")
while True:
    nombre = input("Nombe del Gladiador: ")
    if nombre == '':
        print("Error: el nombre no puede estar vacio.")
    else:
        if not nombre.isalpha():
            print("Error: el nombre solo puede ser letras")
        else:
            break

print("--- __ Inicio del Combate __ ---")

while True:
    if vidaGladiador <= 0:
        print("DERROTA. Has caído en combate.")
        break
    if vidaEnemigo <= 0:
        print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
        break
    if turnoGladiador:
        print(f"=== TURNO {contadorTurnos} ===")
        print(f"{nombre}: [HP: {vidaGladiador}] vs Enemigo: [HP: {vidaEnemigo}] -- Pociones: {pocionesDeVida}")
        print("\n1) Ataque Pesado\n2) Ataque Rapido\n3) Curar")
        while True:
            opcion = input(f"{nombre}, por favor elija una opcion: ")
            if opcion.isdigit():
                if 1 <= int(opcion) <= 3:    
                    match opcion:
                        case "1":
                            if vidaEnemigo < 20:
                                dañoCritico = dañoAtaquePesado * 1.5
                                vidaEnemigo -= dañoCritico
                                print(f"¡Atacaste al enemigo por {dañoCritico} puntos de daño!")
                            else:
                                vidaEnemigo -= dañoAtaquePesado
                                print(f"¡Atacaste al enemigo por {dañoAtaquePesado} puntos de daño!")
                        case "2":
                            for ataque in range(3):
                                vidaEnemigo -= 5
                                print("> Golpe conectado por 5 de daño")
                        case "3":
                            if pocionesDeVida > 0:
                                vidaGladiador += 30
                                pocionesDeVida -= 1
                            else:
                                print("¡No quedan pociones!")
                    turnoGladiador = False
                    break
                else:
                    print("Error: elija una opcion entre 1 y 3.")
            else:
                print("Error: elija un numero.")
    else:
        vidaGladiador -= dañoEnemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")
        turnoGladiador = True
        contadorTurnos += 1

