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

def secante(f, expr, x0, x1, epsilon, max_iter=100):
    print("\nÉtapes de la méthode de la sécante :")
    print("Itération  |     x0     |     x1     |    f(x0)    |    f(x1)    |    x2 (nouveau)   ")
    print("--------------------------------------------------------------------------------------")

    i = 0
    f_x0 = f(x0)
    f_x1 = f(x1)
    explications = []

    while abs(x1 - x0) > epsilon and i < max_iter:
        if f_x1 - f_x0 == 0:
            print("Division par zéro détectée, méthode interrompue.")
            break

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        print(f"{i:^10} | {x0:^10.5f} | {x1:^10.5f} | {f_x0:^10.5f} | {f_x1:^10.5f} | {x2:^17.5f}")

        explications.append(
            f"{i}. x2 = x1 - f(x1)*(x1 - x0)/(f(x1)-f(x0)) = "
            f"{x1:.5f} - {f_x1:.5f}*({x1:.5f}-{x0:.5f})/({f_x1:.5f}-{f_x0:.5f}) = {x2:.5f}"
        )

        x0, x1 = x1, x2
        f_x0, f_x1 = f_x1, f(x1)
        i += 1

    print("\nExplications supplémentaires :")
    for ligne in explications:
        print(ligne)

    if i == max_iter:
        print("\n⚠ Nombre maximal d’itérations atteint.")
    else:
        print(f"\n✅ Valeur approchée de la racine : {x1:.5f}")

    return x1

# === Programme principal ===
print("=== Méthode de la Sécante ===")
f, expr = get_function()
x0 = get_float_input("Entrer la première approximation x0 : ")
x1 = get_float_input("Entrer la deuxième approximation x1 : ")
epsilon = get_float_input("Entrer la précision ε (ex: 0.01) : ")

secante(f, expr, x0, x1, epsilon)