
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

    def difundir_nutrientes(self):
        for x in range(10):
            for y in range(10):
                if self.nutrientes[x][y] > 5:
                    self.nutrientes[x][y] -= 1
                    if x > 0:
                        self.nutrientes[x - 1][y] += 0.25
                    if x < 9:
                        self.nutrientes[x + 1][y] += 0.25
                    if y > 0:
                        self.nutrientes[x][y - 1] += 0.25
                    if y < 9:
                        self.nutrientes[x][y + 1] += 0.25
