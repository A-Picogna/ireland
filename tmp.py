
header = []
header.append('Elevation')
header.append('Aspect')
header.append('Slope')
header.append('Horizontal_Distance_To_Hydrology')
header.append('Vertical_Distance_To_Hydrology')
header.append('Horizontal_Distance_To_Roadways')
header.append('Hillshade_9am')
header.append('Hillshade_Noon')
header.append('Hillshade_3pm')
header.append('Horizontal_Distance_To_Fire_Points')
for i in range(1, 5):
    tmp = 'Wilderness_Area'+str(i)
    header.append(tmp)
for i in range(1, 41):
    tmp = 'Soil_Type'+str(i)
    header.append(tmp)

q1 = [2383,165,13,60,4,67,231,244,141,875,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # expect 3
q2 = [2384,170,15,60,5,90,230,245,143,864,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # expect 3
q3 = [3061,288,12,283,32,3140,185,239,194,779,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1] # expect 1

#q = {}
i = 0
length = (len(q1))
res = "{"
for i in range(len(header)):
    tmp=[]
    tmp.append(q1[i])
    tmp.append(q2[i])
    tmp.append(q3[i])
    res += "'"+header[i]+"':"+str(tmp)+","
res += "}"

print(res)


