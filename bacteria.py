import matplotlib.pyplot as plt
from datetime import datetime

class Simular:
    def __init__(self, ambiente, colonia):
        self.ambiente = ambiente
        self.colonia = colonia
        self.historial = []
        self.narracion = []

    def run(self, pasos):
        print(f"Empezamos simulación con {pasos} pasos")

        for i in range(pasos):
            print(f"\n== Paso {i + 1} ==")

            divisiones = 0
            muertes = 0
            mutaciones = 0
            muertes_antibiotico = 0

            for x, fila in enumerate(self.ambiente.grilla):
                for y, celda in enumerate(fila):
                    print(f"Revisando actualmente la celda ({x}, {y})")
                    resultado = self.colonia.paso(celda, x, y)

                    if resultado == "division":
                        divisiones += 1
                    elif resultado == "muerte":
                        muertes += 1
                    elif resultado == "mutacion":
                        mutaciones += 1

            if (i + 1) % 3 == 0:
                muertes_antibiotico = self.ambiente.aplicar_ambiente()

            estado = self.colonia.reporte_estado_dict()
            estado["paso"] = i + 1
            self.historial.append(estado)

            eventos = []
            if divisiones:
                eventos.append(f"{divisiones} divisiones")
            if muertes:
                eventos.append(f"{muertes} muertes por inanición")
            if muertes_antibiotico:
                eventos.append(f"{muertes_antibiotico} muertes por antibiótico")
            if mutaciones:
                eventos.append(f"{mutaciones} mutaciones")

            linea = f"Paso {i + 1}: " + "; ".join(eventos) + "."
            self.narracion.append(linea)

        print("Fin del proceso")
        self.exportar_txt()
        self.graficar_crecimiento()

    def exportar_txt(self, archivo="reporte_simulacion.txt"):
        if not self.historial:
            print("No hay historial para exportar.")
            return

        with open(archivo, "w") as f:
            f.write("=== Reporte de evolución numérica ===\n\n")
            for estado in self.historial:
                linea = (
                    f"Paso {estado['paso']} - "
                    f"Activas: {estado['activas']} | "
                    f"Muertas: {estado['muertas']} | "
                    f"Resistentes: {estado['resistentes']}\n"
                )
                f.write(linea)

            f.write("\n=== Narración de la simulación ===\n\n")
            for linea in self.narracion:
                f.write(linea + "\n")

        print(f"📄 Reporte completo guardado en {archivo}")

    def graficar_crecimiento(self):
        if not self.historial:
            print("No hay datos para graficar.")
            return

        pasos = [h["paso"] for h in self.historial]
        activas = [h["activas"] for h in self.historial]
        resistentes = [h["resistentes"] for h in self.historial]
        porcentaje_resistentes = [
            (r / a) * 100 if a > 0 else 0 for a, r in zip(activas, resistentes)
        ]

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

        ax1.plot(pasos, activas, label="Activas", color="green", marker="o")
        ax1.plot(pasos, resistentes, label="Resistentes", color="orange", marker="x")
        ax1.set_title("Crecimiento bacteriano")
        ax1.set_ylabel("Cantidad")
        ax1.grid(True)
        ax1.legend()

        ax2.plot(pasos, porcentaje_resistentes, label="% Resistentes", color="blue", marker="s")
        ax2.set_title("Proporción de bacterias resistentes")
        ax2.set_xlabel("Paso")
        ax2.set_ylabel("Porcentaje (%)")
        ax2.grid(True)
        ax2.legend()

        plt.tight_layout()

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"grafico_combinado_{timestamp}.png"
        plt.savefig(nombre_archivo)
        print(f"📷 Gráfico combinado guardado como '{nombre_archivo}'")

        plt.show()
