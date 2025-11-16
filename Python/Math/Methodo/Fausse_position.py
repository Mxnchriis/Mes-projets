import math

# Génère la fonction f(x) depuis une chaîne de caractères
def create_function(expr):
    def f(x):
        return eval(expr, {"x": x, "math": math})
    return f

# Implémentation de la méthode de la fausse position (n itérations)
def fausse_position(f, x1, x2, iterations):
    print(f"\n🎯 Méthode de la fausse position sur [{x1}, {x2}] pour {iterations} itérations")

    f1 = f(x1)
    f2 = f(x2)

    print(f"\nÉtape 1 : Vérification du changement de signe")
    print(f"  f({x1}) = {f1:.6f}")
    print(f"  f({x2}) = {f2:.6f}")

    if f1 * f2 > 0:
        print("⚠️ Pas de changement de signe → Méthode non applicable sur cet intervalle.")
        return

    for i in range(1, iterations + 1):
        numerator = f1 * (x2 - x1)
        denominator = f2 - f1
        x_new = x1 - numerator / denominator
        f_new = f(x_new)

        print(f"\n🧮 Itération {i}:")
        print(f"  x1 = {x1:.6f}, f(x1) = {f1:.6f}")
        print(f"  x2 = {x2:.6f}, f(x2) = {f2:.6f}")
        print(f"  x_new = x1 - f(x1) * (x2 - x1) / (f(x2) - f(x1))")
        print(f"        = {x1:.6f} - ({f1:.6f}) * ({x2:.6f} - {x1:.6f}) / ({f2:.6f} - {f1:.6f})")
        print(f"        = {x_new:.6f}, f(x_new) = {f_new:.6f}")

        # Mise à jour des bornes
        if f1 * f_new < 0:
            x2, f2 = x_new, f_new
        else:
            x1, f1 = x_new, f_new

    print(f"\n✅ Approximation finale de la racine après {iterations} itérations : x ≈ {x_new:.4f}")

# --- Partie interactive ---
print("📌 Méthode de la fausse position")
print("ℹ️ Utilisez 'x' dans votre fonction. Exemples : x**3 - 4*x + 1 ou math.sin(x) - x/2")

try:
    func_str = input("🔣 Entrer la fonction f(x) : ")
    f = create_function(func_str)

    x1 = float(input("🔢 Entrer x1 (borne gauche) : "))
    x2 = float(input("🔢 Entrer x2 (borne droite) : "))
    iterations = int(input("🔁 Nombre d’itérations à effectuer : "))

    fausse_position(f, x1, x2, iterations)

except Exception as e:
    print(f"❌ Erreur : {e}")
