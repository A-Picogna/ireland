'''Alexandre Picogna & Yasmine Serot'''

import pandas
import time
import plotly
from plotly.graph_objs import Scatter, Layout
import numpy as np
print (plotly.__version__)

csv = pandas.read_csv("./data/DataSet.csv", engine='python', header=0, index_col=0)

categoricalFeatures = csv.describe(include=["object"])

countList = []
cardList = []
mode1 = []
mode1Count = []
mode1Percentage = []
mode2 = []
mode2Count = []
mode2Percentage = []

csvCategoryColumns = csv.select_dtypes(include=['object'])
for col in csvCategoryColumns:
    tmp = csv[col].values.tolist().count(' ?')
    tmp2 = round((tmp/len(csv[col].values.tolist()))*100)
    if tmp == 0:
        '''we remove 1 if there is a missing category'''
        tmp2 = tmp2-1
        if tmp2 < 0:
            tmp2 = 0
    countList.append(tmp2)
    cardList.append(len(csv[col].value_counts().tolist()))
    mode = csv[col].value_counts()
    indexList = mode.index.tolist()
    valueList = mode.values.tolist()
    modeP = csv[col].value_counts(normalize=True)
    mode1.append(indexList[0])
    mode1Count.append(valueList[0])
    mode1Percentage.append(round(modeP.values.tolist()[0]*100))
    mode2.append(indexList[1])
    mode2Count.append(valueList[1])
    mode2Percentage.append(round(modeP.values.tolist()[1]*100))

categoricalFeatures = categoricalFeatures.transpose()
categoricalFeatures.insert(1, "% Missing", countList)
categoricalFeatures.insert(2, "Card", cardList)
categoricalFeatures.insert(3, "Mode", mode1)
categoricalFeatures.insert(4, "Mode Count", mode1Count)
categoricalFeatures.insert(5, "Mode %", mode1Percentage)
categoricalFeatures.insert(6, "2nd Mode", mode2)
categoricalFeatures.insert(7, "2nd Mode Count", mode2Count)
categoricalFeatures.insert(8, "2nd Mode %", mode2Percentage)
categoricalFeatures = categoricalFeatures.drop('unique', 1)
categoricalFeatures = categoricalFeatures.drop('top', 1)
categoricalFeatures = categoricalFeatures.drop('freq', 1)

categoricalFeatures.to_csv("./data/picogna_serot-DQR-CategoricalFeatures.csv")

print(categoricalFeatures)


'''generation of plots'''
'''

for col in csvCategoryColumns:
    data = csv[col].value_counts()
    Xvalue = data.index.tolist()
    Yvalue = data.values.tolist()
    card = len(csv[col].value_counts().tolist())
    if card <= 10:
        plotly.offline.plot({
            "data": [
                plotly.graph_objs.Bar(x=Xvalue, y=Yvalue)
            ],
            "layout": Layout(
                title=col
            )
        })
    else:
        print(Yvalue)
        plotly.offline.plot({
            "data": [
                plotly.graph_objs.Histogram(x=csv[col])
            ],
            "layout": Layout(
                title=col
            )
        })
    time.sleep(2)

'''