import numpy as np
import matplotlib.pyplot as plt
import dichotomie as dic
import secante as sec
import newton as new

def f(x):
    return x*x - 2

def derf(x):
    return 2*x

# Stocker les résultats des méthodes
x1, x2, result_dicho, iter_dicho = dic.dichotomie(f, 1, 2, 1e-6)
sol_sec, iter_sec = sec.secante(f, 1, 2, 1e-6)
# sol_newton, iter_newton, x_vals_newton = new.newton(f, derf, 1.5, 1e-6)

# Créer des listes d'itérations pour dichotomie et sécante
x_vals_dicho = [x1, x2]
x_vals_sec = [1, 2]

# Préparer le graphe
plt.figure(figsize=(8, 6))
plt.axhline(y=np.sqrt(2), color='black', linestyle='dashed', label="Racine réelle sqrt(2)")

plt.plot(range(len(x_vals_dicho)), x_vals_dicho, 'ro-', label='Dichotomie')
plt.plot(range(len(x_vals_sec)), x_vals_sec, 'bo-', label='Sécante')
# plt.plot(range(len(x_vals_newton)), x_vals_newton, 'go-', label='Newton')

plt.xlabel("Itérations")
plt.ylabel("Valeur de x")
plt.title("Convergence des méthodes numériques")
plt.legend()
plt.grid()
plt.show()
