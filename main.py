import random
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from bacteria import Bacteria
from ambiente import Ambiente
from colonia import Colonia
from simular import Simular

# Visualizarde la grilla
def visualizar_grilla(ambiente):
    grilla = ambiente.grilla
    matriz = []
    for fila in grilla:
        fila_numerica = []
        for celda in fila:
            if celda is None:
                fila_numerica.append(0)
            elif celda.get_estado() == "muerta":
                fila_numerica.append(2)
            elif celda.is_resistente():
                fila_numerica.append(3)
            else:
                fila_numerica.append(1)
        matriz.append(fila_numerica)

    fig, ax = plt.subplots(figsize=(6, 6))
    cmap = plt.cm.get_cmap('Set1', 5)
    cax = ax.matshow(matriz, cmap=cmap)

    legend_elements = [
        Patch(facecolor=cmap(1 / 5), label='Bacteria activa'),
        Patch(facecolor=cmap(2 / 5), label='Bacteria muerta'),
        Patch(facecolor=cmap(3 / 5), label='Bacteria resistente'),
        Patch(facecolor=cmap(4 / 5), label='Biofilm (opcional)')
    ]

def crear_bacteria():
    b = Bacteria()
    print("\nSeleccione el tipo de bacteria:")
    print("1  Tipo A (energía 60)")
    print("2  Tipo B (energía 40, resistente)")
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
            print("Opción no válida. Ingrese 1, 2 o 3.")

    b.set_estado("activa")
    return b

def agregar_bacteria(grilla):
    b = crear_bacteria()
    vacias = [(x, y) for x in range(len(grilla)) for y in range(len(grilla[0])) if grilla[x][y] is None]

    if not vacias:
        print("no hay espacio para la bacteria.")
        return

    x, y = random.choice(vacias)
    grilla[x][y] = b
    print(f"Bacteria {b.get_id()} ubicada automáticamente en ({x}, {y})\n")

# mmenu
def menu():
    print("\nMenú Principal")
    print("1 Agregar bacteria")
    print("2 Simular pasos")
    print("3 Visualizar grilla con colores")
    print("4 Activar antibióticos")
    print("5 Desactivar antibióticos")
    print("0 Salir")

    opcion = input("Opcion:")

    if opcion == "1":
        agregar_bacteria(ambiente.grilla)
    elif opcion == "2":
        pasos = int(input("¿Cuántos pasos vas a simular? "))
        simulador.run(pasos)
    elif opcion == "3":
        visualizar_grilla(ambiente)
    elif opcion == "4":
        ambiente.factor_ambiental = 1
        print("antibioticos activado")
    elif opcion == "5":
        ambiente.factor_ambiental = 0
        print("antibioticos desactivado")
    elif opcion == "0":
        return False
    else:
        print("Opción inválida.")
    return True

#iniciar el sistema
ambiente = Ambiente()
colonia = Colonia(ambiente)
simulador = Simular(ambiente, colonia)

if __name__ == "__main__":
    while True:
        if not menu():
            break
