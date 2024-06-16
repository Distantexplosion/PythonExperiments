import math
import time

b=1
dt=1

def f(t):
    return t

def f_next(t,x):
    return f(t)*math.e**(b*x*dt)

t=0

while (t<1000000):
    #print ("Time:" + str(t))
    for x in range(1):
        #print(f_next(t,1))
        y = f_next(t,1)
        
   # time.sleep(0.01)
    t=t+1

print ("Done"+ str (y))
print(math.e)
