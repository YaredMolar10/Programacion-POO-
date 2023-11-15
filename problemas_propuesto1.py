class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def ingreso(self):
        self.nombre = input("Ingrese su nombre:")
        self.edad = int(input("Ingrese su edad:"))
    def validador_de_edad(self):
        if self.edad >= 18:
            print("Usted es mayor de edad")
        else:
            print("Usted es menor de edad")
    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

persona = Persona()
persona.ingreso()
persona.imprimir_datos()
persona.validador_de_edad()