import pandas as p
import csv
import plotly.figure_factory as pff

df = p.read_csv("data.csv")
fig = pff.create_distplot([df["Height(Inches)"].tolist()],["Heights"],show_hist = False)
fig.show()
