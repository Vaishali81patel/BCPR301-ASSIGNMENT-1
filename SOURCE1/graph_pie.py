# written by Vaishali
"""
Basic pie chart
Note: only the show_gender is implemented
"""

import matplotlib.pyplot as plt
from graph import Graph


class PieChart(Graph):
    def show_gender(self):
        explode = (0, 0.1)  

        fig1, ax1 = plt.subplots()

        ax1.pie(self._sizes, explode=explode, labels=self._labels,
                autopct='%1.1f%%', shadow=True, startangle=90)

        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')

        plt.title("Ratio of Females vs Males")
        plt.show()

    def show_BMI(self):
        pass