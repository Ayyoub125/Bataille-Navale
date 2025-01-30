import random

# Grille de jeu
grille = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# variable de taille de bateau
tailles_bateaux = [3, 4, 2]
tailles_bateaux2 = [3, 4, 2]

# place un bateau sur la grille
def placer_bateau(taille_bateau):
    horizontal = random.choice([True, False])
    
    if horizontal:
        x = random.randint(0, len(grille) - 1)
        y = random.randint(0, len(grille[0]) - taille_bateau)
        for i in range(taille_bateau):
            grille[x][y + i] = 1
    else:
        x = random.randint(0, len(grille) - taille_bateau)
        y = random.randint(0, len(grille[0]) - 1)
        for i in range(taille_bateau):
            grille[x + i][y] = 1

def placer_bateau2(taille_bateau):
    horizontal = random.choice([True, False])
    
    if horizontal:
        x = random.randint(0, len(grille) - 1)
        y = random.randint(0, len(grille[0]) - taille_bateau)
        for i in range(taille_bateau):
            grille[x][y + i] = 2
    else:
        x = random.randint(0, len(grille) - taille_bateau)
        y = random.randint(0, len(grille[0]) - 1)
        for i in range(taille_bateau):
            grille[x + i][y] = 2

# Place les bateaux sur la grille 
for taille in tailles_bateaux:
    placer_bateau(taille)

for taille in tailles_bateaux2:
    placer_bateau2(taille)

# Affichage de la grille
print(grille) 
