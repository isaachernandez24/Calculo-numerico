import math

#funcion para realizar el metdo de biseccion 
def bisection_method(func, a, b, tol=0.01, max_iter=100):
    iter_count = 0
    #el bucle seguira iterando hasta que el numero de iteraciones sea igual a 100 o que el error sea menor a la tolerancia que tiene 
    while (b - a) / 2 > tol and iter_count < max_iter:
        m = (a + b) / 2
        f_a = func(a)
        f_b = func(b)
        f_m = func(m)
        
        if f_a * f_m < 0:
            b = m
        else:
            a = m
        #calculo del error
        error = (b - a) / 2
        iter_count += 1

    return (a + b) / 2
