import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    

    # Create scatter plot
    df_draw = df.copy()
    plt.scatter(df_draw['Year'], df_draw['CSIRO Adjusted Sea Level'])
    plt.axis([1850, 2100,-2,12])
    plt.xticks(np.arange(1850, 2100, step=25))

    # Create first line of best fit
    #was throwing error 'too many values to unpack' because linregress returns 5 values, but we only need the first 2
    slope, intercept = linregress(df_draw['Year'], df_draw['CSIRO Adjusted Sea Level'])[:2]
    
    #see scipy doc https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html re drawing line of best fit
    plt.plot(np.arange(1880, 2051, step=1), slope*np.arange(1880, 2051, step=1) + intercept, color='red')
    

    # Create second line of best fit
    slope2, intercept2 = linregress(df_draw[df_draw['Year'] >= 2000]['Year'], df_draw[df_draw['Year'] >= 2000]['CSIRO Adjusted Sea Level'])[:2]

    plt.plot(np.arange(2000, 2051, step=1), slope2*np.arange(2000, 2051, step=1) + intercept2, color='blue')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()