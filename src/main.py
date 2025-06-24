from acceder import ejecutar_acceso

def menu_opciones():
    print("1. Acceder")
    print("2. Agregar Alumno")
    print("3. Panel de Administracion")
    print("4. Salir")
    return input("Seleccione una opcion: ")

def menu():
    while True:
        opcion = menu_opciones()
        match opcion: #switch
            case "1":
                ejecutar_acceso()
            case "2":
                pass
            case "3":
                pass
            case "4":
                print("Saliendo del programa ...")
                break
            case _:
                print("Opcion Invalida!")

if __name__ == "__main__":
    menu()