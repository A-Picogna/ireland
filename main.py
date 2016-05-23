import plotly
import pandas

csv = pandas.read_csv("DataSet.csv", engine='python', header=0, index_col=0)


test = csv.describe(include=["object"])
test = test.transpose()
countList = []

for col in csv.columns:
    count = 0
    for val in csv[col].values:
        if val == " ?":
            count += 1
    countList.append(count)


print(countList)
print(test)

