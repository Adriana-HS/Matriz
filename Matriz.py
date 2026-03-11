#codigos
class Matriz:
    def __init__(self):
        self.filas = 0
        self.columnas = 0
        self.matriz = []
        self.tiene_inversa = True

    def pedirTamano(self):
        while True:
            try:
                self.filas = int(input("Ingrese el numero de filas: "))
                self.columnas = int(input("Ingrese el numero de columnas: "))
                if self.filas == self.columnas and self.filas > 0:
                    break
                else:
                    print("La matriz debe ser cuadrada y mayor a 0")
            except ValueError:
                print("Ingrese solo numeros enteros")

        self.matriz = [[0 for _ in range(self.columnas * 2)] for _ in range(self.filas)]

    def ingresarDatos(self):
        print("Ingrese datos de la matriz")
        for i in range(self.filas):
            for j in range(self.columnas):
                while True:
                    try:
                        self.matriz[i][j] = float(input())
                        break
                    except ValueError:
                        print("Ingrese un numero valido")

    def CrearMatrizAumentada(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if i == j:
                    self.matriz[i][j + self.columnas] = 1
                else:
                    self.matriz[i][j + self.columnas] = 0

    def MostrarMatrizAumentada(self):
        print("\nMatriz aumentada A|I")
        for i in range(self.filas):
            for j in range(self.columnas * 2):
                print(self.matriz[i][j], end=" ")
            print()

    def GaussJordan(self):
        for i in range(self.filas):
            pivote = self.matriz[i][i]

            if pivote == 0:
                for r in range(i + 1, self.filas):
                    if self.matriz[r][i] != 0:
                        self.matriz[i], self.matriz[r] = self.matriz[r], self.matriz[i]
                        pivote = self.matriz[i][i]
                        break
                else:
                    print("No existe matriz inversa")
                    self.tiene_inversa = False
                    return

            for k in range(self.columnas * 2):
                self.matriz[i][k] /= pivote

            for j in range(self.filas):
                if i != j:
                    aux = self.matriz[j][i]
                    for k in range(self.columnas * 2):
                        self.matriz[j][k] = self.matriz[j][k] - aux * self.matriz[i][k]

    def MostrarInversa(self):
        if not self.tiene_inversa:
            return

        print("\nMatriz inversa:")
        for i in range(self.filas):
            for j in range(self.columnas, self.columnas * 2):
                print(self.matriz[i][j], end=" ")
            print()

    def ConvertirVector(self):
        vec = []
        for i in range(self.filas):
            for j in range(self.columnas, self.columnas * 2):
                vec.append(self.matriz[i][j])
        return vec
        
    def particion(self, arr, izq, der):
        pivote = arr[der]
        menor = izq - 1

        for exp in range(izq, der):
            if arr[exp] <= pivote:
                menor += 1
                arr[menor], arr[exp] = arr[exp], arr[menor]

        menor += 1
        arr[menor], arr[der] = arr[der], arr[menor]

        return menor

    def quickSortRec(self, arr, izq, der):
        if izq < der:
            pi = self.particion(arr, izq, der)
            self.quickSortRec(arr, izq, pi - 1)
            self.quickSortRec(arr, pi + 1, der)


    def MostrarInversaOrdenada(self):
        if not self.tiene_inversa:
            return

        ptr = self.ConvertirVector()
        self.quickSortRec(ptr, 0, len(ptr) - 1)

        print("\nInversa ordenada:")

        k = 0
        for i in range(self.filas):
            for j in range(self.columnas):
                print(ptr[k], end=" ")
                k += 1
            print()



m = Matriz()

m.pedirTamano()
m.ingresarDatos()

m.CrearMatrizAumentada()
m.MostrarMatrizAumentada()

m.GaussJordan()

m.MostrarInversa()
m.MostrarInversaOrdenada()