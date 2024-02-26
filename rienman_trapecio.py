import math
#funcion para calcular la aproximacion mediante el metodo de riemman 
def riemann_integral(func, a, b, n):
    delta_x = (b - a) / n
    integral_sum = 0

    # iterador para resolver la sumatoria 
    for i in range(n):
        x_i = a + i * delta_x
        integral_sum += func(x_i) * delta_x
    return integral_sum

# funcion para calcular la integral por el metodo del trapecio 
def trapezoidal_integral(func, a, b, n):
    delta_x = (b - a) / n
    integral_sum = (func(a) + func(b)) / 2

    #iterador para resolver
    for i in range(1, n):
        x_i = a + i * delta_x
        integral_sum += func(x_i)
    return integral_sum * delta_x

#funcion para calcular el error (funciona para ambos metodos)
def calculate_error(integral_approx, integral_exact):
    return abs(integral_approx - integral_exact)
