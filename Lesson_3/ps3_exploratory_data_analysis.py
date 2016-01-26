import numpy as np
import pandas
import matplotlib.pylab
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histogram may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    plt.figure()
    turnstile_weather[turnstile_weather["rain"] == 0]["ENTRIESn_hourly"].hist(bins = 150, alpha = 0.8, label = "No Rain") # your code here to plot a historgram for hourly entries when it is not raining
    turnstile_weather[turnstile_weather["rain"] == 1]["ENTRIESn_hourly"].hist(bins = 150, alpha = 0.8, label = "Rain")# your code here to plot a historgram for hourly entries when it is raining
    x1,x2,y1,y2 = plt.axis()
    plt.axis([0, 6000, y1, 45000])
    plt.legend()
    plt.title("Histogram of ENTRIESn_hourly")
    plt.xlabel("ENTRIESn_hourly")
    plt.ylabel("Frequency")
    print("Here")
    return plt



turnstile_weather = pandas.read_csv("turnstile_data_master_with_weather.csv")
fig = entries_histogram(turnstile_weather)
fig.show()