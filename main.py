class Asiento:

    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if color in ("rojo", "verde", "amarillo", "negro", "blanco"):
            self.color = color

    
class Auto:

    cantidadcreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos:[Asiento] = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        r = [1 if (a != None) else 0 for a in self.asientos]
        return sum(r)

    def verificarIntegridad(self):
        original = True

        if self.registro != self.motor.registro:
            original = False
        
        for a in self.asientos:
            if a != None:
                if self.registro != a.registro:
                    original = False
                    break
        
        if original:
            return "Auto original"
        else:
            return "Las piezas no son originales"


class Motor:

    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ("electrico", "gasolina"):
            self.tipo = tipo