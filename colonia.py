from ambiente import Ambiente
import random

class Colonia():
    def __init__(self):
        self.ambiente = Ambiente()#objeto
        self.bacterias = []

    def registrar_bacteria(self, bacteria):
        self.bacterias.append(bacteria)

    def paso(self, celda, x, y):
        if not celda or celda.get_estado() != "activa":
            return None

        # Energía se gasta
        celda.set_energia(celda.get_energia() - 8)#[O]la colonia manipula resta energia a bacteria
        
        if celda.get_energia() <= 0:
            celda.morir()
            self.ambiente.grilla[y][x] = None#[O]Colonia modifica el ambiente al morir
            if celda in self.bacterias:
                self.bacterias.remove(celda)
            return "muerte"

        # Alimentacion
        comida = self.ambiente.nutrientes[y][x] #[O] a datos del ambiente
        energia_ganada = 0

        if comida > 0:
            if comida >= 15:#cuanto come
                energia_gastada = 15
            else:
                energia_ganada = comida #come lo que haya si es menos de 5
        celda.alimentar(energia_ganada)
        self.ambiente.nutrientes[x][y] -= energia_ganada# bacteria reduce los nutrienes

        azar = random.random()
        activas_cerca = 0

        if azar < 0.4:

            if energia_ganada > 0 and random.random() < 0.9:
                celda.alimentar(energia_ganada)
                self.ambiente.nutrientes[y][x] -= energia_ganada

            # Vecino izquierda
             
            if x > 0 and self.ambiente.grilla[y][x - 1]:
                if self.ambiente.grilla[y][x - 1].get_estado() == "activa":
                    activas_cerca += 1

            # Vecino derecha
            if x < 9 and self.ambiente.grilla[y][x + 1]:
                if self.ambiente.grilla[y][x + 1].get_estado() == "activa":
                    activas_cerca += 1

            # Vecino abajo
            if y > 0 and self.ambiente.grilla[y - 1][x]:
                if self.ambiente.grilla[y - 1][x].get_estado() == "activa":
                    activas_cerca += 1

            # Vecino arriba
            if y < 9 and self.ambiente.grilla[y + 1][x]:
                if self.ambiente.grilla[y + 1][x].get_estado() == "activa":
                    activas_cerca += 1

            # Diagonal abajo izquierda
            if x > 0 and y > 0 and self.ambiente.grilla[y - 1][x - 1]:
                if self.ambiente.grilla[y - 1][x - 1].get_estado() == "activa":
                    activas_cerca += 1

            # Diagonal abajo derecha
            if x < 9 and y > 0 and self.ambiente.grilla[y - 1][x + 1]:
                if self.ambiente.grilla[y - 1][x + 1].get_estado() == "activa":
                    activas_cerca += 1

            # Diagonal arriba izquierda
            if x > 0 and y < 9 and self.ambiente.grilla[y + 1][x - 1]:
                if self.ambiente.grilla[y + 1][x - 1].get_estado() == "activa":
                    activas_cerca += 1

            # Diagonal arriba derecha
            if x < 9 and y < 9 and self.ambiente.grilla[y + 1][x + 1]:
                if self.ambiente.grilla[y + 1][x + 1].get_estado() == "activa":
                    activas_cerca += 1

            if activas_cerca >= 4:
                return None  # Demasiada densidad

            hija = celda.dividir()# [O]llama al metodo de la bacteria
            # Derecha
            if x < 9 and self.ambiente.grilla[y][x + 1] is None:
                self.ambiente.grilla[y][x + 1] = hija
                self.bacterias.append(hija)
                return "division"

            # Abajo
            if y < 9 and self.ambiente.grilla[y + 1][x] is None:
                self.ambiente.grilla[y + 1][x] = hija
                self.bacterias.append(hija)
                return "division"

            # Izquierda
            if x > 0 and self.ambiente.grilla[y][x - 1] is None:
                self.ambiente.grilla[y][x - 1] = hija
                self.bacterias.append(hija)
                return "division"

            # Arriba
            if y > 0 and self.ambiente.grilla[y - 1][x] is None:
                self.ambiente.grilla[y - 1][x] = hija
                self.bacterias.append(hija)
                return "division"

            return None  # No encontró espacio

        # Mutación
        elif azar < 0.75:
            if random.random() < 0.05:
                nueva = celda.mutar()
                self.ambiente.grilla[y][x] = nueva
                if celda in self.bacterias:
                    self.bacterias.remove(celda)
                self.bacterias.append(nueva)
                return "mutacion"

        return None

    def reporte_estado(self):#muestra el estado de la bacteria en la intefaz
        activas = 0
        muertas = 0
        resistentes = 0

        for b in self.bacterias:
            if b.get_estado() == "activa":
                activas += 1
                if b.is_resistente():
                    resistentes += 1
            elif b.get_estado() == "muerta":
                muertas += 1

        return (
            f"Estado actual de la colonia:\n\n"
            f"Bacterias activas: {activas}\n"
            f"Bacterias muertas: {muertas}\n"
            f"Resistentes activas: {resistentes}"
        )

    def reporte_estado_actual(self):
        activas = 0
        muertas = 0
        resistentes = 0

        for b in self.bacterias:
            estado = b.get_estado()
            if estado == "activa":
                activas += 1
                if b.is_resistente():
                    resistentes += 1
            elif estado == "muerta":
                muertas += 1

        return {
            "activas": activas,
            "muertas": muertas,
            "resistentes": resistentes
    }


    def exportar_txt(self, narracion, archivo="reporte_colonia.txt"):
        with open(archivo, "w") as f:
            f.write("=== Estado actual de la colonia ===\n\n")
            resumen = self.reporte_estado()
            f.write(resumen + "\n")

            f.write("\n=== Detalle de bacterias activas ===\n\n")
            for b in self.bacterias:
                f.write(
                    f"ID: {b.get_id()} | Raza: {b.get_raza()} | "
                    f"Energía: {b.get_energia()} | "
                    f"Resistente: {b.is_resistente()} | "
                    f"Estado: {b.get_estado()}\n"
                )
            f.write("\n=== Narración de la simulación ===\n\n")
            for linea in narracion:
                f.write(linea + "\n")

        print(f"Reporte guardado en {archivo}")
