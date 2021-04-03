'''
Programador: Luis Angel Rivera Sanchez
Fecha: Cuatro de Abril del 2021
Curso: Compiladores
Avec: Dr. José Luis Quiroz Fabián

Tarea: Multiplicar dos matrices utilizando el lenguaje de programación python.

Desarrollado en:
Equipo: Asus Q550LF
OS: Windows 10
Python: v3.9.2
'''

import numpy as np


class Operador():
    def __init__(self, matA, matB):
    #tamA y tamB son arreglos de dos elementos cada uno que denotan las dimensiones
    #SUMA: Se revisa para ver que tamA == tamB
    #MULT: Se revisa que tamA[1] == tamB[0]
        print("\n\tINICIALIZANDO OPERADOR()")
        self.tamA = dimensiones_matriz(matA)
        self.tamB = dimensiones_matriz(matB)
        
        if self.tamA == self.tamB:
            print("\tSe puede realizar multiplicación y suma de estas dos matrices.")
        elif self.tamA[1] == self.tamB[0]:
            print("\tSe puede realizar multiplicación de estas dos matrices.")
        else:
            print("\tNo se puede realizar ni suma ni multiplicación de estas\n\tmatrices por dimensiones distintas.")
        
        
    def suma(self, matA, matB):
        print("\n\tINICIALIZANDO SUMA DE OPERADOR.")
        dimMatA, dimMatB = self.tamA, self.tamB
        
        #Validación:
        if dimMatA != dimMatB: #matA.shape != matB.shape hace lo mismo!!!
            print("\tNo se pueden sumar.")
            print("\tFINALIZANDO SUMA DE OPERADOR.")
            return
        
        #Verificación:
        print("Sumando matA con matB.")
        matrizC = np.zeros(self.tamA, dtype=int)
        for i in range(dimMatA[0]):
            for j in range(dimMatA[1]):
                matrizC[i][j] = matA[i][j] + matB[i][j]
            
        #Resultados:
        #Si llega a este punto, las tres matrices comparten las mismas dimensiones.
        print("\nLa matriz resultante C=A+B es de %dx%d" % (dimMatA[0], dimMatA[1]))
        print("La matriz resultante C es:\n",format(matrizC))

        print("\n\tFINALIZANDO SUMA DE OPERADOR.")
    
    def mult(self, matA, matB):
        print("\n\tINICIALIZANDO MULT DE OPERADOR.")
        dimMatA, dimMatB = self.tamA, self.tamB
        
        #Validación:
        if dimMatA[1] != dimMatB[0]:
            print("\tNo se pueden multiplicar.")
            print("\tFINALIZANDO MULT DE OPERADOR.")
            return
            
        #Verificación:
        print("Multiplicando matA con matB.")
        matrizC = np.zeros((dimMatA[0], dimMatB[1]), dtype=int)
        for i in range(dimMatA[0]):
            for j in range(dimMatB[1]):
                for k in range(dimMatA[0]):
                    matrizC[i][j] += matA[i][k]*matB[k][j]
                    
        #Resultados:
        print("\nLa matriz resultante C=A*B es de %dx%d" % (dimMatA[0], dimMatB[1]))
        print("La matriz resultante C es:\n",format(matrizC))

        print("\n\tFINALIZANDO MULT DE OPERADOR.")
    

def dimensiones_matriz(matriz):
    dimMatriz = [len(matriz),len(matriz[0])]
    return dimMatriz
	
def main():
    #Estos son los tamaños seleccionados para crear matrices por numpy.
    tam1, tam2, tam3, tam4 = 3,3,3,3
    rangoDeN = 11 #Para generar números aleatorios de 0 a n-1
    
    #Inicializamos matrices (rango, tamaño)
    matA = np.random.randint(11, size=(tam1,tam2))
    matB = np.random.randint(11, size=(tam3,tam4))
    #FIN NUMPY
    
    tamMatA = dimensiones_matriz(matA)
    tamMatB = dimensiones_matriz(matB)

    print("\nLa matriz A es de %dx%d" % (tamMatA[0], tamMatA[1]))
    print("La matriz A es:\n",format(matA))
    
    print("\nLa matriz B es de %dx%d" % (tamMatB[0], tamMatB[1]))
    print("La matriz B es:\n",format(matB))

    #Se llama a las clase Operador
    o = Operador(matA, matB)
    
    #Intentamos hacer las operaciones de sumar y multiplicar
    o.suma(matA,matB)
    o.mult(matA,matB)
    
    print("\nFIN DE PROGRAMA.")
    
    
if __name__ == "__main__":
    print("INICIO DE PROGRAMA.\n")
    main()
    