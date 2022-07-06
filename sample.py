import pandas as pd 
import plotly.express as pe
import random as rd
import statistics as st
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
p_mean=st.mean(data)
p_std=st.stdev(data)
print(f"Population mean is {p_mean}")
print(f"Population Standard Deviation is {p_std}")
fig=ff.create_distplot([data] , ["Temperature"] , show_hist=False)
#fig.show()

dataSet=[]
for i in range(0,100):
    random_index=rd.randint(0,len(data))
    value=data[random_index]
    dataSet.append(value)
mean=st.mean(dataSet)
std=st.stdev(dataSet)
#print(f"Sample mean is {mean}")
#print(f"Sample Standard Deviation is {std}")

def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=rd.randint(0,len(data) - 1 )
        value=data[random_index]
        dataSet.append(value)
    mean=st.mean(dataSet)
    return mean
def setup():
    meanList = []
    for i in range(0,1000):
        s=randomSetOfMean(100)
        meanList.append(s)
    mean=st.mean(meanList)
    std = st.stdev(meanList)
    print(f"Mean of the sample distribution is {mean}")
    print(f"Standard deviation of the sample distribution is {std}")
    fig=ff.create_distplot([meanList] , ["Sample Temperature Data"] , show_hist=False)
    fig.show()
setup()

#conclusion
#the mean of the sample data is equal to the mean of the population data

#Standard deviation of the sampling mean = 1/10 of Population Standard deviation
