class Simular():
    def __init__(self, ambiente, colonia):
        self.ambiente = ambiente
        self.colonia = colonia

    def run(self, pasos):
        print(f"Empezamos simulacion con {pasos} pasos")

        for i in range(pasos):
            print(f"\n== Paso {i + 1} ==")
            
            coordenada_x = 0
            for fila in self.ambiente.grilla:
                coordenada_y = 0
                for celda in fila:
                    print(f"Revisando actualmente la celda ({coordenada_x}, {coordenada_y})")
                    self.colonia.paso(celda, coordenada_x, coordenada_y)
                    coordenada_y += 1
                coordenada_x += 1
            
        if (i + 1) % 3 == 0:
            self.ambiente.actualizar_nutrientes()
            print("Nutrientes actualizados")

        print("Fin del proceso")

        print("Fin del proceso")