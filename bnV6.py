##################################################################################
#                                                                                #
#                                                                                #
#             ~ Voici la partie python de notre bataille navale ~                #
#                                                                                #
#                                                                                #
##################################################################################


# Fonction pour créer la grille
def creer_grille():
    # Demande le nombre de lignes et de colonnes
    lignes = int(input(" - Entrez le nombre de lignes : "))
    colonnes = int(input(" - Entrez le nombre de colonnes : "))
    
    # Crée une grille remplie de 0
    grille = [[0 for _ in range(colonnes)] for _ in range(lignes)]
    return grille

# Fonction pour demander les tailles des bateaux
def demander_bateaux():
    tailles = []
    nb_bateaux = int(input(" - Combien de bateaux voulez-vous ? "))

    for i in range(nb_bateaux):
        taille = int(input(f" - Taille du bateau {i+1} : "))
        tailles.append(taille)
    
    return tailles

# Fonction pour vérifier si un bateau peut être placé
def peut_placer(grille, x, y, taille, horizontal):
    # Vérifie si le bateau dépasse la grille ou chevauche un autre bateau
    for i in range(taille):
        if horizontal:
            if y + i >= len(grille[0]) or grille[x][y + i] != 0:
                return False
        else:
            if x + i >= len(grille) or grille[x + i][y] != 0:
                return False
    return True

# Fonction pour placer un bateau
def placer_bateau(grille, taille, joueur):
    print(f"Joueur {joueur}, placez un bateau de taille {taille}")
    while True:
        # Demande les coordonnées
        x = int(input(f" - Ligne (0-{len(grille)-1}) : "))
        y = int(input(f" - Colonne (0-{len(grille[0])-1}) : "))
        horizontal = input(" - Horizontal ? (o/n) : ").lower() == 'o'

        # Vérifie si le placement est possible
        if peut_placer(grille, x, y, taille, horizontal):
            # Place le bateau
            for i in range(taille):
                if horizontal:
                    grille[x][y + i] = joueur
                else:
                    grille[x + i][y] = joueur
            break
        else:
            print("Placement impossible. Réessayez.")

# Fonction pour afficher la grille
def afficher_grille(grille):
    print("Grille :")
    for ligne in grille:
        print(" ".join(str(cell) for cell in ligne))
    print()

# Fonction principale pour jouer
def jouer(grille):
    while True:
        # Tour du joueur 1
        print("Tour du Joueur 1")
        x = int(input(" - Ligne pour tirer : "))
        y = int(input(" - Colonne pour tirer : "))

        if grille[x][y] == 0:
            grille[x][y] = 'X'
            print("Coup dans l'eau !")
        elif grille[x][y] == 2:
            grille[x][y] = 'O'
            print("Touché !")
        else:
            print("Déjà tiré ici ou bateau du Joueur 1.")
        afficher_grille(grille)

        # Tour du joueur 2
        print("Tour du Joueur 2")
        x = int(input(" - Ligne pour tirer : "))
        y = int(input(" - Colonne pour tirer : "))

        if grille[x][y] == 0:
            grille[x][y] = 'X'
            print("Coup dans l'eau !")
        elif grille[x][y] == 1:
            grille[x][y] = 'O'
            print("Touché !")
        else:
            print("Déjà tiré ici ou bateau du Joueur 2.")
        afficher_grille(grille)

# Programme principal
print("Bienvenue dans notre Bataille Navale !")

# Crée la grille
grille = creer_grille()

# Demande les tailles des bateaux
tailles_bateaux = demander_bateaux()

# Placement des bateaux pour chaque joueur
for joueur in [1, 2]:
    print(f"\nPlacement des bateaux pour le Joueur {joueur}")
    for taille in tailles_bateaux:
        placer_bateau(grille, taille, joueur)
    afficher_grille(grille)

# Lancement du jeu
print("\nDébut de la partie !")
jouer(grille)

# Lancement du jeu
jouer(grille)
