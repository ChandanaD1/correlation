#correlation

import csv
import pandas as pd
import plotly.express as px

# to use co-coef
import numpy

df1 = pd.read_csv("csvfiles/Coffee.csv")
coffee = df1["Coffee in ml"].tolist()
sleep = df1["sleep in hours"].tolist()

graph1 = px.scatter(x=coffee, y=sleep)
graph1.show()

correlation1 = numpy.corrcoef(coffee,sleep)
print(correlation1[0,1])

df2 = pd.read_csv("csvfiles/Marks.csv")
marks = df2["Marks In Percentage"].tolist()
days = df2["Days Present"].tolist()

graph2 = px.scatter(x=marks, y=days)
graph2.show()

correlation2 = numpy.corrcoef(marks,days)
print(correlation2[0,1])