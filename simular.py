import matplotlib.pyplot as plt

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

            # Recorremos la grilla y procesamos cada celda
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

            # Cada 3 pasos se aplica antibiótico (si está activo)
            if (i + 1) % 3 == 0:
                muertes_antibiotico = self.ambiente.aplicar_ambiente()

            # Registrar el estado para análisis posterior
            estado = self.colonia.reporte_estado_dict()
            estado["paso"] = i + 1
            self.historial.append(estado)

            # Construir narración del paso
            linea = f"Paso {i+1}: "
            eventos = []
            if divisiones:
                eventos.append(f"{divisiones} divisiones")
            if muertes:
                eventos.append(f"{muertes} muertes por inanición")
            if muertes_antibiotico:
                eventos.append(f"{muertes_antibiotico} muertes por antibiótico")
            if mutaciones:
                eventos.append(f"{mutaciones} mutaciones")
            linea += "; ".join(eventos) + "."
            self.narracion.append(linea)

        print("Fin del proceso")
        self.exportar_txt()

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

        print(f"Reporte completo guardado en {archivo}")

    def graficar_crecimiento(self):
        if not self.historial:
            print("No hay datos para graficar.")
            return

        pasos = [h["paso"] for h in self.historial]
        activas = [h["activas"] for h in self.historial]
        resistentes = [h["resistentes"] for h in self.historial]

        plt.figure(figsize=(8, 5))
        plt.plot(pasos, activas, label="Activas", color="green", marker="o")
        plt.plot(pasos, resistentes, label="Resistentes", color="orange", marker="x")
        plt.title("Crecimiento de la colonia bacteriana")
        plt.xlabel("Paso")
        plt.ylabel("Cantidad de bacterias")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Guardar el gráfico como imagen
        plt.savefig("grafico_crecimiento.png")
        print("Gráfico guardado como 'grafico_crecimiento.png'")

        # Mostrar ventana emergente con el gráfico
        plt.show()