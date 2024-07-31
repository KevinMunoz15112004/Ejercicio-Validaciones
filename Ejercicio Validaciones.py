import random 
from os import system 

detalleCompra = [[], [], [], [], [], [], [], []]

def menu_opciones():
    print("¿Qué acción desea realizar?")
    print("1. Registrar Pedidos")
    print("2. Mostrar Pedidos")
    print("3. Mostrar detalle de un pedido")
    print("4. Salir del sistema")
    while True:
        try:
            opcion = int(input("Ingrese la opción: "))
            if opcion < 1 or opcion > 4:
                print("Error: por favor elegir una opción del 1 al 4.")
            else:
                return opcion
        except ValueError:
            print("Error: Por favor, ingresar una opción del 1 al 4.")

def ingresar_pedido():
    print("-------Nuevo Pedido--------")
    print("         Ingresar los datos del cliente      ")
    while True:
        nombre_cliente = input("Nombre: ")
        if not nombre_cliente.isalpha() or len(nombre_cliente) < 3 or len(nombre_cliente) > 10:
            print("Error. Por favor, ingresar solo letras entre 3 y 10 caracteres.")
        else:
            break
    while True:
        apellido_cliente = input("Apellido: ")
        if not apellido_cliente.isalpha() or len(apellido_cliente) < 3 or len(apellido_cliente) > 10:
            print("Error. Por favor, ingresar solo letras entre 3 y 10 caracteres.")
        else:
            break
    while True:
        try:
            telefono_cliente = int(input("Teléfono: "))
            if len(str(telefono_cliente)) != 9:
                print("Error: El teléfono debe tener 9 dígitos.")
            else:
                break
        except ValueError:
            print("Error: El teléfono debe ser un número entero.")
   
    print("         Ingresar los datos de la policrush      ")

    while True:
        nombre_crush = input("Nombre: ")
        if not nombre_crush.isalpha() or len(nombre_crush) < 3 or len(nombre_crush) > 10:
            print("Error. Por favor ingresar solo letras entre 3 y 10 caracteres.")
        else:
            break
    while True:
        dependencia = input("Dependencia: ")
        if not dependencia.isalpha() or len(dependencia) < 5 or len(dependencia) > 15:
            print("Error: Ingresar solo letras entre 5 y 15 caracteres.")
        else:
            break
    while True:
        try:
            telefono_crush = int(input("Teléfono: "))
            if len(str(telefono_crush)) != 9:
                print("Error: El teléfono debe tener 9 dígitos.")
            else:
                break
        except ValueError:
            print("Error: El teléfono debe ser un número entero.")
    
    detalleCompra[0].append(nombre_cliente)
    detalleCompra[1].append(apellido_cliente)
    detalleCompra[2].append(telefono_cliente)
    detalleCompra[3].append(nombre_crush)
    detalleCompra[4].append(dependencia)
    detalleCompra[5].append(telefono_crush)
    detalleCompra[6].append(random.randrange(1000, 9999))    
    
    print("         Selección del regalo      ")
    print("1) Opción 1. Poliflor + Polipeluche = $2,50")
    print("2) Opción 2. Poliflor + Policarta = $1,50")
    print("3) Opción 3. Poliflor + Polillavero = $2,00")
    print("4) Opción 4. Poliflor + Polivaso = $2,75")
    print(" ")
    
    while True:
        try:
            opcion = int(input("Ingresa la opción: "))
            if opcion < 1 or opcion > 4:
                print("Error: Por favor, seleccionar una opción entre 1 y 4.")
            else:
                break
        except ValueError:
            print("Error: Por favor, ingresar solo números enteros.")
    
    if opcion == 1:
        detalleCompra[7].append(2.50 + (0.1 * 2.50))
    elif opcion == 2:
        detalleCompra[7].append(1.50 + (0.1 * 1.50))
    elif opcion == 3: 
        detalleCompra[7].append(2.00 + (0.1 * 2.00))
    elif opcion == 4: 
        detalleCompra[7].append(2.75 + (0.1 * 2.75))

    print("------- Pedido registrado con éxito -------")
    print(" ")

def mostrar_pedidos(i):
    print("---------Detalle de la Compra--------")
    print("* Nombre del cliente:", detalleCompra[0][i])
    print("* Apellido del cliente:", detalleCompra[1][i])   
    print("* Teléfono del cliente:", detalleCompra[2][i])
    print("* Nombre de la policrush:", detalleCompra[3][i])
    print("* Dependencia:", detalleCompra[4][i])
    print("* Celular de la policrush:", detalleCompra[5][i])
    print("* Código del pedido:", detalleCompra[6][i])
    print("* Pago final:", detalleCompra[7][i])
    

def buscarPedido():
    while True:
        try:
            codigo = int(input("Ingrese el código: "))
            if len(str(codigo)) != 4:
                print("Error: El código del pedido debe tener 4 dígitos.")
            else:
                break
        except ValueError:
            print("Error: El código debe ser un número entero.")
    
    if codigo in detalleCompra[6]:
        print("Pedido encontrado:")
        dato = detalleCompra[6].index(codigo)
        mostrar_pedidos(dato)
    else:
        print("No existe ese pedido")

def main():
    print("----------- MI POLICRUSH -----------")
    print("            Bienvenido(a)           ")
    opcion = menu_opciones()
    while opcion != 4:
        if opcion == 1:
            ingresar_pedido()
            opcion = menu_opciones()
        elif opcion == 2:
            if len(detalleCompra[0]) == 0:
                print("No existen pedidos registrados")
            else:
                for i in range(len(detalleCompra[0])):
                    mostrar_pedidos(i)
            print()
            opcion = menu_opciones()
        elif opcion == 3:
            print()
            buscarPedido()
            opcion = menu_opciones()

    print("--- Muchas gracias ---")

main()
