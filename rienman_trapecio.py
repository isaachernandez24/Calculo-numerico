import math

def riemann_integral(func, a, b, n):
    delta_x = (b - a) / n
    integral_sum = 0
    for i in range(n):
        x_i = a + i * delta_x
        integral_sum += func(x_i) * delta_x
    return integral_sum

def trapezoidal_integral(func, a, b, n):
    delta_x = (b - a) / n
    integral_sum = (func(a) + func(b)) / 2
    for i in range(1, n):
        x_i = a + i * delta_x
        integral_sum += func(x_i)
    return integral_sum * delta_x

def calculate_error(integral_approx, integral_exact):
    return abs(integral_approx - integral_exact)