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
        self.factor_ambiental = 1
    
    def actualizar_nutrientes(self, cantidad=5, max_nutrientes=50):
        for x in range(10):
            for y in range(10):
                self.nutrientes[x][y] = min(self.nutrientes[x][y] + cantidad, max_nutrientes)

    def difundir_nutrientes(self):
        nueva_matriz = [fila[:] for fila in self.nutrientes]
        for x in range(10):
            for y in range(10):
                if self.nutrientes[x][y] > 5:
                    nueva_matriz[x][y] -= 1
                    if x > 0:
                        nueva_matriz[x - 1][y] += 0.25
                    if x < 9:
                        nueva_matriz[x + 1][y] += 0.25
                    if y > 0:
                        nueva_matriz[x][y - 1] += 0.25
                    if y < 9:
                        nueva_matriz[x][y + 1] += 0.25
        self.nutrientes = nueva_matriz

    def aplicar_ambiente(self):
        eliminadas = 0
        self.actualizar_nutrientes()
        self.difundir_nutrientes()

        if self.factor_ambiental == 1:
            for x in range(10):
                for y in range(10):
                    celda = self.grilla[x][y]
                    if celda and celda.get_estado() == "activa" and not celda.is_resistente():
                        celda.morir()
                        self.grilla[x][y] = None
                        eliminadas += 1
                        print(f"Bacteria {celda.get_id()} eliminada por antibiótico en ({x}, {y})")
        return eliminadas