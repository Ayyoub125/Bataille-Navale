# Grille de jeu (modulable)
# Fonction pour créer la grille
def grille1():
    grille = []
    nb_colonne = int(input(" - Entrez combien de colonnes voulez-vous ? "))
    nb_ligne = int(input(" - Entrez combien de lignes voulez-vous ? "))
    
    grille = [[0] * nb_ligne for _ in range(nb_colonne)]
    return grille

# Fonction pour définir les tailles des bateaux
def bateau():
    tailles_bateaux = []
    nb_bateau = int(input(" - Entrez combien de bateaux voulez-vous ? "))

    for i in range(nb_bateau):
        taille = int(input(f" - Entrez la taille du bateau {i+1} : "))
        tailles_bateaux.append(taille)
        
    return tailles_bateaux

# Fonction pour vérifier si un bateau peut être placé
def peut_placer_bateau(grille, x, y, taille_bateau, horizontal):
    """
    Vérifie si on peut placer un bateau à un certain endroit sans dépasser la grille ni chevaucher un autre bateau.
    
    Paramètres :
      - grille : la grille de jeu
      - x : la ligne de départ
      - y : la colonne de départ
      - taille_bateau : la taille du bateau
      - horizontal : True si le bateau est horizontal, False si vertical
    """
    for i in range(taille_bateau):
        if horizontal:
            if y + i >= len(grille[0]) or grille[x][y + i] != 0:
                return False
        else:
            if x + i >= len(grille) or grille[x + i][y] != 0:
                return False
    return True

# Fonction pour placer un bateau sur la grille
def placer_bateau(grille, taille_bateau, joueur):
    """
    Place un bateau sur la grille.
    Si joueur == 1, le bateau sera marqué par 1.
    Si joueur == 2, le bateau sera marqué par 2.
    """
    print(f"Joueur {joueur}, placez un bateau de taille {taille_bateau}")
    while True:
        x = int(input(f"Entrez la ligne (0-{len(grille)-1}) : "))
        y = int(input(f"Entrez la colonne (0-{len(grille[0])-1}) : "))
        horizontal = input("Voulez-vous placer le bateau horizontalement ? (o/n) : ").lower() == 'o'

        if peut_placer_bateau(grille, x, y, taille_bateau, horizontal):
            for i in range(taille_bateau):
                if horizontal:
                    grille[x][y + i] = joueur
                else:
                    grille[x + i][y] = joueur
            break
        else:
            print("Placement impossible. réessayez !")

# Fonction pour afficher la grille
def afficher_grille(grille):
    """
    Affiche la grille.
    """
    for ligne in grille:
        print(" ".join(str(cell) for cell in ligne))
    print()

# Fonction principale pour jouer
def jouer(grille):
    """
    Permet de jouer.
    """
    while True:
        # Tour du joueur 1
        print("Tour du Joueur 1")
        x = int(input("Entrez la ligne pour le tir : "))
        y = int(input("Entrez la colonne pour le tir : "))

        if grille[x][y] == 0:
            grille[x][y] = 'X'
            print("Coup dans l'eau !")
        elif grille[x][y] == 2:
            grille[x][y] = 'O'
            print("Touché !")
        else:
            print("Cet endroit a déjà été tiré ou tu ne peux pas tirer sur ton bateau.")
        afficher_grille(grille)

        # Tour du joueur 2
        print("Tour du Joueur 2")
        x = int(input("Entrez la ligne pour le tir : "))
        y = int(input("Entrez la colonne pour le tir : "))

        if grille[x][y] == 0:
            grille[x][y] = 'X'
            print("Coup dans l'eau !")
        elif grille[x][y] == 1:
            grille[x][y] = 'O'
            print("Touché !")
        else:
            print("Cet endroit a déjà été tiré ou tu ne peux pas tirer sur ton bateau.")
        afficher_grille(grille)

# Création de la grille et des bateaux
grille = grille1()
taille_bateaux = bateau()

# Placement des bateaux pour chaque joueur
for joueur in range(1, 3):
    print(f"Placement des bateaux pour le Joueur {joueur}")
    for taille in taille_bateaux:
        placer_bateau(grille, taille, joueur)
    afficher_grille(grille)

# Lancement du jeu
jouer(grille)
