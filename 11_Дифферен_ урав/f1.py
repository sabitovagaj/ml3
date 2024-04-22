import numpy as np
from scipy. integrate import odeint
import matplotlib.pyplot as plt

 # create function
def dydt(y, t):
	return -y*t+2*t+1

t = np.linspace( -2, 2, 51) # vector of time
y0 = 1 # start value
y = odeint (dydt, y0, t) # solve eq.
y = np.array(y).flatten() 
plt.plot( t, y,'-sr', linewidth=3) # graphic
plt.show() # display
