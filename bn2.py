import random

# Grille de jeu (10x10)
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

# Tailles des bateaux à placer
tailles_bateaux = [3, 4, 2]  # Bateaux du premier joueur
tailles_bateaux2 = [3, 4, 2]  # Bateaux du deuxième joueur

def peut_placer_bateau(grille, x, y, taille_bateau, horizontal):
    """
    Vérifie si on peut placer un bateau à un certain endroit sans dépasser la grille ni chevaucher un autre bateau.
    
    Paramètres :
    grille (list)
    x (int)
    y (int)
    taille_bateau (int)
    horizontal.
    """
    for i in range(taille_bateau):
        if horizontal:
            if y + i >= len(grille[0]) or grille[x][y + i] != 0:
                return False
        else:
            if x + i >= len(grille) or grille[x + i][y] != 0:
                return False
    return True

def afficher_grille(grille):
    """
    Affiche la grille
    
    Paramètres :
    grille
    """
    for ligne in grille:
        print(ligne)


def jouer():
    """
    Permet de jouer 
    """
    while True:
        
        # Demande les coordonnées du tir pour le joueur 1
        x = int(input("Entrez la ligne (0-9) pour le tir du joueur 1 : "))
        y = int(input("Entrez la colonne (0-9) pour le tir du joueur 1 : "))
        
        if grille[x][y] == 0:
            grille[x][y] = 'X'  # Met un 'X' si tir raté
            afficher_grille(grille)
            print("Coup dans l'eau")
        elif grille[x][y] == 1 or grille[x][y] == 2:
            grille[x][y] = 'O'  # Met un 'O' si tir touché
            afficher_grille(grille)
            print("Touché")
        else:
            print("Cet endroit a déjà été tiré.")

        # Demande les coordonnées du tir pour le joueur 2
        x = int(input("Entrez la ligne (0-9) pour le tir du joueur 2 : "))
        y = int(input("Entrez la colonne (0-9) pour le tir du joueur 2 : "))
        
        if grille[x][y] == 0:
            grille[x][y] = 'X'  # Met un 'X' si tir raté
            afficher_grille(grille)
            print("Coup dans l'eau")
        elif grille[x][y] == 1 or grille[x][y] == 2:
            grille[x][y] = 'O'  # Met un 'O' si tir touché
            afficher_grille(grille)
            print("Touché")
        else:
            print("Cet endroit a déjà été tiré.")
        
# Place les bateaux du premier joueur
for taille in tailles_bateaux:
    placer_bateau(grille, taille)

# Place les bateaux du deuxième joueur
for taille in tailles_bateaux2:
    placer_bateau2(grille, taille)

# Affiche la grille après placement des bateaux
afficher_grille(grille)

# Lancer le jeu
jouer()
