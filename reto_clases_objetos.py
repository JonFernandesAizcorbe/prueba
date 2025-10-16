class Libro:
    def __init__(self, titulo, autor, paginas=None, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = disponible

    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            print(f"El libro {self.titulo} ha sido prestado correctamente")
        else:
            print(f"El libro {self.titulo} ya esta prestado")

    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            print(f"El libro {self.titulo} ha sido devuelto correctamente")
        else:
            print(f"El libro {self.titulo} no se ha podido devolver ya estaba en la biblioteca")

    def informacion(self):
        print(f"Titulo: {self.titulo} Autor: {self.autor} Número de paginas: {self.paginas} {"Está diponible" if self.disponible == True else "No está disponible"}")


libro1 = Libro("Luna de pluton", "NI idea", 300, False)
libro2 = Libro("Sin blue protocol", "Frieren", 1, True)

libro1.prestar()
libro2.prestar()

libro1.devolver()
libro2.devolver()

libro1.informacion()
libro2.informacion()
# prueba 