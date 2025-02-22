# Grille de jeu (modulable)
def grille1():
    grille = []
    nb_colonne = int(input(" -Entrez combien de colonne voulez vous ? "))
    nb_ligne = int(input(" -Entrez combien de ligne voulez vous ? "))
    
    grille = [ [0] * nb_ligne for i in range(nb_colonne) ]

    return grille

grille = grille1() 

# Tailles des bateaux à placer
def bateau():
    tailles_bateaux = []

    nb_bateau = int(input(" -Entrez combien de bateau voulez vous ? "))

    for i in range(nb_bateau):
        taille = int(input(" -Entrez la taille du/des bateaux "))

        tailles_bateaux.append(taille)
        
    return tailles_bateaux


taille_bateaux = bateau()

def placer_bateau(grille, taille_bateau, joueur):
    """
    Place un bateau sur la grille
    Si joueur == 1, le bateau sera marquer  1 
    Si joueur == 2, le bateau sera marquer  2 
    """
    x =
    y = 
        


def peut_placer_bateau(grille, x, y, taille_bateau, horizontal):
    """
    Vérifie si on peut placer un bateau à un certain endroit sans dépasser la grille ni chevaucher un autre bateau.
    
    Parametres :
      - grille 
      - x 
      - y 
      - taille_bateau 
      - horizontal 
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
        while x < 0 or x > 9:
            print("Le nombre pour la ligne doit être entre 0 et 9")
            x = int(input("Entrez la ligne (0-9) pour le tir du joueur 1 : "))
            
        y = int(input("Entrez la colonne (0-9) pour le tir du joueur 1 : "))
        while y < 0 or y > 9:
            print("Le nombre pour la colonne doit être entre 0 et 9")
            y = int(input("Entrez la colonne (0-9) pour le tir du joueur 1 : "))
        
        if grille[x][y] == 0:
            grille[x][y] = 'X' 
            afficher_grille(grille)
            print("Coup dans l'eau")
        elif grille[x][y] == 2:
            grille[x][y] = 'O'  
            afficher_grille(grille)
            print("Touché")
        else:
            print("Cet endroit a déjà été tiré ou tu ne peux pas tirer sur ton bateau")

        # Demande les coordonnées du tir pour le joueur 2
        x = int(input("Entrez la ligne (0-9) pour le tir du joueur 2 : "))
        while x < 0 or x > 9:
            print("Le nombre pour la ligne doit être entre 0 et 9")
            x = int(input("Entrez la ligne (0-9) pour le tir du joueur 2 : "))
            
        y = int(input("Entrez la colonne (0-9) pour le tir du joueur 2 : "))
        while y < 0 or y > 9:
            print("Le nombre pour la colonne doit être entre 0 et 9")
            y = int(input("Entrez la colonne (0-9) pour le tir du joueur 2 : "))
        
        if grille[x][y] == 0:
            grille[x][y] = 'X'  
            afficher_grille(grille)
            print("Coup dans l'eau")
        elif grille[x][y] == 1:
            grille[x][y] = 'O'  
            afficher_grille(grille)
            print("Touché")
        else:
            print("Cet endroit a déjà été tiré ou tu ne peux pas tirer sur ton bateau")


for joueur in range(1, 3):
    for taille in taille_bateaux:
        placer_bateau(grille, taille, joueur)

# Affiche la grille après placement des bateaux
afficher_grille(grille)

# Lancer le jeu
jouer()
