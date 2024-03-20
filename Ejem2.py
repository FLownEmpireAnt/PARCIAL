salpicones = []

def eliminar_fruta(nombre):
    for fruta in salpicones[:]:
        if fruta['nombre'] == nombre:
            confirmacion = input(f"¿Estás seguro de eliminar {nombre}? (s/n): ")
            if confirmacion.lower() == 's':
                salpicones.remove(fruta)
                print(f"{nombre} ha sido eliminado del inventario.")
            else:
                print(f"No se eliminó {nombre}.")
            return
    print(f"No se encontró la fruta {nombre} en el inventario.")

opcion = 100
while opcion != 6:
    print("1. Agregar frutas al inventario")
    print("2. Mostrar costo total del salpicón")
    print("3. Mostrar frutas del salpicón ordenadas por costo (de mayor a menor)")
    print("4. Mostrar la fruta más barata")
    print("5. Eliminar un producto del inventario por nombre")
    print("6. Salir")

    opcion = int(input("Digita una opción: "))

    if opcion == 1:
        n = int(input("Ingrese cantidad de frutas para el salpicón: "))
        for i in range(n):
            fruta = {}
            fruta["id"] = int(input("Digita el id: "))
            fruta["nombre"] = input("Nombre de la fruta: ")
            fruta["precioU"] = int(input("Precio Unitario: "))
            fruta["cantidad"] = int(input("Cantidad: "))
            salpicones.append(fruta)

    elif opcion == 2:
        precioTotal = sum(fruta["precioU"] * fruta["cantidad"] for fruta in salpicones)
        print(f"El costo total del salpicón es ${precioTotal:.2f}")

    elif opcion == 3:
        frutas_ordenadas = sorted(salpicones, key=lambda x: x["precioU"], reverse=True)
        print("Frutas del salpicón ordenadas por costo (de mayor a menor):")
        for fruta in frutas_ordenadas:
            print(f"Nombre: {fruta['nombre']}, Precio Unitario: ${fruta['precioU']}")

    elif opcion == 4:
        fruta_mas_barata = min(salpicones, key=lambda x: x["precioU"])
        print(f"La fruta más barata es: {fruta_mas_barata['nombre']} - Precio Unitario: ${fruta_mas_barata['precioU']}")

    elif opcion == 5:
        nombre_fruta_eliminar = input("Ingrese el nombre de la fruta que desea eliminar: ")
        eliminar_fruta(nombre_fruta_eliminar)

    elif opcion == 6:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, elija una opción válida.")