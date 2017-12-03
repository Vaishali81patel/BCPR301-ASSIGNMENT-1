# written by Vaishali

import matplotlib.pyplot as plt
from graph import Graph
import numpy as na
import matplotlib.pyplot as plt


class BarChart(Graph):

    def show_gender(self):
        _labels = self._labels
        _data = self._sizes

        # check to see what range the yticks should be
        if _data[0] > _data[1]:
            _top_value = _data[0]
        else:
            _top_value = _data[1]

        error = [0.3497, 0.3108]

        xlocations = na.array(range(len(_data))) + 0.5
        width = 0.5
        plt.bar(xlocations, _data, yerr=error, width=width)
        plt.yticks(range(0, _top_value + 1))
        plt.xticks(xlocations + width / 2, _labels)
        plt.xlim(0, xlocations[-1] + width * 2)
        plt.title("Males and Females")
        plt.gca().get_xaxis().tick_bottom()
        plt.gca().get_yaxis().tick_left()

        plt.show()

    def show_BMI(self):
        pass
