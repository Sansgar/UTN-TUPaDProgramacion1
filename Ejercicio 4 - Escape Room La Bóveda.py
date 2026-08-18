energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
cantForzarCerradura = 0
stepSuma = 0

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
    if cerraduras_abiertas == 3:
        print("Boveda Abierta!\nVICTORIA!")
        break
    elif alarma == True and int(tiempo) <= 3:
        print("Sistema Bloqueado\nDERROTA")
        break
    elif energia <= 0:
        print("Te quedaste sin energia!\nDERROTA")
        break
    elif tiempo <= 0:
        print("Te quedaste sin tiempo\nDERROTA")
        break
    else:
        print(f"Energia: {energia} - Tiempo: {tiempo} - Cerraduras Abiertas: {cerraduras_abiertas} - Alarma Activa {"Verdadero" if alarma else "Falso"} - Codigo: {codigo_parcial}")
        print("\n1- Forzar Cerradura.\n2- Hackear Panel.\n3- Descansar")
        opcion = input(f"{nombre}, por favor elija una opcion: ")
        if opcion.isdigit():
            if 1 <= int(opcion) <= 3:    
                match opcion:
                    case "1":
                        cantForzarCerradura += 1
                        energia -= 20 
                        tiempo -= 2
                        if energia < 40:
                            while True:
                                numero = input("Riesgo de Alarma. Ingreso un numero del 1 al 3: ")
                                if numero.isdigit():
                                    if 1 <= int(numero) <= 3:
                                        if numero == "3":
                                            alarma = True
                                            break
                                        else:
                                            cerraduras_abiertas += 1
                                            break
                                    else:
                                        print("Por favor elegir 1 para Lunes o 2 para Martes")
                                else:
                                    print("Error: por favor ingresar un numero")
                        else:
                            if cantForzarCerradura >= 3:
                                print("Alarma activada. Cerradura trabada")
                                alarma = True
                            else:
                                cerraduras_abiertas += 1
                    case "2":
                        energia -= 10
                        tiempo -= 3
                        cantForzarCerradura = 0
                        for step in range(4):
                            codigo_parcial += chr(65 + step + stepSuma)
                        if len(codigo_parcial) >= 8:
                            cerraduras_abiertas += 1
                        stepSuma += 4
                    case "3":
                        energia += 15
                        tiempo -= 1
                        if alarma:
                            energia -= 10
                        if energia > 100:
                            energia = 100
                        cantForzarCerradura = 0
                        
            else:
                print("Error: elija una opcion entre 1 y 3.")
        else:
            print("Error: elija un numero.")
