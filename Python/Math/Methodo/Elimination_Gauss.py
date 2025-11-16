import re
import numpy as np

def parser_equation(equation):
    # Nettoyage de l'équation
    equation = equation.replace(" ", "")
    left, right = equation.split("=")
    right = float(right)

    # Capture des coefficients
    regex = re.compile(r'([+-]?[\d\.]*)(x|y|z)')
    coeffs = {'x': 0, 'y': 0, 'z': 0}
    
    for match in regex.finditer(left):
        val, var = match.groups()
        if val in ['', '+']:
            coeff = 1.0
        elif val == '-':
            coeff = -1.0
        else:
            coeff = float(val)
        coeffs[var] = coeff

    return [coeffs['x'], coeffs['y'], coeffs['z'], right]

def saisir_systeme_textuel():
    print("🔢 Entrez chaque équation sous la forme (ex : 2x + 3y + z = 14) :")
    equations = []
    for i in range(1, 4):
        eq = input(f"Équation {i} : ")
        row = parser_equation(eq)
        equations.append(row)
    return np.array(equations, dtype=float)

def afficher_ligne(ligne):
    return "[ " + " ".join(f"{val:.0f}" for val in ligne) + " ]"

def elimination_gauss(A):
    print("\n✅ Étape 1 : Matrice augmentée (A|B) initiale :")
    print(A, "\n")

    n = len(A)
    print("✅ Étape 2 : Élimination de Gauss :")

    for pivot in range(n - 1):
        for i in range(pivot + 1, n):
            if A[pivot][pivot] == 0:
                raise ValueError("Division par zéro détectée.")
            facteur = A[i][pivot] / A[pivot][pivot]
            ancienne_ligne = A[i].copy()
            A[i] = A[i] - facteur * A[pivot]
            print(f"→ Ligne {i+1} = Ligne {i+1} - ({facteur:.2f}) × Ligne {pivot+1} => {afficher_ligne(A[i])}")

        print(f"\nMatrice après pivot {pivot+1} :")
        print(A, "\n")
    
    return A

def substitution_inverse(A):
    print("✅ Étape 3 : Substitution inverse :")
    n = len(A)
    x = np.zeros(n)

    for i in reversed(range(n)):
        somme = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (A[i][n] - somme) / A[i][i]
        print(f"x{i+1} = ({A[i][n]} - {somme}) / {A[i][i]} = {x[i]:.4f}")

    print("\n✅ Solution finale :")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.4f}")

# --- Programme principal ---
print("🎯 Résolution d’un système linéaire 3x3 par la méthode de Gauss (entrée textuelle)")
matrice = saisir_systeme_textuel()
matrice = elimination_gauss(matrice)
substitution_inverse(matrice)
