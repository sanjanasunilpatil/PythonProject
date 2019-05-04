from matplotlib import pyplot as plt


class Demo:

    # This function draws simple bar chart with unique color for all bars
    def drawBarCharWithUniqueColor(self):
        x = ['Java', 'Python', 'PHP', 'JavaScript', 'C #', 'C++']
        y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        plt.bar(x, y, color='green')
        plt.title("Popularity based on Programming language")
        plt.xlabel("Programming language")
        plt.ylabel("Popularity")

        plt.show()

    # This function draws simple bar chart with different colors for all bars.
    # Provides borders at each bar.
    # Provides text label above each bar displaying its popularity (float value).
    def drawBarChartWithDifferentColors(self):
       x = ['Java', 'Python', 'PHP', 'JavaScript', 'C #', 'C++']
       y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
       color = ['green', 'red', 'blue', 'black', 'pink', 'yellow']

       plt.bar(x, y, color=color, edgecolor='blue')
       plt.title("Popularity based on Programming language")
       plt.xlabel("Programming language")
       plt.ylabel("Popularity")

       for i in range(0, len(x), 1):            # Iterates over each bar
           plt.text(x[i], y[i], y[i])           # Labeling above each bar

       plt.show()

    # This function displays a horizontal bar chart.
    def drawHorizontalBar(self):
        x = ['Java', 'Python', 'PHP', 'JavaScript', 'C #', 'C++']
        y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        plt.barh(x, y, color='green')
        plt.title("Popularity based on Programming language")
        plt.ylabel("Programming language")
        plt.xlabel("Popularity")

        plt.show()


d = Demo()
# d.drawBarCharWithUniqueColor()
d.drawBarChartWithDifferentColors()
# d.drawHorizontalBar()