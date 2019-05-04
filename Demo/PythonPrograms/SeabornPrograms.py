import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd


class Demo:

    # This function draws bar plot of sex against survived for a dataset titanic
    def barPlot(self):
        data = sb.load_dataset('titanic')
        sb.barplot(x='sex', y='survived', hue='who', data=data)
        plt.show()

    # This function draws a point plot for sex against survived for a dataset titanic
    def pointPlot(self):
        data = sb.load_dataset('titanic')
        sb.pointplot(x='sex', y='survived', data=data)
        plt.show()

    # This function draws a scatter plot of “day” against “total bill” for a dataset tips
    def scatterPlot(self):
        data = sb.load_dataset('tips')
        sb.barplot(x='day', y='total_bill', data=data)
        plt.show()

    # This function draws a violin plot of sex against total_bill for a given dataset
    def violinPlot_tips(self):
        data = sb.load_dataset('tips')
        sb.violinplot(x='sex', y='total_bill', data=data)
        plt.show()

    # This function draws a violin plot of “species” against “sepal length” for a dataset iris
    def violinPlot_iris(self):
        data = sb.load_dataset('iris')
        sb.violinplot(x='species', y='sepal_length', data=data)
        plt.show()

    # This function draws box plot of life expectancy by continent for a data set given in a
    # url
    def boxPlot(self):
        data = pd.read_csv('https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv')
        sb.boxplot(x='lifeExp', y='continent', data=data)
        plt.show()

    # This function draws a box plot of day by tips for a dataset tips
    def boxPlotTips(self):
        data = sb.load_dataset('tips')
        sb.boxplot(x='day', y='tip', data=data)
        plt.show()

    # This function draws a swarm plot of total bill against size for a dataset tips
    def swarmPlot1(self):
        data = sb.load_dataset('tips')
        sb.swarmplot(x='total_bill', y='size', data=data)
        plt.show()

    # This function draws swarm plot of “total bill” against day for a dataset tips
    def swarmPlot2(self):
        data = sb.load_dataset('tips')
        sb.swarmplot(x='total_bill', y='day', data=data)
        plt.show()


d = Demo()
# d.barPlot()
# d.pointPlot()
# d.scatterPlot()
# d.violinPlot_tips()
# d.violinPlot_iris()
# d.boxPlot()
# d.boxPlotTips()
# d.swarmPlot1()
d.swarmPlot2()