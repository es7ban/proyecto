import gi
import sys
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
import random
from bacteria import Bacteria
from colonia import Colonia
from simular import Simular
from visualizador import visualizar_grilla

class SimuladorApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.simulador.bacterias")
        self.colonia = Colonia()
        self.ambiente = self.colonia.ambiente
        self.simulador = Simular(self.ambiente, self.colonia)
        self.label_estado = Gtk.Label(label="Estado de la colonia")

    def do_activate(self):
        self.ventana = Gtk.ApplicationWindow(application=self)
        self.ventana.set_title("Simulador Bacteriano")
        self.ventana.set_default_size(900, 1000)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.ventana.set_child(main_box)

        header = Gtk.HeaderBar()
        header.set_title_widget(Gtk.Label(label="Simulador de bacterias"))
        self.ventana.set_titlebar(header)

        boton_agregar = Gtk.Button(label="Agregar bacteria")
        boton_agregar.connect("clicked", self.agregar_bacteria)
        header.pack_start(boton_agregar)

        boton_simular = Gtk.Button(label="Simular paso(s)")
        boton_simular.connect("clicked", self.simular_pasos)
        header.pack_start(boton_simular)
 
        self.imagen = Gtk.Picture()#muestra una imagen estatica
        self.imagen.set_halign(Gtk.Align.FILL)
        self.imagen.set_valign(Gtk.Align.FILL)
        self.imagen.set_hexpand(True)
        self.imagen.set_vexpand(True)
        main_box.append(self.imagen)#aqui se agrega la imagen al contenedor

        main_box.append(self.label_estado)

        self.actualizar_imagen()
        self.actualizar_estado()#reporte
        self.ventana.present()

    def actualizar_imagen(self):
        pixbuf = visualizar_grilla(self.ambiente)
        self.imagen.set_pixbuf(pixbuf)#"muestra la imagen actualizada"

    def actualizar_estado(self):
        resumen = self.colonia.reporte_estado()#reporte
        self.label_estado.set_label(resumen)

    def agregar_bacteria(self, widget):
        dialogo = Gtk.Dialog(title="Selecciona tipo de bacteria", transient_for=self.ventana)
        box = dialogo.get_content_area()

        info = Gtk.Label(label="Elige un tipo:")
        box.append(info)

        tipos = {#parametros de la bacteria
            "Tipo A (energía, 35)": (1, "A", 35, False),
            "Tipo B (energía, 45, resistente)": (2, "B", 45, True),
            "Tipo C (energía, 35)": (3, "C", 35, False)
        }

        for texto, datos in tipos.items():
            boton = Gtk.Button(label=texto)
            boton.connect("clicked", self.tipo_seleccionado, datos, dialogo)
            box.append(boton)

        dialogo.show()

    def tipo_seleccionado(self, widget, datos, dialogo):
        id_, raza, energia, resistente = datos#se llaman los datos seleccionados
        b = Bacteria()#Bacteria
        b.set_id(id_)
        b.set_raza(raza)
        b.set_energia(energia)
        b.set_resistente(resistente)
        b.set_estado("activa")

        posiciones_vacias = []#Guarda las posiciones vacias
        for fila in range(len(self.ambiente.grilla)):
            for columna in range(len(self.ambiente.grilla[0])):#recorre la grilla
                if self.ambiente.grilla[fila][columna] is None:
                    posiciones_vacias.append((fila, columna))

        # Si hay al menos una celda vacía, colocar la bacteria
        if posiciones_vacias:
            fila, columna = random.choice(posiciones_vacias)
            self.ambiente.grilla[fila][columna] = b#coloca la bacteriaa
            self.colonia.registrar_bacteria(b)


        dialogo.close()
        self.actualizar_imagen()
        self.actualizar_estado()

    def simular_pasos(self, widget):
        dialogo = Gtk.Dialog(title="Simular pasos", transient_for=self.ventana)
        box = dialogo.get_content_area()

        label = Gtk.Label(label="¿Cuántos pasos quieres simular?")
        box.append(label)

        entrada = Gtk.Entry()  
        box.append(entrada)

        boton = Gtk.Button(label="Simular")
        
        def ejecutar_simulacion(_):
            try:
                cantidad_de_pasos = int(entrada.get_text())
                if cantidad_de_pasos > 0:
                    self.simulador.run(cantidad_de_pasos)
                    dialogo.close()
                    self.actualizar_imagen()
                    self.actualizar_estado()
            except ValueError:
                print("Numero inválido.")

        boton.connect("clicked", ejecutar_simulacion)
        box.append(boton)
        dialogo.show()

if __name__ == "__main__":
    app = SimuladorApp()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)