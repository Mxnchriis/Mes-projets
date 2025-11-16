# def f(x):
#     return x * x - 4

iteration = 0

def OGsecante(f, x0, x1, eps):
    global iteration
    x2 = x0
    xinter = x1
    while abs(x2-xinter) > eps:
        x2 = x0
        xinter = (x0 * f(x1) - x1 * f(x0))/(f(x1) - f(x0))
        x0 = xinter
        iteration+=1

    print(f"la solution Secante est {xinter} et la fonction s'est répété {iteration} fois\n")

def secante(f, x0, x1, eps):
    iteration = 0
    
    while abs(x1 - x0) > eps:
        if f(x1) - f(x0) == 0:  # Éviter la division par zéro
            raise ValueError("Division par zéro détectée dans la méthode de la sécante.")
        
        x_new = x1 - (x1 - x0) * f(x1) / (f(x1) - f(x0))
        x0, x1 = x1, x_new
        iteration += 1

    return x1, iteration

# secante( f, 0, 5, 0.0001)

# def secante2(f, x0, x1, eps):
#     while abs(x0 - xinter) > eps:
#         xinter = 1
#         x0 = (x0 - f(x1) - x1 * f(x0))/(f(x1)-f(x0))
#     return x0

