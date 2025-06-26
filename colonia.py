import random
from ambiente import Ambiente

class Colonia():
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.bacterias = []#lista para almacenar bacterias
        self.pasos = None

    def paso(selfm, celda, x, y):
        if celda is None or celda.get_estado() != "activa":
            return

        azar = random.random()

        if azar < 0.4:
            celda.alimentar()
            print(f"Bacteria {celda.get_id()} se alimentó.")
        elif azar < 0.7:
            nueva = celda.dividir()
            print(f"Bacteria {celda.get_id()} se dividió (sin colocar hija aún).")
        elif azar < 0.9:
            celda.mutar()
            print(f"Bacteria {celda.get_id()} mutó.")
        else:
            celda.morir()
            print(f"Bacteria {celda.get_id()} murió.")