import math

def get_float_input(prompt):
    valeur = input(prompt).replace(" ", "")
    if valeur.lower() in ["pi", "π"]:
        return math.pi
    try:
        return float(eval(valeur, {"pi": math.pi, "e": math.e}))
    except Exception:
        raise ValueError(f"Entrée invalide : {valeur}")

def get_function(prompt):
    expr = input(prompt)
    def f(x):
        try:
            return eval(expr, {"x": x, "math": math})
        except Exception as e:
            print(f"Erreur lors de l'évaluation de la fonction : {e}")
            return float("nan")
    return f

def newton_method(g, g_prime, x0, iterations):
    print("\nÉtapes de la méthode de Newton :")
    print(f"{'Itération':^10} | {'x_n':^10} | {'g(x_n)':^12} | {'g(x_n)':^12} | {'x_n+1':^14}")
    print("-" * 70)

    x = x0
    historique = []

    for i in range(iterations + 1):
        gx = g(x)
        gpx = g_prime(x)

        if gpx == 0:
            print(f"{i:^10} | {x:^10.6f} | {gx:^12.6f} | {'0.000000':^12} | {'Indéfini':^14}")
            print("Division par zéro détectée. Fin du calcul.")
            break

        x_next = x - gx / gpx

        print(f"{i:^10} | {x:^10.6f} | {gx:^12.6f} | {gpx:^12.6f} | {x_next:^14.10f}")

        historique.append((x, gx, gpx, x_next))
        x = x_next

    # Justification
    print("\nJustification des calculs :")
    for i, (x, gx, gpx, x_next) in enumerate(historique):
        print(f"{i}. x{i+1} = x{i} - g(x{i}) / g'(x{i}) = {x:.6f} - ({gx:.6f}) / ({gpx:.6f}) = {x_next:.10f}")

# ==== Utilisation ====
print("=== Méthode de Newton ===")
g = get_function("Entrer la fonction g(x) (ex: math.cos(x) - x) : ")
g_prime = get_function("Entrer la dérivée g'(x) (ex: -math.sin(x) - 1) : ")
x0 = get_float_input("Entrer le point de départ x0 : ")
iterations = int(input("Entrer le nombre d'itérations à effectuer : "))

newton_method(g, g_prime, x0, iterations)
