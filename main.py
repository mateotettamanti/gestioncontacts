# Función para agregar un contacto a la lista
def agregar_contacto(nombre, telefono, lista_contactos):
    nuevo_contacto = {"Nombre": nombre, "Teléfono": telefono}
    lista_contactos.append(nuevo_contacto)
    print(f"Contacto {nombre} agregado.")

# Función para eliminar un contacto de la lista
def eliminar_contacto(nombre, lista_contactos):
    for contacto in lista_contactos:
        if contacto["Nombre"] == nombre:
            lista_contactos.remove(contacto)
            print(f"Contacto {nombre} eliminado.")
            return
    print(f"Contacto {nombre} no encontrado.")

# Función para buscar un contacto en la lista
def buscar_contacto(nombre, lista_contactos):
    for contacto in lista_contactos:
        if contacto["Nombre"] == nombre:
            print("Contacto encontrado:")
            print(contacto)
            return
    print(f"Contacto {nombre} no encontrado.")

# Función para mostrar la lista de contactos
def mostrar_contactos(lista_contactos):
    if not lista_contactos:
        print("La lista de contactos está vacía.")
    else:
        print("Lista de contactos:")
        for contacto in lista_contactos:
            print(contacto)

# Lista para almacenar los contactos
lista_de_contactos = []

# Menú principal
while True:
    print("\n*** GESTIÓN DE CONTACTOS ***")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Mostrar contactos")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        agregar_contacto(nombre, telefono, lista_de_contactos)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        eliminar_contacto(nombre, lista_de_contactos)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        buscar_contacto(nombre, lista_de_contactos)
    elif opcion == "4":
        mostrar_contactos(lista_de_contactos)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
