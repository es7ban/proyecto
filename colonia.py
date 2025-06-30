import random
from ambiente import Ambiente

class Colonia():
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.bacterias = []#lista para almacenar bacterias
        self.pasos = None

    def paso(self, celda, x, y):
        if celda is None or celda.get_estado() != "activa":
            return
        
        if self.ambiente.factor_ambiental == 1 and not celda.is_resistente():
            if random.random() < 0.3:
                celda.morir()
                print(f"Bacteria {celda.get_id()} murió por antibiótico en ({x}, {y})")

        if celda.get_estado() != "activa":
            self.ambiente.grilla[x][y] = None
            return


        nutrientes_disponibles = self.ambiente.nutrientes[x][y]
        cantidad_a_absorber = min(10, nutrientes_disponibles)

        azar = random.random()

        if azar < 0.4:
            if cantidad_a_absorber > 0 and random.random() < 0.8:
                celda.alimentar(cantidad_a_absorber)
                self.ambiente.nutrientes[x][y] -= cantidad_a_absorber
                print(f"Bacteria {celda.get_id()} se alimentó con {cantidad_a_absorber} nutrientes en ({x},{y})")
            else:
                print(f"Bacteria {celda.get_id()} no logró alimentarse en ({x},{y})")

        elif azar < 0.7:
            hija = celda.dividir()

            # Intentar colocar en una dirección fija: abajo, derecha, arriba, izquierda
            if x + 1 < len(self.ambiente.grilla) and self.ambiente.grilla[x + 1][y] is None:
                self.ambiente.grilla[x + 1][y] = hija
                print(f"Hija colocada en ({x + 1}, {y})")
            elif y + 1 < len(self.ambiente.grilla[0]) and self.ambiente.grilla[x][y + 1] is None:
                self.ambiente.grilla[x][y + 1] = hija
                print(f"Hija colocada en ({x}, {y + 1})")
            elif x - 1 >= 0 and self.ambiente.grilla[x - 1][y] is None:
                self.ambiente.grilla[x - 1][y] = hija
                print(f"Hija colocada en ({x - 1}, {y})")
            elif y - 1 >= 0 and self.ambiente.grilla[x][y - 1] is None:
                self.ambiente.grilla[x][y - 1] = hija
                print(f"Hija colocada en ({x}, {y - 1})")
            else:
                print("No hubo espacio disponible para colocar la bacteria hija.")

            print(f"Bacteria {celda.get_id()} se dividió.")

        elif azar < 0.9:
            nueva = celda.mutar()
            self.ambiente.grilla[x][y] = nueva
            print(f"Bacteria {nueva.get_id()} mutó en ({x}, {y})")
        
        if celda.get_energia() <= 0:
            celda.morir()
            print(f"Bacteria {celda.get_id()} murió por falta de energía en ({x}, {y})")

       
        if celda.get_estado() == "muerta":
            self.ambiente.grilla[x][y] = None
            print(f"Bacteria eliminada de la grilla en ({x}, {y})")