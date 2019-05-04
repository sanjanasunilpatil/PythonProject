from matplotlib import pyplot as plt
from os import path
import pandas as pd
import numpy as np

class Demo:

    # This function draws simple line from x and Y co-ordinates
    def drawLine(self):
        x = [2, 3]
        y = [3, 5]

        plt.plot(x, y)
        plt.title("Sample Line")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")

        plt.show()

    # This function draws sample line and input for x co-ordinates and y co-ordinates will come from input file
    def drawLineInputFile(self):
        basepath = path.dirname(__file__)             # Gives current path
        filepath = path.abspath(path.join(basepath, "..", "inputFiles/test.txt"))

        file = open(filepath, "r")

        content = file.read()
        content = content.split('\n')

        x = []
        y = []
        for i in range(0, len(content), 1):
            x.append(content[i].split(' ')[0])
            y.append(content[i].split(' ')[1])

        plt.plot(x, y)
        plt.title("Sample Line")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")

        plt.show()

    # This function will draw line chart and data will be read through csv file
    def lineChartOfFinanacialData(self):
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "..", "inputFiles/fdata.csv"))

        data = pd.read_csv(filepath)
        data.plot()
        plt.title("Line chart")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.show()

    # This function will plot more than 2 lines with different styling in same plot
    def plotLines(self):
        x = np.arange(4)

        plt.plot(x, x, label='1st-Line', c='g', linewidth=3)
        plt.plot(x, 2 * x, label='2nd-Line', c='y', linewidth=3, linestyle='dotted')
        plt.plot(x, 3 * x, label='3rd-Line', c='r', linewidth=3)
        plt.plot(x, 4 * x, label='4th-Line', c='b', linewidth=3)
        plt.title("Line chart")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.legend()

        plt.show()





d = Demo()

# d.drawLine()
# d.drawLineInputFile()
# d.lineChartOfFinanacialData()
# d.plotLines()