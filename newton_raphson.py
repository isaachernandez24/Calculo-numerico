import math

def newton_raphson(x0, tol, fx, dfx):
    iteracion = 1
    while True:
        derivada = dfx(x0)
        if derivada == 0:
            print("La derivada es cero. El método no puede continuar.")
            return None
        
        x1 = x0 - fx(x0) / derivada
        error = abs(x1 - x0)
        
        if error < tol:
            return x1, error
        
        x0 = x1
        iteracion += 1
