def creer_grille(lignes, colonnes):
    """
    Crée une grille vide avec des cases qui egal 0
    
    Paramètres :
    - lignes : Le nombre de lignes de la grille
    - colonnes : Le nombre de colonnes de la grille
    
    Renvoie :
    - Une grille avec toutes les cases a 0
    
    """
    return [[0 for _ in range(colonnes)] for _ in range(lignes)]

def demander_taille_plateau():
    """
    Demande aux joueurs la taille du plateau de jeu ligne colonnes
    
    Renvoie :
    - lignes : Le nombre de lignes du plateau
    - colonnes : Le nombre de colonnes du plateau
    """
    lignes = int(input(" - Entrez le nombre de lignes du plateau : "))
    while lignes < 2:
        print("La taille minimale du plateau est 2")
        lignes = int(input(" - Entrez le nombre de lignes du plateau : "))
    colonnes = int(input(" - Entrez le nombre de colonnes du plateau : "))
    while colonnes < 2:
        print("La taille minimale du plateau est 2")
        colonnes = int(input(" - Entrez le nombre de colonnes du plateau : "))
    return lignes, colonnes

def demander_bateaux():
    """
    Demande combien de bateaux les joueurs veulent et leurs tailles
    
    Renvoie :
    - tailles : Liste des tailles des bateaux
    """
    tailles = []
    nb_bateaux = int(input(" - Combien de bateaux voulez-vous ? "))
    for i in range(nb_bateaux):
        taille = int(input(f" - Taille du bateau {i+1} : "))
        tailles.append(taille)
    return tailles

def peut_placer(grille, x, y, taille, horizontal):
    """
    Vérifie si un bateau peut être placé à la position donnée
    
    Paramètres :
    - grille : La grille de jeu
    - x : La ligne où commencer
    - y : La colonne où commencer
    - taille : La taille du bateau
    - horizontal : True si horizontal, False si vertical
    
    Renvoie :
    - True si le bateau peut être placé, False sinon
    """
    for i in range(taille):
        if horizontal:
            if y + i >= len(grille[0]) or grille[x][y + i] != 0:
                return False
        else:
            if x + i >= len(grille) or grille[x + i][y] != 0:
                return False
    return True

def placer_bateau(grille, taille, joueur):
    """
    Demande au joueur de placer un bateau de taille donnée
    
    Paramètres :
    - grille : La grille de jeu
    - taille : La taille du bateau
    - joueur : lidentifiant du joueur (1 ou 2)
    """
    print(f"Joueur {joueur}, placez un bateau de taille {taille}")
    placer = False
    while placer == False:
        x = int(input(f" - Ligne (0-{len(grille)-1}) : "))
        y = int(input(f" - Colonne (0-{len(grille[0])-1}) : "))
        orientation = input(" - Orientation (h pour horizontal, v pour vertical) : ").lower()
        horizontal = (orientation == 'h')
        if peut_placer(grille, x, y, taille, horizontal):
            for i in range(taille):
                if horizontal:
                    grille[x][y + i] = joueur
                else:
                    grille[x + i][y] = joueur
            placer = True
        else:
            print("Placement impossible reessayez")

def afficher_grille(grille, joueur):
    """
    Affiche la grille du joueur avec les bateaux visibles et les cases vides.
    
    Paramètres :
    - grille : La grille de jeu.
    - joueur : L'identifiant du joueur (1 ou 2).
    """
    for ligne in grille:
        for elt in ligne:
            if elt == joueur:
                print("B", end=" ")
            elif elt == 0:
                print("0", end=" ")
            elif elt == 'X' or elt == 'O':
                print(elt, end=" ")
            else:
                print("0", end=" ")
        print()

def a_encore_bateaux(grille, joueur):
    """
    Vérifie si un joueur a encore des bateaux sur la grille
    
    
    Paramètres :
    - grille : La grille du joueur
    - joueur : L'identifiant du joueur (1 ou 2).
    
    Renvoie :
    - True si le joueur a encore des bateaux, False sinon.
    """
    for ligne in grille:
        if joueur in ligne:
            return True
    return False

def demander_tir(joueur):
    """
    Demande ou le joueur veut tirer
    
    Paramètres :
    - joueur : L'identifiant du joueur 1 ou 2
    
    Renvoie :
    - x : La ligne où tirer.
    - y : La colonne où tirer.
    """
    print(f"Joueur {joueur}, c'est a vous de tirer.")
    x = int(input(" - Ligne pour tirer : "))
    y = int(input(" - Colonne pour tirer : "))
    return x, y

def jouer(grille_j1, grille_j2):
    """
    Joue une partie entre les deux joueur
    
    Paramètres :
    - grille_j1 : La grille du joueur 1.
    - grille_j2 : La grille du joueur 2.
    """
    tour = 1
    partie_terminee = False

    while partie_terminee == False:
        if tour == 1:
            print("Tour du Joueur 1")
            x, y = demander_tir(1)

            while grille_j2[x][y] == 'X' or grille_j2[x][y] == 'O':
                print("Vous avez déjà tiré ici, réessayez.")
                x, y = demander_tir(1)

            if grille_j2[x][y] == 0:
                grille_j2[x][y] = 'X'
                print("Coup dans l'eau !")
            elif grille_j2[x][y] == 2:
                grille_j2[x][y] = 'O'
                print("Touché !")
            
            afficher_grille(grille_j2, 1)

            if a_encore_bateaux(grille_j2, 2) == False:
                print("Le Joueur 1 gagne !")
                partie_terminee = True

            tour = 2
        else:
            print("Tour du Joueur 2")
            x, y = demander_tir(2)

            while grille_j1[x][y] == 'X' or grille_j1[x][y] == 'O':
                print("Vous avez déjà tiré ici, réessayez.")
                x, y = demander_tir(2)

            if grille_j1[x][y] == 0:
                grille_j1[x][y] = 'X'
                print("Coup dans l'eau !")
            elif grille_j1[x][y] == 1:
                grille_j1[x][y] = 'O'
                print("Touché !")

            afficher_grille(grille_j1, 2)

            if a_encore_bateaux(grille_j1, 1) == False:
                print("Le Joueur 2 gagne !")
                partie_terminee = True

            tour = 1

print("Bienvenue dans notre jeu de Bataille Navale !")

print("taille du plateau de jeu")
lignes, colonnes = demander_taille_plateau()

grille_j1 = creer_grille(lignes, colonnes)
grille_j2 = creer_grille(lignes, colonnes)

tailles_bateaux = demander_bateaux()

print("Placement des bateaux pour le Joueur 1")
for taille in tailles_bateaux:
    placer_bateau(grille_j1, taille, 1)
afficher_grille(grille_j1, 1)

print("Placement des bateaux pour le Joueur 2")
for taille in tailles_bateaux:
    placer_bateau(grille_j2, taille, 2)
afficher_grille(grille_j2, 2)

print("Début de la partie !")
jouer(grille_j1, grille_j2)
