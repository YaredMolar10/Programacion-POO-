class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))

    def suma(self):
        resultado = self.valor1 + self.valor2
        print("La suma es:", resultado)

    def resta(self):
        resultado = self.valor1 - self.valor2
        print("La resta es:", resultado)

    def multiplicacion(self):
        resultado = self.valor1 * self.valor2
        print("La multiplicación es:", resultado)

    def division(self):
        if self.valor2 != 0:
            resultado = self.valor1 / self.valor2
            print("La división es:", resultado)
        else:
            print("No se puede dividir por cero")

# Crear una instancia de Operaciones
operaciones = Operaciones()

# Realizar las operaciones e imprimir los resultados
operaciones.suma()
operaciones.resta()
operaciones.multiplicacion()
operaciones.division()
