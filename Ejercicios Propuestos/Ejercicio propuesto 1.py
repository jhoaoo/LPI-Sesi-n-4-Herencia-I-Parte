class ErrorValidacion(ValueError):
    pass

def pedir_str(msg: str) -> str:
    while True:
        try:
            valor = input(msg).strip()
            if not valor:
                raise ErrorValidacion("No puede estar vacío.")
            return valor
        except ErrorValidacion as e:
            print(f"Error: {e}")

def pedir_int(msg: str, minimo=0):
    while True:
        try:
            valor = int(input(msg).strip())
            if valor < minimo:
                raise ErrorValidacion(f"Debe ser >= {minimo}")
            return valor
        except ValueError:
            print("Error: Debe ingresar un número entero.")
        except ErrorValidacion as e:
            print(f"Error: {e}")

def pedir_bool(msg: str) -> bool:
    while True:
        val = input(msg + " (true/false): ").strip().lower()
        if val in ("true", "t", "si", "s", "1"):
            return True
        if val in ("false", "f", "no", "n", "0"):
            return False
        print("Error: responda true o false.")

class Vehiculo:
    def __init__(self, marca, modelo, color, ruedas, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas
        self.cilindrada = cilindrada
        self.arranca = False
        self.acelera = False
        self.frena = False

    def arrancar(self, estado): self.arranca = estado
    def acelerar(self, estado): self.acelera = estado
    def frenar(self, estado):   self.frena = estado

    def mostrar(self):
        print(f"Marca:  {self.marca}")
        print(f"Modelo:  {self.modelo}")
        print(f"Color:  {self.color}")
        print(f"Ruedas:  {self.ruedas}")
        print(f"Cilindrada:  {self.cilindrada}")
        print(f"Arranca:  {self.arranca}")
        print(f"Acelera:  {self.acelera}")
        print(f"Frena:  {self.frena}")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, ruedas, cilindrada):
        super().__init__(marca, modelo, color, ruedas, cilindrada)

class Furgoneta(Vehiculo):
    def __init__(self, marca, modelo, color, ruedas, cilindrada):
        super().__init__(marca, modelo, color, ruedas, cilindrada)

print("\n== Ejercicio 1 ==")
tipo = ""
while tipo not in ("bicicleta", "furgoneta"):
    tipo = pedir_str("Tipo (bicicleta/furgoneta): ").lower()
    if tipo not in ("bicicleta", "furgoneta"):
        print("Error: debe escribir bicicleta o furgoneta.")

marca = pedir_str("Marca: ")
modelo = pedir_str("Modelo: ")
color = pedir_str("Color: ")
ruedas = pedir_int("Número de ruedas: ", minimo=0)
cilindrada = pedir_int("Cilindrada: ", minimo=0)

obj = Bicicleta(marca, modelo, color, ruedas, cilindrada) if tipo == "bicicleta" else Furgoneta(marca, modelo, color, ruedas, cilindrada)

obj.arrancar(pedir_bool("¿Arranca?"))
obj.acelerar(pedir_bool("¿Acelera?"))
obj.frenar(pedir_bool("¿Frena?"))

print("\n-- Resultado --")
obj.mostrar()