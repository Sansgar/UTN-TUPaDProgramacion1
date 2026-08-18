usuario = "alumno"
clave = "python123"
cantIntentos = 1
login = False

while True:
    print("Sistema de Login Menu Campus")
    usuarioInput = input("Usuario: ")
    claveInput = input("Clave: ")
    if usuario == usuarioInput and clave == claveInput:
        login = True
        break
    elif cantIntentos > 3:
        print(f"Cantidad de intentos superados. Cuenta bloqueada")
        break
    else:
        print(f"Intento {cantIntentos}/3 \nIntente nuevamente")
        cantIntentos += 1

if login:
    while True:
        print("\n1- Estado de inscripcion.\n2- Cambiar Clave\n3- Mensaje Motivacional\n4- Salir")
        opcion = input("Elija una opcion: ")
        if opcion.isdigit():
            if 1 <= int(opcion) <= 4:
                match opcion:
                    case "1":
                        print("Inscripto")
                    case "2":
                        while True:
                            nuevaClave = input("Por favor introducir la nueva clave: ")
                            if len(nuevaClave) < 6:
                                print("La clave debe tener minimo 6 caracteres")
                            else:
                                nuevaClave2 = input("Por favor vuelva a introducir la nueva clave: ")
                                if nuevaClave == nuevaClave2:
                                    print("Clave cambiada correctamente")
                                    break
                                else:
                                    print("Las claves deben coincidir")
                    case "3":
                        print("Es bueno tener una meta hacia la cual dirigirse; pero, al final, lo que importa es el viaje.")
                    case "4":
                        break
            else:
                print("Error: elija una opcion entre 1 y 4.")
        else:
            print("Error: elija un numero.")
        
