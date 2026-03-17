# Sistema básico de gestión de inventario y pedidos

inventario = []
pedidos = []

# ===============================
# FUNCIONES DE INVENTARIO
# ===============================

def registrar_producto():
    print("\n--- Registrar Producto ---")

    id_producto = input("ID del producto: ")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {
        "id": id_producto,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    print("Producto registrado correctamente.\n")


def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")

    if len(inventario) == 0:
        print("No hay productos registrados.\n")
        return

    for producto in inventario:
        print(producto)

    print()


def editar_producto():
    id_buscar = input("Ingrese ID del producto a editar: ")

    for producto in inventario:

        if producto["id"] == id_buscar:

            producto["nombre"] = input("Nuevo nombre: ")
            producto["precio"] = float(input("Nuevo precio: "))
            producto["cantidad"] = int(input("Nueva cantidad: "))

            print("Producto actualizado.\n")
            return

    print("Producto no encontrado.\n")


def eliminar_producto():

    id_buscar = input("Ingrese ID del producto a eliminar: ")

    for producto in inventario:

        if producto["id"] == id_buscar:

            inventario.remove(producto)

            print("Producto eliminado.\n")
            return

    print("Producto no encontrado.\n")


# ===============================
# FUNCIONES DE PEDIDOS
# ===============================

def registrar_pedido():

    print("\n--- Registrar Pedido ---")

    id_pedido = input("ID del pedido: ")
    cliente = input("Nombre del cliente: ")
    producto = input("Producto solicitado: ")
    cantidad = int(input("Cantidad: "))

    pedido = {
        "id": id_pedido,
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad
    }

    pedidos.append(pedido)

    print("Pedido registrado.\n")


def mostrar_pedidos():

    print("\n--- LISTA DE PEDIDOS ---")

    if len(pedidos) == 0:
        print("No hay pedidos registrados.\n")
        return

    for pedido in pedidos:
        print(pedido)

    print()


def eliminar_pedido():

    id_buscar = input("Ingrese ID del pedido a eliminar: ")

    for pedido in pedidos:

        if pedido["id"] == id_buscar:

            pedidos.remove(pedido)

            print("Pedido eliminado.\n")
            return

    print("Pedido no encontrado.\n")


# ===============================
# MENÚ PRINCIPAL
# ===============================

def menu():

    while True:

        print("====== SISTEMA DE INVENTARIO Y PEDIDOS ======")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Registrar pedido")
        print("6. Mostrar pedidos")
        print("7. Eliminar pedido")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            mostrar_productos()

        elif opcion == "3":
            editar_producto()

        elif opcion == "4":
            eliminar_producto()

        elif opcion == "5":
            registrar_pedido()

        elif opcion == "6":
            mostrar_pedidos()

        elif opcion == "7":
            eliminar_pedido()

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida\n")


menu()