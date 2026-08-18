lunesT1, lunesT2, lunesT3, lunesT4 = "", "", "", ""
martesT1, martesT2, martesT3 = "", "", ""

while True:
    nombre = input("Por favor ingresar su nombre: ")
    if nombre == '':
        print("Error: el nombre no puede estar vacio.")
    else:
        if not nombre.isalpha():
            print("Error: el nombre solo puede ser letras")
        else:
            break
while True:
    print("\n1- Reservar un turno.\n2- Cancelar turno por nombre.\n3- Ver agenda del dia.\n4- Ver resumen general.\n5- Cerrar sistema.")
    opcion = input("Elija una opcion: ")
    if opcion.isdigit():
        if 1 <= int(opcion) <= 5:    
            match opcion:
                case "1":
                    while True:
                        dia = input("Por favor elegir dia 1 = Lunes - 2 = Martes: ")
                        if opcion.isdigit():
                            if 1 <= int(dia) <= 2:
                                while True:
                                    paciente = input("Por favor ingresar nombre del paciente: ")
                                    if paciente == '':
                                            print("Error: el nombre no puede estar vacio.")
                                    else:
                                        if not nombre.isalpha():
                                            print("Error: el nombre solo puede ser letras")
                                        else:
                                            break
                                break
                            else:
                                print("Por favor elegir 1 para Lunes o 2 para Martes")
                        else:
                            print("Error: por favor ingresar un numero")
                    if dia == "1":
                        if paciente.lower() == lunesT1.lower() or paciente.lower() == lunesT2.lower() or paciente.lower() == lunesT3.lower() or paciente.lower() == lunesT4.lower():
                            print("Paciente ya tiene turno.")
                        else:
                            if lunesT1 == "":
                                lunesT1 = paciente
                            elif lunesT2 == "":
                                lunesT2 = paciente
                            elif lunesT3 == "":
                                lunesT3 = paciente
                            elif lunesT4 == "":
                                lunesT4 = paciente
                            else:
                                print("Todos los turnos ocupados")
                    else:
                        if paciente.lower() == martesT1.lower() or paciente.lower() == martesT2.lower() or paciente.lower() == martesT3.lower():
                            print("Paciente ya tiene turno.")
                        else:
                            if martesT1 == "":
                                martesT1 = paciente
                            elif martesT2 == "":
                                martesT2 = paciente
                            elif martesT3 == "":
                                martesT3 = paciente
                            else:
                                print("Todos los turnos ocupados")
                case "2":
                    while True:
                        dia = input("Por favor elegir dia 1 = Lunes - 2 = Martes: ")
                        if opcion.isdigit():
                            if 1 <= int(dia) <= 2:
                                while True:
                                    paciente = input("Por favor ingresar nombre del paciente: ")
                                    if paciente == '':
                                        print("Error: el nombre no puede estar vacio.")
                                    else:
                                        if not nombre.isalpha():
                                            print("Error: el nombre solo puede ser letras")
                                        else:
                                            break
                                break
                            else:
                                print("Por favor elegir 1 para Lunes o 2 para Martes")
                        else:
                            print("Error: por favor ingresar un numero")
                    if dia == "1":
                        if paciente.lower() == lunesT1.lower():
                            lunesT1 = ""
                        elif paciente.lower() == lunesT2.lower():
                            lunesT2 = ""
                        elif paciente.lower() == lunesT3.lower():
                            lunesT3 = "" 
                        elif paciente.lower() == lunesT4.lower():
                            lunesT4 = ""
                        else:
                            print("Paciente no tiene turno.")
                    else:
                        if paciente.lower() == martesT1.lower():
                            martesT1 = ""
                        elif paciente.lower() == martesT2.lower():
                            martesT2 = ""
                        elif paciente.lower() == martesT3.lower():
                            martesT3 = ""
                        else:
                            print("Paciente no tiene turno.")
                case "3":
                    while True:
                        dia = input("Por favor elegir dia 1 = Lunes - 2 = Martes: ")
                        if opcion.isdigit():
                            if 1 <= int(dia) <= 2:
                                if dia == "1":
                                    print("Turnos Lunes:")
                                    print(f"Turno 1: {"Libre" if lunesT1 == "" else lunesT1}\nTurno 2: {"Libre" if lunesT2 == "" else lunesT2}\nTurno 3: {"Libre" if lunesT3 == "" else lunesT3}\nTurno 4: {"Libre" if lunesT4 == "" else lunesT4}")
                                else:
                                    print("Turnos Martes:")
                                    print(f"Turno 1: {"Libre" if martesT1 == "" else martesT1}\nTurno 2: {"Libre" if martesT2 == "" else martesT2}\nTurno 3: {"Libre" if martesT3 == "" else martesT3}")
                                break
                            else:
                                print("Por favor elegir 1 para Lunes o 2 para Martes")
                        else:
                            print("Error: por favor ingresar un numero")
                case "4":
                    turnosLunes = 0
                    turnosMartes = 0
                    if lunesT1 != "":
                        turnosLunes += 1
                    if lunesT2 != "":
                        turnosLunes += 1
                    if lunesT3 != "":
                        turnosLunes += 1
                    if lunesT4 != "":
                        turnosLunes += 1
                    if martesT1 != "":
                        turnosMartes += 1
                    if martesT2 != "":
                        turnosMartes += 1
                    if martesT3 != "":
                        turnosMartes += 1
                    print("Turnos dia Lunes:")
                    print(f"Turno 1: {"Libre" if lunesT1 == "" else lunesT1}\nTurno 2: {"Libre" if lunesT2 == "" else lunesT2}\nTurno 3: {"Libre" if lunesT3 == "" else lunesT3}\nTurno 4: {"Libre" if lunesT4 == "" else lunesT4}\n")
                    print("Turnos dia Martes:")
                    print(f"Turno 1: {"Libre" if martesT1 == "" else martesT1}\nTurno 2: {"Libre" if martesT2 == "" else martesT2}\nTurno 3: {"Libre" if martesT3 == "" else martesT3}\n")
                    if turnosLunes > turnosMartes:
                        print(f"Lunes dia con mas turnos")
                    elif turnosMartes > turnosLunes:
                        print(f"Martes dia con mas turnos")
                    else:
                        print("Ambos dias con igual cantidad de turnos")
                case "5":
                    break                       
        else:
            print("Error: elija una opcion entre 1 y 5.")
    else:
        print("Error: elija un numero.")
