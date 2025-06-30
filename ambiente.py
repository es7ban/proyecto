
class Ambiente():
    def __init__(self):
        self.grilla = [
            [None, None, None, None, None, None, None, None, None, None],  
            [None, None, None, None, None, None, None, None, None, None],  
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
        ]
        self.nutrientes = [
            [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50 ,50 ,50 ,50, 50, 50],
        ]
        # antibioticos
        self.factor_ambiental = 0 
    
    def actualizar_nutrientes(self, cantidad=5, max_nutrientes=50):
        for x in range(len(self.nutrientes)):
            for y in range(len(self.nutrientes[0])):
                self.nutrientes[x][y] = min(self.nutrientes[x][y] + cantidad, max_nutrientes)

class BacteriaResistente(Bacteria):
    def __init__(self):
        super().__init__()
        self.set_resistente(True)
        self.set_estado("activa")