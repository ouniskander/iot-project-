import numpy as np

# Création d'un tableau 2x3 avec des valeurs
a = np.array([[1, 2, 3], [5, 6, 9]])

# Affichage du tableau
print("Array:")
print(a)

# Calcul de la diagonale principale (de haut en bas à gauche à droite)
# Pour une matrice 2x3, il n'y a pas de diagonale carrée complète, 
# donc cela peut ne pas renvoyer les éléments attendus si c'est une matrice non carrée.
print("\nDiagonal (will be empty for non-square matrix):")
print(np.diag(a))

# Calcul de la trace
# La trace est la somme des éléments diagonaux, mais cela ne s'applique qu'aux matrices carrées
# Nous allons tester cela avec np.trace()
print("\nTrace of the matrix:")
print(np.trace(a))
