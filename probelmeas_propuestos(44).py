class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def imprimir_perimetro(self):
        perimetro = self.lado * 4
        print("El perímetro del cuadrado es:", perimetro)

    def imprimir_superficie(self):
        superficie = self.lado ** 2
        print("La superficie del cuadrado es:", superficie)

# Crear una instancia de Cuadrado con un lado de 5
cuadrado = Cuadrado(5)

# Imprimir el perímetro y la superficie
cuadrado.imprimir_perimetro()
cuadrado.imprimir_superficie()
