# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:03:52 2023

@author: icuredwa
"""

import matplotlib.pyplot as plt
import numpy as np
import math as math
k1 = 1.0
k2 = 1.0
k3 = 1.0
k4 = 0.2
dt = 0.01


x = 0.2
y = 1
t = 0

x_arr = []
y_arr = []
t_arr = []

def prey_der(x,y) :
    prey_rate = x*(k1-k2*y)
    return prey_rate

def pred_der(x,y) :
    pred_rate = y*(k3*x-k4)
    return pred_rate


while t <= 100:
    x_arr.append(x)
    y_arr.append(y)
    t_arr.append(t)
    g = prey_der(x,y)
    q = pred_der(x,y)
    x = x + (g * dt)
    y = y + (q * dt)
    t = t+dt
    
plt.plot(t_arr,x_arr ,label = "Prey population")
plt.plot(t_arr,y_arr , label = "Predator population")
plt.legend(loc = "upper right")
plt.xlabel("time (yr)")
plt.ylabel("population size (1000's)")
plt.title("Prey and predator population vs time")
plt.grid()
#plt.savefig("population vs time part 1.pdf")
plt.show()


plt.plot(x_arr,y_arr)
plt.ylabel("Prediators")
plt.xlabel("Prey")
plt.title("prey vs predators Phase Space")
plt.scatter(k4/k3, k1/k2, color = "red" , label = "(k4/k3 , k1/k2)")
plt.scatter(0,0, color = "orange", label = "(0,0)")
plt.legend()
plt.savefig("phase space part 1.pdf")
plt.show()

x = 1
y = 1
t = 0

x_arr = []
y_arr = []
t_arr = []

c_arr = []



while t <= 100:


    x_arr.append(x)
    y_arr.append(y)
    t_arr.append(t)
    c = k3 * x - (k4*math.log(x+1)) + k2*y - (k1 * math.log(abs(y)))
    c_arr.append(c)
    g = (prey_der(x,y) + prey_der(x + dt,y+dt))/2
    q = (pred_der(x,y) +pred_der(x + dt,y + dt))/2
    x = x + (g * dt)
    y = y + (q * dt)
    t = t+dt
    


plt.plot(t_arr,x_arr ,t_arr,y_arr)
plt.show()


plt.plot(x_arr,y_arr)
plt.ylabel("Prediators")
plt.xlabel("Prey")
plt.title("prey vs predators Phase Space")
plt.scatter(k4/k3, k1/k2, color = "red" , label = "(k4/k3 , k1/k2)")
#plt.scatter(0,0, color = "orange", label = "(0,0)")
plt.legend(loc = "lower right")

plt.savefig("phase space part 2.2.pdf")

plt.show()





'''

plt.plot(t_arr,c_arr)
plt.show()




'''