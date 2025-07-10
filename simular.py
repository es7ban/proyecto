import matplotlib.pyplot as plt
from datetime import datetime

class Simular():
    def __init__(self, ambiente, colonia):
        self.ambiente = ambiente
        self.colonia = colonia
        self.historial = []
        self.narracion = []

    def run(self, pasos):
        print(f"Empezamos simulación con {pasos} pasos")

        for paso in range(pasos):
            print(f"\n== Paso {paso + 1} ==")

            divisiones = 0
            muertes = 0
            mutaciones = 0
            muertes_antibiotico = 0

            filas = len(self.ambiente.grilla)
            columnas = len(self.ambiente.grilla[0])

            for i in range(filas):
                for j in range(columnas):
                    celda = self.ambiente.grilla[i][j]
                    print("Revisando actualmente la celda (", i, ",", j, ")")
                    resultado = self.colonia.paso(celda, i, j)

                    if resultado == "division":
                        divisiones += 1
                    elif resultado == "muerte":
                        muertes += 1
                    elif resultado == "mutacion":
                        mutaciones += 1

            if (paso + 1) % 6 == 0:#aplica el ambiente cada 6 pasos
                muertes_antibiotico = self.ambiente.aplicar_ambiente()

            estado = self.colonia.reporte_estado_actual()
            estado["paso"] = paso + 1
            self.historial.append(estado)#gurada datos numericos
            self.colonia.exportar_txt(self.narracion)


            eventos = []
            if divisiones:
                eventos.append(f"{divisiones} divisiones")
            if muertes:
                eventos.append(f"{muertes} muertes por inanición")
            if muertes_antibiotico:
                eventos.append(f"{muertes_antibiotico} muertes por antibiótico")
            if mutaciones:
                eventos.append(f"{mutaciones} mutaciones")

            linea = f"Paso {paso + 1}: " + "; ".join(eventos) + "."
            self.narracion.append(linea)

        print("Fin del proceso")
        self.graficar_crecimiento()

    def graficar_crecimiento(self):
        if not self.historial:
            print("No hay datos para graficar.")
            return

        pasos = [h["paso"] for h in self.historial]#datos para graficar
        activas = [h["activas"] for h in self.historial]
        resistentes = [h["resistentes"] for h in self.historial]
        porcentaje_resistentes = [
            (r / a) * 100 if a > 0 else 0 for a, r in zip(activas, resistentes)
        ]

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

        ax1.plot(pasos, activas, label="Activas", color="green", marker="o")#grafico
        ax1.plot(pasos, resistentes, label="Resistentes", color="orange", marker="x")
        ax1.set_title("Crecimiento bacteriano")#primer grafico
        ax1.set_ylabel("Cantidad")
        ax1.grid(True)
        ax1.legend()

        ax2.plot(pasos, porcentaje_resistentes, label="% Resistentes", color="blue", marker="s")
        ax2.set_title("Proporción de bacterias resistentes")#segundo grafico
        ax2.set_xlabel("Paso")
        ax2.set_ylabel("Porcentaje (%)")
        ax2.grid(True)
        ax2.legend()

        plt.tight_layout()#genera los datos

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"grafico_combinado_{timestamp}.png"
        plt.savefig(nombre_archivo)
        print(f"Gráfico combinado guardado como '{nombre_archivo}'")

        plt.show()
