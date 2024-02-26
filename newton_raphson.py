import math

def newton_raphson(x0, tol, fx, dfx):
    iteracion = 1
    while True:
        #se recibe la derivada del archivo tests.py 
        derivada = dfx(x0)

        #si la derivada es 0 el sistema se detiene 
        if derivada == 0:
            print("La derivada es cero. El método no puede continuar.")
            return None

        #calculo del error 
        x1 = x0 - fx(x0) / derivada
        error = abs(x1 - x0)

        # solo se detiene si el error es menor a la tolerancia que se obtiene en el test
        if error < tol:
            return x1, error
        
        x0 = x1
        iteracion += 1
