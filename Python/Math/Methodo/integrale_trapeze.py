import math

# Fonction pour générer f(x) depuis une expression sécurisée
def create_function(expr):
    def f(x):
        return eval(expr, {"x": x, "math": math})
    return f

# --- Entrée utilisateur ---
expr = input("Entrez la fonction f(x) (ex: x**2, math.sin(x), etc.) : ")
a = float(input("Entrez la borne inférieure a : "))
b = float(input("Entrez la borne supérieure b : "))
n = int(input("Entrez le nombre de sous-intervalles n : "))

# --- Étape 1 : Calcul des points ---
h = (b - a) / n
x_values = [a + i * h for i in range(n + 1)]
f = create_function(expr)
f_values = [f(x) for x in x_values]

# --- Étape 2 : Affichage des points ---
print("\nPoints x_i et f(x_i) :")
for i, (x, fx) in enumerate(zip(x_values, f_values)):
    print(f"   x_{i} = {x:.4f}, f(x_{i}) = {fx:.6f}")

# --- Étape 3 : Calcul détaillé de l’intégrale ---
print("\nDétail du calcul de l’intégrale par la méthode des trapèzes :")
print(f"   h = (b - a)/n = ({b} - {a})/{n} = {h:.4f}")

print("\n   Formule :")
print("   I ≈ (h/2) * [ f(x_0) + 2 * (f(x_1) + ... + f(x_{n-1})) + f(x_n) ]")

# Calcul de la somme
somme_interne = sum(f_values[1:-1])
approx = (h / 2) * (f_values[0] + 2 * somme_interne + f_values[-1])

# Affichage du détail du calcul :
fx0 = f_values[0]
fxn = f_values[-1]
print(f"\n   I ≈ ({h}/2) * [ {fx0:.6f} + 2 * ({' + '.join(f'{v:.6f}' for v in f_values[1:-1])}) + {fxn:.6f} ]")

print(f"     = ({h}/2) * [ {fx0:.6f} + 2 * {somme_interne:.6f} + {fxn:.6f} ]")
print(f"     = ({h}/2) * [ {fx0 + 2 * somme_interne + fxn:.6f} ]")
print(f"     = {approx:.6f}")

# --- Résultat final ---
print(f"\n✅ Approximation finale de l'intégrale : {approx:.6f}")
