import sympy as sp

def interpolation_lagrange(points):
    x = sp.Symbol('x')
    n = len(points)
    termes_simplifiés = []

    print("\n📌 Polynôme d'interpolation de Lagrange :\n")
    print("Formule générale :")
    print("   P(x) = Σ [ yᵢ × Lᵢ(x) ]\n")

    for i in range(n):
        xi, yi = points[i]
        Li = 1
        denominateur = 1
        numerateur_texte = []

        print(f"🔹 Étape {i+1} : Calcul de L{i}(x)")

        for j in range(n):
            if i != j:
                xj = points[j][0]
                numerateur_texte.append(f"(x - {xj})")
                Li *= (x - xj)
                denominateur *= (xi - xj)

        Li_expr = Li / denominateur
        Li_simplifie = sp.expand(Li_expr)

        print(f"   ➤ L{i}(x) = {' * '.join(numerateur_texte)} / ({denominateur})")
        print(f"     = {Li} / {denominateur}")
        print(f"     = {Li_simplifie}\n")

        yi_Li_simplifie = sp.expand(yi * Li_expr)

        print(f"   ➤ y{i} × L{i}(x) = {yi} × ({Li_expr}) = {yi_Li_simplifie}\n")

        termes_simplifiés.append(yi_Li_simplifie)

    # 🧮 Construction de P(x) complet
    print("🧮 Construction de P(x) complet (avant simplification) :\n")

    p_non_simplifie = " + ".join([f"({str(term)})" for term in termes_simplifiés])
    print(f"   P(x) = {p_non_simplifie}\n")

    p_simplifie = sp.expand(sum(termes_simplifiés))

    print("✅ Résultat final :")
    print(f"   P(x) = {p_simplifie}\n")

def demander_points():
    print("🧮 Entrée des points pour l'interpolation de Lagrange")
    try:
        n = int(input("🔢 Nombre de points : "))
        points = []
        for i in range(n):
            x = float(input(f"  ➤ x{i} : "))
            y = float(input(f"  ➤ y{i} : "))
            points.append((x, y))
        return points
    except Exception as e:
        print(f"❌ Erreur : {e}")
        return []

# === Lancement du programme ===
if __name__ == "__main__":
    points = demander_points()
    if points:
        interpolation_lagrange(points)
