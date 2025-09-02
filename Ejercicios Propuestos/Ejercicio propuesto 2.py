class ErrorValidacion(ValueError):
    """Excepción personalizada para errores de validación."""
    pass

def pedir_str(msg: str) -> str:
    correcto = False
    valor = ""
    while not correcto:
        try:
            valor = input(msg).strip()
            if not valor:
                raise ErrorValidacion("El valor no puede estar vacío.")
            correcto = True
        except ErrorValidacion as e:
            print(f"Error: {e}")
    return valor

def pedir_int(msg: str, minimo=0) -> int:
    correcto = False
    valor = 0
    while not correcto:
        try:
            valor = int(input(msg).strip())
            if valor < minimo:
                raise ErrorValidacion(f"El número debe ser mayor o igual a {minimo}.")
            correcto = True
        except ValueError:
            print("Error: debe ingresar un número entero.")
        except ErrorValidacion as e:
            print(f"Error: {e}")
    return valor

class Colaborador:
    def __init__(self, codigo, nombre, apellido, salario):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def imprimir_pantalla(self):
        print("==========================")
        print(f"Codigo:  {self.codigo}")
        print(f"Nombre:  {self.nombre}")
        print(f"Apellido:  {self.apellido}")
        print(f"Salario:  {self.salario}")

class Rrhh(Colaborador):
    def __init__(self, codigo, nombre, apellido, salario):
        super().__init__(codigo, nombre, apellido, salario)

    def aumentar_salario(self, incremento):
        if incremento < 0:
            raise ErrorValidacion("El incremento no puede ser negativo.")
        self.salario += incremento

print("\n== Registro de Colaborador ==")
codigo = pedir_int("Ingrese código (entero > 0): ", minimo=1)
nombre = pedir_str("Ingrese nombre: ")
apellido = pedir_str("Ingrese apellido: ")
salario = pedir_int("Ingrese salario (entero >= 0): ", minimo=0)

col = Rrhh(codigo, nombre, apellido, salario)

print("\n-- Datos iniciales --")
col.imprimir_pantalla()

# Pedir incremento de salario
incremento_valido = False
while not incremento_valido:
    try:
        incremento = pedir_int("Ingrese incremento de salario (entero >= 0): ", minimo=0)
        col.aumentar_salario(incremento)
        incremento_valido = True
    except ErrorValidacion as e:
        print(f"Error: {e}")

print("\n-- Datos luego del incremento --")
col.imprimir_pantalla()