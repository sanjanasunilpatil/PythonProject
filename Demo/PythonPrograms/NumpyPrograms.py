import numpy as np
import math


class Demo:

    def basic(self):
        a = [12.23, 13.32, 100, 36.32]
        print(np.array(a))    # Converts given a array into 1D array
        print(np.ravel(a))

        print(np.arange(2, 11).reshape(3, 3))    # Creates new 3D array ranging from 2 to 10

        b = np.zeros(10)    # creates array of zeros with total no of elements as 10
        b[6] = 11           # get 6th element and update it to 11
        print(b)

    def reverseArray(self):
        a = np.arange(12, 38)   # creates array from 12 to 37
        print("Original Array", a)
        b = np.flip(a)     # reveres array
        print("Updated array after reversing", b)

    def numpy_5(self):
        total_ones = int(input("Enter number of ones which should be exact square of any number "))
        n = int(math.sqrt(total_ones))
        a = np.ones(total_ones).reshape(n, n)
        print("Original Matrix : \n", a)
        a[1:(n-1)][..., 1:(n-1)] = 0   # 1st [] will select rows , 2nd [] will select columns
        print("Original Matrix : \n", a)

    def addBorder(self):
        total_ones = int(input("Enter number of ones which should be exact square of any number "))
        n = int(math.sqrt(total_ones))
        a = np.ones(total_ones).reshape(n, n)
        print("Original Matrix : \n", a)

        a = np.pad(a, pad_width=1, mode='constant', constant_values=0)  # Here value of pad_with will be added at boundaries of matrix

        print("Original Matrix : \n", a)

    def checkerBoard(self):
        total_zeros = int(input("Enter number of ones which should be exact square of any number "))
        n = int(math.sqrt(total_zeros))
        a = np.zeros(total_zeros).reshape(n, n)
        print("Original Matrix : \n", a)

        for i in range(1, n, 2):       # Traverse through rows
            for j in range(0, n, 2):   # Traverse through Columns
                a[i][j] = 1            # update alternate row and update column particular to row i
                a[j][i] = 1            # update alternate Column and update row particular to column j

        print("Updated Matrix : \n", a)

    def listTupleToArray(self):
        l1 = [1, 2, 3, 4, 5, 6, 7, 8]
        t1 = ([8, 4, 6], [1, 2, 3])
        a1 = np.array(l1)
        print(a1)
        a2 = np.array(t1)
        print(a2)

    def appendValuesToEndOfArray(self):
        a = np.array([10, 20, 30])
        print("Original array: ", a)
        print("Updated array ", np.append(a, [40, 50, 60], axis=0))

    def realImaginaryPart(self):
        a = np.array([1.00000000 + 0.j, 0.70710678 + 0.70710678j], dtype=complex)
        real = a.real
        imaginary = a.imag
        print("Real part", real)
        print("Imaginary part", imaginary)

    def sizeOfArray(self):
        a = np.array([1, 10, 3], dtype=np.int32)
        print("length of array", a.size)
        print("size of single element in bytes", a.itemsize)
        print("size of total element in bytes", a.nbytes)

    def setOperations(self):
        a = np.array([0, 10, 20, 40, 60, 80])
        b = np.array([10, 30, 40, 50, 70])
        print("XOR: ", np.setxor1d(a, b))
        print("Union:", np.union1d(a, b))
        print("Intersection/Common from both arrays: ", np.intersect1d(a, b))
        print("Difference from 1st - 2nd array: ", np.setdiff1d(a, b))
        print("Difference from 2nd - 1st array: ", np.setdiff1d(b, a))

    def equalityOperations(self):
        a = np.array([1, 2])
        b = np.array([4, 5])

        print("Is 1st greater than 2nd array", np.greater(a, b))
        # print("Is 2nd greater than 1st array", np.greater(b, a))
        print("Is 1st greater than equal to 2nd array", np.greater_equal(a, b))
        print("Is 1st equal 2nd array", np.equal(a, b))
        print("Is 1st less than 2nd array", np.less(a, b))
        print("Is 1st less than equal 2nd array", np.less_equal(a, b))

d = Demo()
# d.basic()
# d.reverseArray()
# d.numpy_5()
# d.addBorder()
# d.checkerBoard()
# d.listTupleToArray()
# d.appendValuesToEndOfArray()
# d.realImaginaryPart()
# d.sizeOfArray()
d.setOperations()
# d.equalityOperations()
