import random

class Bacteria():
    def __init__(self):
        self.__id = None
        self.__raza = None
        self.__energia = 0
        self.__resistente = False
        self.__estado = "activa"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        try:
            if isinstance(id, int):
                self.__id = id
            else:
                raise TypeError("El tipo de datos no corresponde a Integer")
        except TypeError as error:
            print(f"Error al ingresar id: {error}")

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        try:
            if isinstance(raza, str):
                self.__raza = raza
            else:
                raise TypeError("El tipo de datos no corresponde a string")
        except TypeError as error:
            print(f"error al ingresar raza: {error}")

    def get_energia(self):
        return self.__energia

    def set_energia(self, energia):
        try:
            energia = int(energia)
            if isinstance(energia, int):
                if energia >= 0:
                    self.__energia = energia
                else:
                    raise ValueError("La energia no puede ser negativa")
            else:
                raise TypeError("El tipo de datos no corresponde a Integer")
            
        except TypeError as error:
            print(f"Error al ingresar energía: {error}")
        except ValueError as error:
            print(f"Error al ingresar energía: {error}")

    def is_resistente(self):
        return self.__resistente

    def set_resistente(self, resistente):
        try:
            if isinstance(resistente, bool):
                self.__resistente = resistente
            else:
                raise TypeError("el tipo de datos no corresponde a booleano")
        except TypeError as error:
            print(f"error al ingresar resistencia: {error}")

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        try:
            if isinstance(estado, str):
                self.__estado = estado
            else:
                raise TypeError("El tipo de datos no corresponde a string")
        except TypeError as error:
            print(f"Error al ingresar estado: {error}")

    def alimentar(self, cantidad):
        if self.__estado != "activa":
            return
        self.__energia += cantidad
        
        print(f"Bacteria {self.__id} ganó {cantidad} de energía (total: {self.__energia}).")
        if random.random() < 0.8:  
            self.__energia += cantidad
            print(f"Bacteria {self.__id} se alimento")
        else:
            print(f"Bacteria {self.__id} no se alimento.")
    
    def dividir(self):
        hija = BacteriaResistente() if self.is_resistente() else Bacteria()
        hija.set_id(self.get_id())
        hija.set_raza(self.get_raza())
        hija.set_energia(self.get_energia() // 2)
        self.set_energia(self.get_energia() // 2)
        return hija

    def mutar(self):
        if not self.is_resistente():
            nueva = BacteriaResistente()
            nueva.set_id(self.get_id())
            nueva.set_raza(self.get_raza())
            nueva.set_energia(self.get_energia())
            print(f"Bacteria {self.get_id()} muto")
            return nueva
        else:
             print(f"Bacteria {self.get_id()} ya es resistente.")
        return self
    
    def morir(self):
        self.__estado = "muerta"
        print(f"bacteria {self.__id} ha muerto")

class BacteriaResistente(Bacteria):
    def __init__(self):
        super().__init__()
        self.set_resistente(True)
        self.set_estado("activa")
        self.set_energia(60)  # mas energia que una bacteria comun
    