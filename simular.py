class Simular():
    def __init__(self, ambiente, colonia):
        self.ambiente = ambiente
        self.colonia = colonia

    def run(self, pasos):
        print(f"Empezamos simulación con {pasos} pasos")

        for i in range(pasos):
            print(f"\n== Paso {i + 1} ==")

            for x, fila in enumerate(self.ambiente.grilla):
                for y, celda in enumerate(fila):
                    print(f"Revisando actualmente la celda ({x}, {y})")
                    self.colonia.paso(celda, x, y)

            if (i + 1) % 3 == 0:
                self.ambiente.aplicar_ambiente()

        print("Fin del proceso")