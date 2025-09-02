
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    def mostrar_atributos(self):
        print("\nAtributos del Personaje")
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
    def subir_nivel(self):
        print(f"\n¡{self.nombre} ha subido de nivel!")
        self.fuerza += 5
        self.inteligencia += 5
        self.defensa += 5
        self.vida += 10
        print("Los atributos han mejorado.")
    def esta_vivo(self):
        return self.vida > 0
    def morir(self):
        print(f"\n{self.nombre} ha muerto en combate...")
nombre = input("Ingrese el nombre del personaje: ")
fuerza = int(input("Ingrese la fuerza del personaje: "))
inteligencia = int(input("Ingrese la inteligencia del personaje: "))
defensa = int(input("Ingrese la defensa del personaje: "))
vida = int(input("Ingrese la vida del personaje: "))
personaje = Personaje(nombre, fuerza, inteligencia, defensa, vida)
personaje.mostrar_atributos()
personaje.subir_nivel()
personaje.mostrar_atributos()
danio = int(input("\nIngrese el danio recibido: "))
personaje.vida -= danio
if personaje.esta_vivo():
    print(f"\n{personaje.nombre} sigue vivo con {personaje.vida} de vida.")
else:
    personaje.morir()
