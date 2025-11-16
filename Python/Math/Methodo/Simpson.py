import math

# Génère la fonction f(x) à partir d'une expression texte
def create_function(expr):
    def f(x):
        return eval(expr, {"x": x, "math": math, "exp": math.exp})
    return f

# Méthode de Simpson pour n = 2
def simpson(f, a, b):
    print(f"\n📐 Méthode de Simpson sur [{a}, {b}] avec 2 sous-intervalles")

    h = (b - a) / 2
    x0 = a
    x1 = a + h
    x2 = b

    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)

    print(f"\n🧮 Points de calcul :")
    print(f"  x0 = {x0:.4f}, f(x0) = {f0:.6f}")
    print(f"  x1 = {x1:.4f}, f(x1) = {f1:.6f}")
    print(f"  x2 = {x2:.4f}, f(x2) = {f2:.6f}")

    approx = (h / 3) * (f0 + 4 * f1 + f2)

    print(f"\n📊 Formule de Simpson :")
    print(f"  h = {(b - a)/2:.4f}")
    print(f"  Intégrale ≈ (h/3) * [f(x0) + 4f(x1) + f(x2)]")
    print(f"           ≈ ({h}/3) * ({f0:.6f} + 4×{f1:.6f} + {f2:.6f})")
    print(f"           ≈ {approx:.6f}")

    return approx

# Partie interactive
print("📌 Approximation par la méthode de Simpson (n = 2 sous-intervalles)")
print("ℹ️ Utilisez 'x' pour la variable. Exemples : math.exp(x), x**2, math.sin(x)")

try:
    func_str = input("🔣 Entrer la fonction f(x) à intégrer : ")
    a = float(input("📍 Entrer la borne a : "))
    b = float(input("📍 Entrer la borne b : "))
    exact_str = input("🎯 Entrer la valeur exacte de l’intégrale (facultatif, sinon laisser vide) : ")

    f = create_function(func_str)
    approximation = simpson(f, a, b)

    if exact_str.strip():
        exact = float(eval(exact_str, {"math": math}))
        erreur = abs(exact - approximation)
        print(f"\n✅ Valeur exacte : {exact:.6f}")
        print(f"🔎 Erreur absolue : {erreur:.6f}")
    else:
        print("\nℹ️ Valeur exacte non fournie → Comparaison ignorée.")

except Exception as e:
    print(f"\n❌ Erreur : {e}")
