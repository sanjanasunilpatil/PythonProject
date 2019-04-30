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

        a[1::2, ::2] = 1      # Alternate rows converted into alternate 1s as per alternate column .. Only for alternate row
        a[::2, 1::2] = 1      # Alternate columns converted into alternate 1s as per alternate row .. Only for alternate columns

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

d = Demo()
# d.basic()
# d.reverseArray()
# d.numpy_5()
# d.addBorder()
# d.checkerBoard()
# d.listTupleToArray()
d.appendValuesToEndOfArray()
