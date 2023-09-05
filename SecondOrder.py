import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return 0
def g(y, z, t, m, k, c):
    return f(t)  -(k/m)*z-y*c/m


def euler_method(y0, z0, num_steps, tf, m , k , c ):
    t_values = np.linspace(0, tf, num=num_steps+1)
    delta_t = tf/num_steps


    y_values = np.zeros(num_steps+1)
    z_values = np.zeros(num_steps+1)


    z_prime_values = np.zeros(num_steps+1)
    y_values[0] = y0
    z_values[0] = z0

    z_prime_values[0]=g(y_values[0], z_values[0],t_values[0], m, k,c)

    for i in range(1, num_steps+1):
        y_values[i] = y_values[i-1]+delta_t*z_values[i-1]
        z_values[i] = z_values[i-1]+delta_t*z_prime_values[i-1]
        z_prime_values[i] =  g(y_values[i-1], z_values[i-1],t_values[i-1], m, k,c)
    
    return t_values , y_values
m=int(input("Enter m :"))
k=int(input("Enter k :"))
c=int(input("Enter c :"))
y0=int(input("Enter y0 :"))
z0=int(input("Enter z0 :"))

num_steps=int(input("Enter the number of steps : "))

tf=int(input("Enter stopping time : "))

t , y = euler_method(y0,z0,num_steps,tf, m , k ,c)


plt.plot(t,y)
plt.show()
