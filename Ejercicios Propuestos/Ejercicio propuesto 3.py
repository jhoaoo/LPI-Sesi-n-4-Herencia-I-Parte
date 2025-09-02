class ErrorValidacion(ValueError):
    """Excepción personalizada para validaciones de entrada."""
    pass

def pedir_str(msg: str) -> str:
    valido = False
    valor = ""
    while not valido:
        try:
            valor = input(msg).strip()
            if not valor:
                raise ErrorValidacion("El valor no puede estar vacío.")
            valido = True
        except ErrorValidacion as e:
            print(f"Error: {e}")
    return valor

def pedir_int(msg: str, minimo=0) -> int:
    valido = False
    valor = 0
    while not valido:
        try:
            texto = input(msg).strip()
            valor = int(texto)
            if valor < minimo:
                raise ErrorValidacion(f"El número debe ser >= {minimo}.")
            valido = True
        except ValueError:
            print("Error: debe ingresar un número entero.")
        except ErrorValidacion as e:
            print(f"Error: {e}")
    return valor

def pedir_pais_peru(msg: str) -> str:
    valido = False
    valor = ""
    while not valido:
        try:
            valor = input(msg).strip()
            if valor.lower() not in ("peru", "perú"):
                raise ErrorValidacion("Para este ejercicio solo se admite Perú.")
            valor = "Perú"  # normalizamos
            valido = True
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

class Pais:
    def __init__(self, pais):
        self.pais = pais

    def mostrar_pais(self):
        return f"Vivo en {self.pais}."

class RrhhPais(Colaborador, Pais):
    def __init__(self, codigo, nombre, apellido, salario, pais):
        Colaborador.__init__(self, codigo, nombre, apellido, salario)
        Pais.__init__(self, pais)

    def imprimir_resumen(self):
        print(f"Hola, mi nombre es {self.nombre} y mi código es {self.codigo}.")
        print("Trabajo en Recursos Humanos.")
        print(self.mostrar_pais())

print("\n== Registro de Colaborador de RRHH con País ==")
codigo = pedir_int("Ingrese código (entero > 0): ", minimo=1)
nombre = pedir_str("Ingrese nombre: ")
apellido = pedir_str("Ingrese apellido: ")
salario = pedir_int("Ingrese salario (entero >= 0): ", minimo=0)

col = Rrhh(codigo, nombre, apellido, salario)

print("\n-- Datos iniciales --")
col.imprimir_pantalla()

# Incremento con validación
incremento_ok = False
while not incremento_ok:
    try:
        inc = pedir_int("Ingrese incremento de salario (entero >= 0): ", minimo=0)
        col.aumentar_salario(inc)
        incremento_ok = True
    except ErrorValidacion as e:
        print(f"Error: {e}")

# País solo Perú
pais = pedir_pais_peru("Ingrese país de residencia (Perú): ")

print("\n-- Datos luego del incremento --")
col.imprimir_pantalla()

print("\n-- Presentación con país --")
col_pais = RrhhPais(col.codigo, col.nombre, col.apellido, col.salario, pais)
col_pais.imprimir_resumen()