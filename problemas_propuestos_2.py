class Triangulo:
    def inicializar(self,lado1,lado2,lado3,mayor):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
        self.mayor=mayor
    def ingreso(self):
        self.lado1=float(input("Ingrese la medida de lado 1:"))
        self.lado2=float(input("Ingrese la medida del lado 2:"))
        self.lado3=float(input("Ingrese la medida del lado 3:"))
    def buscar_mayor(self):
        self.mayor=max(self.lado1,self.lado2,self.lado3)
        print("El lado mayor es:",self.mayor)
    def validar_equilatero(self):
        if self.lado1==self.lado2 and self.lado2==self.lado3:
            print("El trangulo es equilatero")
        else:
            print("El trangulo no es equilatero")

triangulo=Triangulo()
triangulo.ingreso()
triangulo.buscar_mayor()
triangulo.validar_equilatero()    
        