import plotly as plt
import plotly.graph_objs as go
import numpy as np
import pandas as pd


class Demo:

    # This function draws a scatter plot for random 1000 x and y coordinates
    def scatterPlot(self):
        x = np.random.rand(1000)
        y = np.random.rand(1000)

        trace = go.Scatter(x=x, y=y, mode='markers')
        data = [trace]

        plt.offline.plot(data, filename='scatter.html')

    # This function draws a line and scatter plots for random 100 x and y coordinates
    def lineScatterPlot(self):
        x = np.random.rand(100)
        y = np.random.rand(100)

        trace = go.Scatter(x=x, y=y, mode='lines+markers')
        data = [trace]

        plt.offline.plot(data, filename='line_scatter.html')

    #  This function draws a scatter plot for a given dataset csv's url and show datalabels on hover
    def scatterPlotFromCSV(self):
        data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

        x = data['Rank']
        y = data['Population']

        trace = go.Scatter(x=x, y=y, mode='markers', text=data['State'])
        layout = go.Layout(title='Population across states', xaxis=dict(title='Rank'), yaxis=dict(title='Population'))
        fig = go.Figure(data=[trace], layout=layout)

        plt.offline.plot(fig, filename='scatter.html')


d = Demo()
# d.scatterPlot()
# d.lineScatterPlot()
d.scatterPlotFromCSV()