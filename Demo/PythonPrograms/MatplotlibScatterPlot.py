from matplotlib import pyplot as plt
import numpy as np


class Demo:

    # This function draws simple scatter plot
    def scatterPlot(self):
        x = np.random.rand(10)
        y = np.random.rand(10)

        plt.scatter(x, y, s=50, facecolors='none', edgecolors='green')
        plt.title("Sample scatter plot")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.show()

    # This function draws scatter plot having circles with different sizes
    def circlesWithDifferentSizes(self):
        x = np.random.rand(10)
        y = np.random.rand(10)

        for i in range(0, len(x), 1):
            plt.scatter(x[i], y[i], s=10+(i*20), facecolors='none', edgecolors='green')

        plt.title("Sample scatter plot")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.show()

    # This function compares marks of subjects maths and science with marks_range
    # and plots them.
    def compareMarks(self):
        math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
        science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
        marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

        plt.scatter(marks_range, math_marks, label='Maths range')
        plt.scatter(marks_range, science_marks, label='Science range')

        plt.title("Marks Comparison")
        plt.xlabel("Marks Range")
        plt.ylabel("Subject marks")
        plt.legend()
        plt.show()

    # This function draws a scatter plot for three different groups comparing weights
    # and heights.
    def scatterPlotUsingGroups(self):
        group1 = {'height': [113.7, 157.7, 136],
                  'weight': [60.45, 61, 56.23]}
        group2 = {'height': [130.7, 100.7, 200],
                  'weight': [61.9, 64, 62.1]}
        group3 = {'height': [165.8, 170.9, 192.8],
                  'weight': [68.7, 71, 71.3]}

        plt.scatter(group1['height'], group1['weight'], color='red', label='Group1')
        plt.scatter(group2['height'], group2['weight'], color='blue', label='Group2')
        plt.scatter(group3['height'], group3['weight'], color='black', label='Group3')

        plt.title("comparison between weights and heights")
        plt.xlabel("Height")
        plt.ylabel("Weight")
        plt.legend()
        plt.show()


d = Demo()
# d.scatterPlot()
# d.circlesWithDifferentSizes()
# d.compareMarks()
d.scatterPlotUsingGroups()