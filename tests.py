import unittest
import math as mt
from biseccion import bisection_method
from newton_raphson import newton_raphson
from rienman_trapecio import calculate_error, riemann_integral, trapezoidal_integral

class TestCalculoMethods(unittest.TestCase):
    def test_bisection_method(self):
        # Definir la función para la prueba
        def user_function(x):
            return x**2 - 4

        # Definir los parámetros iniciales
        a = 0
        b = 5

        # Llamar al método de bisección
        raiz_aproximada = bisection_method(user_function, a, b)

        # Verificar si la raíz aproximada es correcta dentro de una tolerancia
        self.assertEqual(raiz_aproximada, 2.001953125, msg="Resultado incorrecto para el método de bisección")

    def test_newton_raphson(self):
        # Definir la función y la derivada
        dfx = lambda x: -2*x*(mt.e**(-x**2))-2
        fx = lambda x: (mt.e**(-x**2))-2*x+1

        # Llamar al método de Newton-Raphson
        punto, error = newton_raphson(2, 0.001, fx, dfx)

        # Verificar si el resultado y el error son los esperados
        self.assertEqual(punto, 0.7744627493872464, msg="Resultado incorrecto para el método de Newton-Raphson")
        self.assertEqual(error, 1.8561324865995488e-07, msg="Error incorrecto para el método de Newton-Raphson")

    def test_riemann_integral(self):
        # Definir la función para la prueba
        def user_function(x):
            return x**2

        # Definir los parámetros de la integral
        a = 0
        b = 2
        n = 100000
        integral_exact = (b ** 3) / 3

        # Calcular la integral utilizando el método de Riemann
        integral_riemann = riemann_integral(user_function, a, b, n)
        error_riemann = calculate_error(integral_riemann, integral_exact)

        # Verificar si la integral aproximada y el error son correctos
        self.assertEqual(integral_riemann, 2.6666266667999796, msg="Resultado incorrecto para la integral de Riemann")
        self.assertEqual(error_riemann, 3.99998666869017e-05, msg="Error incorrecto para la integral de Riemann")

    def test_trapezoidal_integral(self):
        # Definir la función para la prueba
        def user_function(x):
            return x**2

        # Definir los parámetros de la integral
        a = 0
        b = 2
        n = 100000
        integral_exact = (b ** 3) / 3

        # Calcular la integral utilizando el método del trapecio
        integral_trapezoidal = trapezoidal_integral(user_function, a, b, n)
        error_trapezoidal = calculate_error(integral_trapezoidal, integral_exact)

        # Verificar si la integral aproximada y el error son correctos
        self.assertEqual(integral_trapezoidal, 2.6666666667999968, msg="Resultado incorrecto para la integral trapezoidal")
        self.assertEqual(error_trapezoidal, 1.3333023574091385e-10,  msg="Error incorrecto para la integral trapezoidal")

if __name__ == '__main__':
    unittest.main()
