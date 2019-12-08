import numpy as np
import matplotlib.pyplot as plt
from math import *

def run(x):
    y=np.zeros(200)
    for i in n:
        i=int(i)
        if i==0:
            y[i]=-1.5*x[i]+2*x[i+1]-0.5*x[i+2]
        elif ((0 < i) and (i <= 198)):
                y[i]=0.5*x[i+1]-0.5*x[i-1]
        elif i==199:
            y[i]=1.5*x[i]-2*x[i-1]+0.5*x[i-2]
            plt.plot(n,x,label='x values')
            plt.plot(n,y,label='y values')
            plt.legend()
            
n = np.linspace(0,199,num=200,endpoint=True)
z = input("Enter an equation: ")          
run(eval(z))
