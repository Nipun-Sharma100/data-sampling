import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import statistics 
import plotly.graph_objects as go

df=pd.read_csv("code7.csv")
data=df["population_mean"].tolist()


def random_setofmean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    print("mean of sampling distribution: ",mean)
    fig=ff.create_distplot([df],["population_mean"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_setofmean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()

def sd():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_setofmean(100)
        mean_list.append(set_of_means)
    
    sd=statistics.stdev(mean_list)
    print("sd",sd)
sd()