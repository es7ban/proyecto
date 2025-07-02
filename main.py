import gi
import sys
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
import random
from bacteria import Bacteria
from ambiente import Ambiente
from colonia import Colonia
from simular import Simular
from visualizador import visualizar_grilla

class SimuladorApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.simulador.bacterias")
        self.ambiente = Ambiente()
        self.colonia = Colonia(self.ambiente)
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

        btn_agregar = Gtk.Button(label="Agregar bacteria")
        btn_agregar.connect("clicked", self.on_agregar_bacteria)
        header.pack_start(btn_agregar)

        btn_simular = Gtk.Button(label="Simular paso(s)")
        btn_simular.connect("clicked", self.on_simular_pasos)
        header.pack_start(btn_simular)

        btn_aplicar_ambiente = Gtk.Button(label="Aplicar ambiente")
        btn_aplicar_ambiente.connect("clicked", self.on_aplicar_ambiente)
        header.pack_start(btn_aplicar_ambiente)

        self.imagen = Gtk.Picture()
        self.imagen.set_halign(Gtk.Align.FILL)
        self.imagen.set_valign(Gtk.Align.FILL)
        self.imagen.set_hexpand(True)
        self.imagen.set_vexpand(True)
        main_box.append(self.imagen)

        main_box.append(self.label_estado)

        self.actualizar_imagen()
        self.actualizar_estado()
        self.ventana.present()

    def actualizar_imagen(self):
        pixbuf = visualizar_grilla(self.ambiente)
        self.imagen.set_pixbuf(pixbuf)

    def actualizar_estado(self):
        resumen = self.colonia.reporte_estado()
        self.label_estado.set_label(resumen)

    def on_aplicar_ambiente(self, _):
        self.ambiente.aplicar_ambiente()
        self.actualizar_imagen()
        self.actualizar_estado()

    def on_agregar_bacteria(self, _):
        dialogo = Gtk.Dialog(title="Selecciona tipo de bacteria", transient_for=self.ventana)
        box = dialogo.get_content_area()

        info = Gtk.Label(label="Elige un tipo:")
        box.append(info)

        tipos = {
            "Tipo A (energía 45)": (1, "A", 45, False),
            "Tipo B (energía 35, resistente)": (2, "B", 35, True),
            "Tipo C (energía 20)": (3, "C", 20, False)
        }

        for texto, datos in tipos.items():
            boton = Gtk.Button(label=texto)
            boton.connect("clicked", self.on_tipo_seleccionado, datos, dialogo)
            box.append(boton)

        dialogo.show()

    def on_tipo_seleccionado(self, _, datos, dialogo):
        id_, raza, energia, resistente = datos
        b = Bacteria()
        b.set_id(id_)
        b.set_raza(raza)
        b.set_energia(energia)
        b.set_resistente(resistente)
        b.set_estado("activa")

        vacias = [
            (x, y)
            for x in range(len(self.ambiente.grilla))
            for y in range(len(self.ambiente.grilla[0]))
            if self.ambiente.grilla[x][y] is None
        ]
        if vacias:
            x, y = random.choice(vacias)
            self.ambiente.grilla[x][y] = b
        dialogo.close()
        self.actualizar_imagen()
        self.actualizar_estado()

    def on_simular_pasos(self, _):
        dialogo = Gtk.Dialog(title="Simular pasos", transient_for=self.ventana)
        box = dialogo.get_content_area()

        label = Gtk.Label(label="¿Cuántos pasos quieres simular?")
        box.append(label)

        entrada = Gtk.Entry()
        entrada.set_placeholder_text("Ej: 3")
        box.append(entrada)

        boton = Gtk.Button(label="Simular")
        def ejecutar_simulacion(_):
            try:
                pasos = int(entrada.get_text())
                if pasos > 0:
                    self.simulador.run(pasos)
                    dialogo.close()
                    self.actualizar_imagen()
                    self.actualizar_estado()
            except ValueError:
                print("Número inválido.")

        boton.connect("clicked", ejecutar_simulacion)
        box.append(boton)
        dialogo.show()

if __name__ == "__main__":
    app = SimuladorApp()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)