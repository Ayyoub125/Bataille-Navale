function 
'creer une liste qui fait affaire de terrain de jeu'

console.log(plateau_de_jeu.length);
// 100

###def mange_case(liste,ligne,colonne):
    """ elimine les 0 au-dessus et a droite de la case choisie """
    if liste[ligne][colonne]==1:
        return "case eliminee, rejouer"
    if liste[ligne][colonne]==0:
        for j in range(0,ligne+1):
            for i in range(colonne,len(liste[0])):
                liste[j][i]=1
    return liste###
