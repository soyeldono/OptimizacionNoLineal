import math
import matplotlib.pyplot as plt
import numpy as np

max_it = 20

def f(x,l=None):
    global iss
    if l != None:
        iss[l] += 1
    try:
        return 0.65 - (0.75/(1+x**2)) - 0.65*x*np.arctan(1/x)
    except:
        return 0

def fib(n):
    n = int(n)
    if n == 0 or n == 1:
        return 1
    fn_1 = 1
    fn_2 = 0
    for i in range(2,n+2):
        aux = fn_1
        fn_1 = fn_1+fn_2
        fn_2 = aux
    return fn_1

def fibonacci(a,b,n):
    k = 2
    L = b-a
    aux = 0
    Lk = (fib(n-k)/fib(n))*L
    x1 = a + Lk 
    x2 = b - Lk 
    fx1 = f(x1,"f") 
    fx2 = f(x2,"f") 
    z = 0
    while k <= n and z < max_it:
        if k > 2:
            Lk = (fib(n-k)/fib(n))*L
            x1 = a + Lk 
            x2 = b - Lk 
            fx1 = f(x1,"f") if aux != 1 else fx1
            fx2 = f(x2,"f") if aux != 2 else fx2
        if fx1 > fx2:
            a = x1
            aux = 1
            fx1 = fx2
        else:
            b = x2
            aux = 2
            fx2 = fx1
        k += 1
        z += 1
    return ("{0:.3f}".format(a),"{0:.3f}".format(b))

def division(a,b,e):
    xm = (a+b)/2
    fxm = f(xm,"d")
    L = b-a
    z = 0
    while abs(L) > e and z < max_it:
        x1 = a + (L/4)
        x2 = b - (L/4)            
        fx1 = f(x1,"d")
        fx2 = f(x2,"d")
        if fx1 < fxm:
            b = xm
            xm = x1
            fxm = fx1
        else:
            if fx2 < fxm:
                a = xm
                xm = x2
                fxm = fx2
            else:
                a = x1
                b = x2
        L = b - a
        z += 1
    return ("{0:.3f}".format(a),"{0:.3f}".format(b))   

def acotamiento(x0,D):
    f1x0 = f(x0-abs(D),"a") 
    f2x0 = f(x0,"a")
    f3x0 = f(x0+abs(D),"a")

    if f1x0 >= f2x0 >= f3x0:
        x1 = x0 + abs(D)
        D = abs(D)
    else:
        if f1x0 <= f2x0 <= f3x0:
            x1 = x0 - abs(D)
            D = abs(D)*-1
        else:
            return (x0-abs(D),x0+abs(D))
    
    k = 1
    xk_1 = x1 + ((2**k)*D)
    xk__1 = x0
    xk = x1
    fxk_1 = f(xk_1,"a")
    fxk = f3x0
    z = 0

    while fxk_1 < fxk and z < max_it:
        k += 1
        xk__1  = xk
        xk = xk_1
        fxk = fxk_1
        xk_1 = xk + ((2**k)*D)
        fxk_1 = f(xk_1,"a")
        z += 1
        
    return ("{0:.3f}".format(xk__1),"{0:.3f}".format(xk_1))




a,b,e = 0.001,3,0.001
iss = {"f":0,"d":0,"a":0}
fib_res = fibonacci(a,b,18)
print("fib:("+str(fib_res[0])+","+str(fib_res[1])+")")
div_res = division(a,b,e)
print("div:("+str(div_res[0])+","+str(div_res[1])+")")
acot_res = acotamiento(0.5,0.0025)
print("acot:("+str(acot_res[0])+","+str(acot_res[1])+")")
print(iss)
plt.plot(np.arange(0,3,0.01),f(np.arange(0,3,0.01)))
plt.show()
