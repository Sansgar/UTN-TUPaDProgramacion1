
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
    cantProductos = input("Por favor ingresar cantidad de productor a comprar: ")
    if not cantProductos.isdigit():
        print("Error: Ingresar un numero entero positivo por favor")
    else:
        if int(cantProductos) <= 0:
            print("Error: Por favor ingrese una cantidad mayor a 0.")
        else:
            break

total = 0
totalConDesc = 0.00
totalAhorro = 0.00
promedioProductos = 0.00
mensajeFinal = (f"Cliente: {nombre} \nCantidad de Productos: {cantProductos} \n")

for producto in range (int(cantProductos)):
    while True:
        precio = input(f"Por favor ingresar precio del producto {producto+1}: ")
        if not precio.isdigit():
            print("Error: Por favor ingrese un numero valido para el precio.")
        else:
            if int(precio) <= 0:
                print("Error: Por favor ingrese un precio mayor a 0.")
            else:
                break
    while True:
        tieneDesc = input("Este producto tiene descuento? S/N: ")
        if tieneDesc in ['s','S', 'n', 'N']:
            totalAhorro += int(precio) * 0.10
            break
        else:
            print("Por favor ingrese S/N solamente.")
    mensajeFinal += (f"Producto {producto+1} - Precio: {precio} - Descuento S/N: {tieneDesc.lower()} \n")
    total += int(precio)

totalConDesc = total - totalAhorro
promedioProductos = float(total) / float(cantProductos)
mensajeFinal += (f"\nTotal sin descuentos: ${total}\nTotal con descuentos: ${totalConDesc}\nAhorro: ${totalAhorro}\nPromedio por producto: ${promedioProductos:.2f}")
print(mensajeFinal)
