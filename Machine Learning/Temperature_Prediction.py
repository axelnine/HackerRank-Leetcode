import fileinput
import pandas as pd
import numpy as np

i=-2
mintemp = []
maxtemp = []
missing_dict = {}
def change(inputseries):
    inputseries = pd.Series(inputseries)
    inputseries = inputseries.str.replace("\n","")
    inputseries = inputseries.apply(lambda x: np.nan if 'M' in x else x)
    inputseries = pd.to_numeric(inputseries, errors='coerce')
    return inputseries

for line in fileinput.input():
    if i==-2 or i==-1:
        i=i+1
    else:
        temperature_list = line.split("\t")
        if 'M' in temperature_list[2]:
            missing_dict[int(temperature_list[2].replace("Missing_","").replace("\n",""))]=['min',i]
        if 'M' in temperature_list[3]:
            missing_dict[int(temperature_list[3].replace("Missing_","").replace("\n",""))]=['max',i]
        i=i+1
        mintemp.append(temperature_list[2])
        maxtemp.append(temperature_list[3])


mintemp = change(mintemp)
maxtemp = change(maxtemp)

df = pd.DataFrame({'min' : mintemp,'max' : maxtemp})
df = df.interpolate(method = 'linear')

for x in sorted(missing_dict.keys()):
    print(df[missing_dict[x][0]][missing_dict[x][1]])
