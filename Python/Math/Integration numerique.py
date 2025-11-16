import math
import numpy as np
import matplotlib.pyplot as plt
import cmath

# def f (x):
#     return x * math.sin(x)

# def f (x):
#     return math.exp(x) * math.sin(x)

# def f (t):
#     return math.exp(-(t**2))

# def f (u):
#     return 1/ (3 - math.cos(u))

# def f (x):
#     try:
#         return math.sin(1/x) if x != 0 else 0
#     except ZeroDivisionError:
#         return 0

# def f (x):
#     try:
#         return 1/x if x != 0 else 0
#     except ZeroDivisionError:
#         return 0

# def f (x):
#     try:
#         return abs(x) if x != 0 else 0
#     except ZeroDivisionError:
#         return 0

def f (x):
    try:
        return cmath.exp(1j * x) if x != 0 else 0
    except ZeroDivisionError:
        return 0

def integrNumerique(a, b):
    n = 1000
    Pas = (b-a)/n
    PasM = (b-a)/(2*n)
    Ag = 0
    Ad = 0
    Am = 0
    Trapeze = 0
    
    x_vals = np.linspace(a, b, 1000)  # Points pour tracer la fonction
    y_vals = [f(x) for x in x_vals]   # Valeurs de la fonction
    
    x_Ag = np.linspace(a, b - Pas, n)
    x_Ad = np.linspace(a + Pas, b, n)
    x_Am = [a + (2 * k + 1) * PasM for k in range(n)]
    x_Trapeze = np.linspace(a, b, n)
    
    y_Ag = [f(x) for x in x_Ag]
    y_Ad = [f(x) for x in x_Ad]
    y_Am = [f(x) for x in x_Am]
    y_Trapeze = [f(x) for x in x_Trapeze]
    
    for k in range(n):
        Ag += Pas * f(a + k * Pas)
    
    for k in range(1, n + 1):
        Ad += Pas * f(a + k * Pas)
    
    for k in range(n):
        Am += Pas * f(a + (2 * k + 1) * PasM)
    
    for k in range(n):
        Trapeze += Pas * (f(a + k * Pas) + f(a + (k + 1) * Pas)) / 2
    
    print(f"Ag = {Ag}\nAd = {Ad}\nAm = {Am}\nTrapeze = {Trapeze}")
    
    # Affichage du graphique
    plt.figure(figsize=(10, 6))
    
    # Tracé de la fonction
    plt.plot(x_vals, y_vals, label=f"f(x) = {f(1)}", color="black", linewidth=2)
    
    # Affichage des points d'évaluation
    plt.scatter(x_Ag, y_Ag, color="red", s=5, label="Points Gauche (Ag)")
    plt.scatter(x_Ad, y_Ad, color="blue", s=5, label="Points Droite (Ad)")
    plt.scatter(x_Am, y_Am, color="green", s=5, label="Points Milieu (Am)")
    plt.scatter(x_Trapeze, y_Trapeze, color="orange", s=5, label="Points Trapeze")
    
    # Légende et affichage
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Intégration numérique par différentes méthodes")
    plt.legend()
    plt.grid()
    plt.show()

integrNumerique(0, math.pi*2)
# integrNumerique(1, 2)
# integrNumerique(-1, 1)
# integrNumerique(0, math.pi/4)


