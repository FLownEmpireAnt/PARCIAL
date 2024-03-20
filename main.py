import random

comics = []

def eliminar_comic(nombre):
    global comics
    for comic in comics:
        if comic["nombrecomic"] == nombre:
            confirmacion = input("¿Está seguro de eliminar este comic? (Sí/No): ").lower()
            if confirmacion == "si":
                comics.remove(comic)
                print("Comic eliminado exitosamente.")
            else:
                print("Operación cancelada.")
            return
    print("El comic no se encontró en la tienda.")

opcion = 100

while opcion != 6:
    print("* Tienda comics *")
    print("------------------------")
    print("1. Registrar Comic")
    print("2. Ver el cartel de comic")
    print("3. Buscar comic")
    print("4. Modificar comic")
    print("5. Eliminar comic")
    print("6. Finalizar")

    try:
        opcion = int(input("Digita una opción: "))

        if opcion == 1:
            comic = {}
            comic["idcomic"] = random.randint(10000, 99999)
            comic["nombrecomic"] = input("Digite el nombre de su comic: ")
            comic["precioUnitarioComic"] = float(input("Digite el precio de su comic: "))
            comic["ubicacionTienda"] = input("Digite la ubicación del comic (A, B, C): ")
            comic["descripcionProducto"] = input("Digite la descripcion de su comic: ")
            comic["casaPertenece"] = input("Digite la casa a la que pertenece: ")
            comic["referencia"] = input("Digite la referencia de su comic: ")
            comic["paisUbicacion"] = input("Digite el pais de origen de su comic: ")
            comic["num_comprado"] = int(input("Digite el numero de compra: "))
            if comic["num_comprado"] > 50:
                print("No queda espacio para más números comprados.")
                continue
            comic["productoGarantia"] = input("¿Tiene garantía? (Sí/No): ").lower() == 'si'
            comics.append(comic)
            print("Comic registrado exitosamente")

        elif opcion == 2:
            print("*** Cartel de Comics ***")
            for comic in comics:
                print(comic)
            print("------------------------")

        elif opcion == 3:
            comicBuscado = input("Digite el comic que quiere encontrar: ")
            encontrado = False 
            for comic in comics:
                if comic["nombrecomic"] == comicBuscado:
                    print("El comic buscado sí está en la tienda. ¡Cómpralo ya!")
                    encontrado = True
                    break
            if not encontrado: 
                print("Aun no contamos con el comic :(")

        elif opcion == 4:
            comicModificado = input("Ingrese el nombre del comic que quiere modificar: ")
            encontrado = False
            for comic in comics:
                if comic["nombrecomic"] == comicModificado:
                    encontrado = True
                    comic["nombrecomic"] = input("Ingrese el nuevo nombre del comic: ")
                    comic["precioUnitarioComic"] = float(input("Ingrese el nuevo precio del comic: "))
                    comic["ubicacionTienda"] = input("Digite la ubicación del comic (A, B, C): ")
                    comic["descripcionProducto"] = input("Ingrese la nueva descripción del comic: ")
                    comic["casaPertenece"] = input("Ingrese la nueva casa a la que pertenece el comic: ")
                    comic["referencia"] = input("Ingrese la nueva referencia del comic: ")
                    comic["paisUbicacion"] = input("Ingrese el nuevo país de origen del comic: ")
                    comic["num_comprado"] = int(input("Digite el numero de compra: "))
                    if comic["num_comprado"] > 50:
                        print("No queda espacio para más números comprados.")
                        continue
                    comic["productoGarantia"] = input("¿Tiene garantía? (Sí/No): ").lower() == 'si'
                    print("Comic modificado exitosamente.")
                    break
            if not encontrado:
                print("El comic no se encontró en la tienda.")

        elif opcion == 5:
            comicEliminar = input("Ingrese el nombre del comic que desea eliminar: ")
            eliminar_comic(comicEliminar)

        elif opcion == 6:
            print("¡Gracias por visitar la tienda de comic, besitos")

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

    except ValueError:
        print("Por favor, introduce un número entero válido.")