import math

def get_float_input(prompt):
    valeur = input(prompt).replace(" ", "")
    if valeur.lower() in ["pi", "π"]:
        return math.pi
    try:
        return float(eval(valeur, {"pi": math.pi, "e": math.e}))
    except:
        raise ValueError(f"Entrée invalide : {valeur}")

def get_function():
    expr = input("Entrer la fonction f(x) : ")
    def f(x):
        try:
            return eval(expr, {"x": x, "math": math})
        except (OverflowError, ZeroDivisionError):
            return 0
    return f, expr

def dichotomie(f, expr, a, b, epsilon):
    print("\nÉtapes de la méthode de la dichotomie :")
    print("Itération  |     a      |     b      |   x_milieu   |   f(x_milieu)   |  f(a)*f(c)")
    print("-------------------------------------------------------------------------------------")

    i = 0
    c = (a + b) / 2
    f_c = f(c)
    produit = f(a) * f_c
    print(f"{i:^10} | {a:^10.5f} | {b:^10.5f} | {c:^12.5f} | {f_c:^15.5f} | {produit:^12.5f}")

    explications = [f"{i}. f(({a:.5f}+{b:.5f})/2) = f({c:.5f}) = {f_c:.5f} {'>' if f_c > 0 else '<' if f_c < 0 else '='} 0"]

    while b - a > epsilon:
        i += 1
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c = (a + b) / 2
        f_c = f(c)
        produit = f(a) * f_c
        changement = " <<== Changement (b ← c)" if f(a) * f(c) < 0 else " <<== Changement (a ← c)"
        print(f"{i:^10} | {a:^10.5f} | {b:^10.5f} | {c:^12.5f} | {f_c:^15.5f} | {produit:^12.5f}{changement}")

        signe = '>' if f_c > 0 else '<' if f_c < 0 else '='
        explication = f"{i}. f(({a:.5f}+{b:.5f})/2) = f({c:.5f}) = {f_c:.5f} {signe} 0"
        explications.append(explication)

    print("\nExplications supplémentaires :")
    for ligne in explications:
        print(ligne)

    print(f"\nValeur approchée de la racine : {c:.5f}")
    return c

# === Programme principal ===
print("=== Méthode de Dichotomie ===")
f, expr = get_function()
a = get_float_input("Entrer la borne inférieure a : ")
b = get_float_input("Entrer la borne supérieure b : ")
epsilon = get_float_input("Entrer la précision ε (ex: 0.01) : ")

dichotomie(f, expr, a, b, epsilon)
