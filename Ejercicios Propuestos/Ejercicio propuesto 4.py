class Calculadora_Basica:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    def sumar(self):
        resultado = self.numero1 + self.numero2
        print(f"La suma de numero1({self.numero1}) y numero2({self.numero2}) es {resultado}")
    def restar(self):
        resultado = self.numero1 - self.numero2
        print(f"La resta de numero1({self.numero1}) y numero2({self.numero2}) es {resultado}")
class Calculadora_Avanzada:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    def potenciacion(self):
        try:
            resultado = self.numero1 ** self.numero2
            return resultado
        except Exception as e:
            return f"Error en la potenciacion: {e}"
    def radicacion(self):
        try:
            if self.numero2 == 0:
                return "No se puede calcular raiz con indice cero"
            resultado = self.numero1 ** (1 / self.numero2)
            return resultado
        except Exception as e:
            return f"Error en la radicacion: {e}"
def main():
    try:
        calc_basica = Calculadora_Basica(10, 5)
        calc_basica.sumar()
        calc_basica.restar()
        calc_avanzada = Calculadora_Avanzada(16, 2)
        print("Potenciacion:", calc_avanzada.potenciacion())
        print("Radicacion:", calc_avanzada.radicacion())
    except Exception as e:
        print("Ocurrio un error durante la ejecucion:", str(e))
if __name__ == "__main__":
    main()
