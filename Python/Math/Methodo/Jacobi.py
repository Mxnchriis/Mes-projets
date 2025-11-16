import re

def parse_equation(eq):
    """Extrait les coefficients de x, y et le terme indépendant d'une équation comme '4x - y = 9'"""
    eq = eq.replace("−", "-")  # Remplace le tiret long Unicode par un tiret standard
    eq = eq.replace(" ", "")   # Supprime les espaces

    lhs, rhs = eq.split("=")

    # Ajout de * pour la détection des coefficients implicites
    lhs = re.sub(r'(?<![\d\.])x', '1*x', lhs)
    lhs = re.sub(r'(?<![\d\.])y', '1*y', lhs)
    lhs = re.sub(r'(?<=\d)(x)', '*x', lhs)
    lhs = re.sub(r'(?<=\d)(y)', '*y', lhs)

    # Recherche des coefficients
    a = re.search(r'([+-]?\d*\.?\d*)\*x', lhs)
    b = re.search(r'([+-]?\d*\.?\d*)\*y', lhs)

    a = float(a.group(1)) if a else 0.0
    b = float(b.group(1)) if b else 0.0
    c = float(rhs)

    return a, b, c

def jacobi_method_from_equations(eq1, eq2, iterations):
    print("\n🔍 Analyse des équations :")
    a11, a12, b1 = parse_equation(eq1)
    a21, a22, b2 = parse_equation(eq2)

    print(f"  Équation 1 : {a11}*x + {a12}*y = {b1}")
    print(f"  Équation 2 : {a21}*x + {a22}*y = {b2}")

    diagonale_dominante = abs(a11) > abs(a12) and abs(a22) > abs(a21)
    print("\n📏 Vérification de la diagonale dominante :")
    print(f"   |{a11}| > |{a12}| : {abs(a11)} > {abs(a12)}")
    print(f"   |{a22}| > |{a21}| : {abs(a22)} > {abs(a21)}")
    print("\n✅ Diagonale dominante\n" if diagonale_dominante else "⚠️ Diagonale NON dominante\n")

    if a11 == 0 or a22 == 0:
        print("❌ Division par zéro détectée (diagonale nulle). Annulation.")
        return

    print("🧾 Transformation du système en forme itérative :\n")

    # Équation 1 : isolement de x
    print(f"  Équation 1 : {a11}*x + ({a12})*y = {b1}")
    print(f"     ➤ Isolement de x :")
    print(f"       x = ({b1} - ({a12})*y) / {a11}")
    if a12 < 0:
        print(f"         = ({b1} + {abs(a12)}*y) / {a11}\n")
    else:
        print(f"         = ({b1} - {a12}*y) / {a11}\n")

    # Équation 2 : isolement de y
    print(f"  Équation 2 : {a21}*x + ({a22})*y = {b2}")
    print(f"     ➤ Isolement de y :")
    print(f"       y = ({b2} - ({a21})*x) / {a22}")
    if a21 < 0:
        print(f"         = ({b2} + {abs(a21)}*x) / {a22}\n")
    else:
        print(f"         = ({b2} - {a21}*x) / {a22}\n")


    xk, yk = 0, 0

    print("🔄 Itérations de Jacobi (détails complets) :")
    for k in range(1, iterations + 1):
        x_num = b1 - a12 * yk
        y_num = b2 - a21 * xk

        xk1 = x_num / a11
        yk1 = y_num / a22

        print(f"\n   🔁 Itération {k} :")
        print(f"      x({k}) = ({b1} - ({a12} * {yk:.6f})) / {a11} = {x_num:.6f} / {a11} = {xk1:.6f}")
        print(f"      y({k}) = ({b2} - ({a21} * {xk:.6f})) / {a22} = {y_num:.6f} / {a22} = {yk1:.6f}")

        xk, yk = xk1, yk1


# --- Interface interactive ---
print("📌 Méthode de Jacobi (entrer les équations directement)")
print("Format attendu : a*x + b*y = c  (ex : 4x - y = 8)")

try:
    eq1 = input("🧮 Entrer l'équation 1 : ")
    eq2 = input("🧮 Entrer l'équation 2 : ")
    iterations = int(input("🔁 Nombre d’itérations à effectuer : "))

    jacobi_method_from_equations(eq1, eq2, iterations)

except Exception as e:
    print(f"❌ Erreur : {e}")
