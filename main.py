import gi
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

    def do_activate(self):
        ventana = Gtk.ApplicationWindow(application=self)
        ventana.set_title("Simulador Bacterias")
        ventana.set_default_size(400, 300)

        # HeaderBar con boton para ver grilla
        header = Gtk.HeaderBar()
        header.set_title_widget(Gtk.Label(label="Simulador de bacterias"))
        ventana.set_titlebar(header)

        boton_grilla = Gtk.Button(label="Mostrar grilla")
        boton_grilla.connect("clicked", self.on_mostrar_grilla)
        header.pack_end(boton_grilla)

        # Texto de bienvenida
        etiqueta = Gtk.Label(label="Haz clic en 'Mostrar grilla' para ver el entorno.")
        etiqueta.set_margin_top(30)
        etiqueta.set_margin_bottom(30)
        etiqueta.set_wrap(True)
        etiqueta.set_justify(Gtk.Justification.CENTER)
        ventana.set_child(etiqueta)

        ventana.present()

    def on_mostrar_grilla(self, _):
        visualizar_grilla(self.ambiente)

if __name__ == "__main__":
    app = SimuladorApp()
    app.run(None)