import random

class Colonia():
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.bacterias = []#lista para almacenar bacterias
        self.pasos = None

    def paso(self, celda, x, y):
        if celda is None or celda.get_estado() != "activa":
            return

        # Gasto basal de energía
        celda.set_energia(celda.get_energia() - 5)
        print(f"Bacteria {celda.get_id()} perdió 5 de energía (ahora tiene {celda.get_energia()})")

        # Muerte por agotamiento de energia
        if celda.get_energia() <= 0:
            celda.morir()
            print(f"Bacteria {celda.get_id()} murió por falta de energía en ({x}, {y})")
            self.ambiente.grilla[x][y] = None
            return

        # Alimentacion
        nutrientes_disponibles = self.ambiente.nutrientes[x][y]
        cantidad_a_absorber = min(10, nutrientes_disponibles)
        azar = random.random()

        if azar < 0.4:
            if cantidad_a_absorber > 0 and random.random() < 0.8:
                celda.alimentar(cantidad_a_absorber)
                self.ambiente.nutrientes[x][y] -= cantidad_a_absorber
                print(f"Bacteria {celda.get_id()} se alimentó con {cantidad_a_absorber} en ({x},{y})")
            else:
                print(f"Bacteria {celda.get_id()} no logró alimentarse en ({x},{y})")

        # Division
        elif azar < 0.7:
            hija = celda.dividir()
            if x + 1 < 10 and self.ambiente.grilla[x + 1][y] is None:
                self.ambiente.grilla[x + 1][y] = hija
                print(f"Hija colocada en ({x + 1}, {y})")
            elif y + 1 < 10 and self.ambiente.grilla[x][y + 1] is None:
                self.ambiente.grilla[x][y + 1] = hija
                print(f"Hija colocada en ({x}, {y + 1})")
            elif x - 1 >= 0 and self.ambiente.grilla[x - 1][y] is None:
                self.ambiente.grilla[x - 1][y] = hija
                print(f"Hija colocada en ({x - 1}, {y})")
            elif y - 1 >= 0 and self.ambiente.grilla[x][y - 1] is None:
                self.ambiente.grilla[x][y - 1] = hija
                print(f"Hija colocada en ({x}, {y - 1})")
            else:
                print("No hubo espacio disponible para la hija.")
            print(f"Bacteria {celda.get_id()} se dividió.")

        # Mutacion
        elif azar < 0.9:
            nueva = celda.mutar()
            self.ambiente.grilla[x][y] = nueva
            celda = nueva
            print(f"Bacteria {nueva.get_id()} mutó en ({x}, {y})")

    def reporte_estado(self):
        activas = 0
        muertas = 0
        resistentes = 0

        for fila in self.ambiente.grilla:
            for celda in fila:
                if celda:
                    if celda.get_estado() == "activa":
                        activas += 1
                        if celda.is_resistente():
                            resistentes += 1
                    elif celda.get_estado() == "muerta":
                        muertas += 1

        print(f"Bacterias activas: {activas}")
        print(f"Bacterias muertas: {muertas}")
        print(f"Resistentes vivas: {resistentes}")