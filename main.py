from bacteria import Bacteria
from ambiente import Ambiente

def crear_bacteria():
    b = Bacteria()

    print("\nSeleccione el tipo de bacteria:")
    print("1  Tipo A (energía 60)")
    print("2  Tipo B (energía 40)")
    print("3  Tipo C (energía 20)")

    while True:
        tipo = input("Opción: ")

        if tipo == "1":
            b.set_id(1)
            b.set_raza("A")
            b.set_energia(60)
            b.set_resistente(False)
            break
        elif tipo == "2":
            b.set_id(2)
            b.set_raza("B")
            b.set_energia(40)
            b.set_resistente(True)
            break
        elif tipo == "3":
            b.set_id(3)
            b.set_raza("C")
            b.set_energia(20)
            b.set_resistente(False)
            break
        else:
            print("Opcion no valida, ingrese solo 1, 2 o 3.")

    b.set_estado("activa")
    return b

def agregar_bacteria(grilla):
    b = crear_bacteria()

    x = int(input("Ingrese la posición X (fila): "))
    y = int(input("Ingrese la posición Y (columna): "))

    if grilla[x][y] is None:
        grilla[x][y] = b
        print(f"Bacteria {b.get_id()} ubicada en ({x}, {y})\n")
    else:
        print("Esa celda ya está ocupada.")

def ver_grilla(grilla):
    for fila in grilla:
        linea = ""
        for celda in fila:
            if celda is None:
                linea += "."
            elif celda.get_estado() == "activa":
                linea += "A"
            elif celda.get_estado() == "muerta":
                linea += "M"
            else:
                linea += "?"
        print(linea)
    print()

def menu():
    print("1 Agregar bacteria")
    print("2 Mostrar grilla")
    print("0  Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_bacteria(ambiente.grilla)
    elif opcion == "2":
        ver_grilla(ambiente.grilla)
    elif opcion == "0":
        return False
    else:
        print("Opción invalida.")

    return True

ambiente = Ambiente()   

if __name__ == "__main__":
    while True:
        if not menu():
            break