from matplotlib import pyplot as plt
from os import path
import pandas as pd


class Demo:

    # This functions creates simple pie chart with labels
    def createPieChart(self):
        label = ['Java', 'Python', 'PHP', 'JavaScript', 'C #', 'C++']
        readings = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

        plt.pie(readings, labels=label, autopct='%.2f%%')
        plt.legend()
        plt.show()

    # This function first get the filepath of input medal.csv file.
    # Then read csv file and data gets converted into pandas's Data Frame DS.
    # Labels and readings will get calculated from data and then pass to pie method to draw pie chart
    def pieChartFromCSV(self):
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "..", "inputFiles/medal.csv"))

        data = pd.read_csv(filepath)
        labels = list(data["country"])
        readings = list(data["gold_medal"])

        plt.pie(readings, labels=labels, autopct='%.2f%%')
        plt.legend()
        plt.show()


d = Demo()
d.createPieChart()
# d.pieChartFromCSV()
