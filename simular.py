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

    def exportar_txt(self, archivo="reporte_simulacion.txt"):
        if not self.historial:
            print("No hay historial para exportar.")
            return

        with open(archivo, "w") as f:
            for estado in self.historial:
                linea = (
                    f"Paso {estado['paso']} - "
                    f"Activas: {estado['activas']} | "
                    f"Muertas: {estado['muertas']} | "
                    f"Resistentes: {estado['resistentes']}\n"
                )
                f.write(linea)

        print(f"Reporte guardado en {archivo}")