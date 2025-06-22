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
            [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
        ]
        #antibioticos
        self.factor_ambiental = 0 