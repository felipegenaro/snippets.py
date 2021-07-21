# Simple implementation of Matplotlib for generation of charts

import matplotlib.pyplot as mp

percenteges = [20,40,30,10]
labels = ["Python", "SQL", "JavaScript", "C#"]

mp.pie(percenteges, labels=labels)
mp.show()


# See more on https://matplotlib.org/stable/tutorials/introductory/sample_plots.html