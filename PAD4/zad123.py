import numpy as np

if __name__ == '__main__':
    # zad 1
    matrix = np.genfromtxt('Zadanie_1.csv', delimiter=';', skip_header=True)

    print("Ilość komórek:")
    print(matrix.size)
    print("Rozmiar macierzy (wiersze, kolumny):")
    print(matrix.shape)
    print("Średnia:")
    print(np.mean(matrix))
    print("Mediana: ")
    print(np.median(matrix))
    print("Wariancja: ")
    print(np.var(matrix))

    matrix2 = np.nan_to_num(matrix)

    print("Średnia: ")
    print(np.mean(matrix2))
    print("Mediana: ")
    print(np.median(matrix2))
    print("Wariancja: ")
    print(np.var(matrix2))

    # zad 2
    # nie można pominąć pierwszego wiersza/headera, są tam wartości
    matrix3 = np.genfromtxt('Zadanie_2.csv', delimiter=';', skip_header=False)

    print("Wektory własne")
    print(np.linalg.eig(matrix3))
    print('Macierz odwrotna:')
    print(np.linalg.inv(matrix3))

    # zad 3
    matrixA = np.genfromtxt('Zadanie_3_macierz_A.csv', delimiter=',', skip_header=False)
    matrixB = np.genfromtxt('Zadanie_3_macierz_B.csv', delimiter=',', skip_header=False)

    print("Macierz podobieństwa:")
    numerator = np.dot(matrixA, matrixB.T)
    A = np.sqrt(np.sum(matrixA ** 2, axis=1))[:, np.newaxis]
    B = np.sqrt(np.sum(matrixB ** 2, axis=1))[np.newaxis, :]
    print(numerator / (A * B))
