import numpy as num
class demo:

    def addMatrices(self):
        x = [[12, 7, 3],
             [4, 5, 6],
             [7, 8, 9]]
        y = [[5, 8, 1],
             [6, 7, 3],
             [4, 5, 9]]

        z = [[], [], []]

        for i in range(0, 3):
            for j in range(0, 3):
                z[i].append(x[i][j] + y[i][j])

        print("Matrix addition: ",num.array(z))

    def scalarMultiplication(self):
        x = [[12, 7, 3],
             [4, 5, 6],
             [7, 8, 9]]
        y = 9
        z = [[], [], []]

        for i in range(0, 3):
            for j in range(0, 3):
                z[i].append(x[i][j] * y)

        print("Scalar multiplication: ", z)

    def vectorMultiplication(self):
        x = [[5, 1, 3],
             [1, 1, 1],
             [1, 2, 1]]
        y = [1, 2, 3]
        z = []

        value = 0
        for row in range(0, 3):
            sum = 0
            for column in range(0, 3):
                value = y[column] * x[column][row]
                sum = sum + value
            z.append(sum)

        print("Vector Multiplication: Z =", z)

    def matrixMultiplication(self):
        x = [[12, 7, 3],
             [4, 5, 6],
             [7, 8, 9]]

        y = [[5, 8, 1],
             [6, 7, 3],
             [4, 5, 9]]

        z = [[], [], []]
        value = 0
        for xRow in range(0, 3):
            l1 = []
            for yColumn in range(0, 3):
                sum = 0
                for yRow in range(0, 3):
                    value = x[xRow][yRow] * y[yRow][yColumn]
                    sum = sum + value
                l1.append(sum)
            z[xRow].append(l1)

        print("Matrix multiplication : Z = ", z)

    def inverseMatrix(self):


        x = [[12, 7, 3],
             [4, 5, 6],
             [7, 8, 9]]

        print("Inverse of Matrix X: ",num.linalg.inv(x))

    def transposeMatrix(self):
        y = [[5, 8, 1],
             [6, 7, 3],
             [4, 5, 9]]

        z = [[], [], []]

        for i in range(0, 3):
            for j in range(0, 3):
                z[i].append(y[j][i])

        print("Original Matrix: ",y)
        print("Transpose of matrix Y: ",z)

d = demo()

d.addMatrices()
# d.scalarMultiplication()
# d.vectorMultiplication()
# d.matrixMultiplication()
# d.inverseMatrix()
# d.transposeMatrix()