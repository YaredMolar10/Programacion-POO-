class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)
    def validar_nota(self):
        if self.nota>4:
            print("Nota regular")
        else:
            print("Libre")

# Crear instancias de la clase Alumno
alumno1=Alumno()
alumno1.inicializar("Yared",5)
alumno1.imprimir()
alumno1.validar_nota()

alumno2=Alumno()
alumno2.inicializar("Pablo",3)
alumno2.imprimir()
alumno2.validar_nota()
