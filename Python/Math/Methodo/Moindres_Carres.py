import matplotlib.pyplot as plt

def saisir_points():
    print("=== Saisie des points expérimentaux ===")
    points = []
    n = int(input("Combien de points souhaitez-vous entrer ? "))
    for i in range(n):
        x = float(input(f"  x{i} = "))
        y = float(input(f"  y{i} = "))
        points.append((x, y))
    return points

def moindres_carres(points):
    n = len(points)
    somme_x = sum(x for x, y in points)
    somme_y = sum(y for x, y in points)
    somme_x2 = sum(x**2 for x, y in points)
    somme_xy = sum(x * y for x, y in points)

    print("\n=== Méthode des moindres carrés ===")
    print("\n1. Données expérimentales :")
    for i, (x, y) in enumerate(points):
        print(f"   Point {i} : (x = {x}, y = {y})")

    print("\n2. Calcul des sommes nécessaires :")
    print(f"   n       = {n}")
    print(f"   Σx      = {somme_x}")
    print(f"   Σy      = {somme_y}")
    print(f"   Σx²     = {somme_x2}")
    print(f"   Σxy     = {somme_xy}")

    print("\n3. Système d'équations normales :")
    print(f"   a * {somme_x2} + b * {somme_x} = {somme_xy}")
    print(f"   a * {n} + b * {somme_x} = {somme_y}")

    det = somme_x2 * n - somme_x * somme_x
    a = (somme_xy * n - somme_x * somme_y) / det
    b = (somme_x2 * somme_y - somme_x * somme_xy) / det

    print("\n4. Résolution du système :")
    print(f"   Dét = {somme_x2}*{n} - {somme_x}² = {det}")
    print(f"   a   = ({somme_xy}*{n} - {somme_x}*{somme_y}) / {det} = {a:.4f}")
    print(f"   b   = ({somme_x2}*{somme_y} - {somme_x}*{somme_xy}) / {det} = {b:.4f}")

    print("\n5. Validation : Somme des carrés des écarts :")
    somme_ecarts_carres = 0
    for x, y in points:
        y_pred = a * x + b
        ecart = y - y_pred
        ecart_carre = ecart**2
        somme_ecarts_carres += ecart_carre
        print(
            f"   Pour x = {x:.1f}, y = {y:.1f} → "
            f"y_pred = a*x + b = {a:.4f}*{x:.1f} + {b:.4f} = {y_pred:.4f}, "
            f"(écart)² = ({y:.4f} - {y_pred:.4f})² = {ecart_carre:.6f}"
        )

    print(f"\n   Somme des carrés des écarts : {somme_ecarts_carres:.6f}")
    print(f"\n➡️  Droite ajustée finale : y = {a:.4f}x + {b:.4f}")

    return a, b, points

def tracer_graphique(a, b, points):
    x_vals = [x for x, y in points]
    y_vals = [y for x, y in points]

    x_line = list(range(int(min(x_vals)) - 1, int(max(x_vals)) + 2))
    y_line = [a * x + b for x in x_line]

    plt.figure(figsize=(8, 5))
    plt.scatter(x_vals, y_vals, color='red', label='Points expérimentaux')
    plt.plot(x_line, y_line, color='blue', linestyle='--', label=f'Droite : y = {a:.2f}x + {b:.2f}')
    plt.title("Ajustement par la méthode des moindres carrés")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# --- Lancement du programme ---
points = saisir_points()
a, b, pts = moindres_carres(points)
tracer_graphique(a, b, pts)
