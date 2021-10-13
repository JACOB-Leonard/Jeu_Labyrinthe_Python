################################################################################
#   Lab3  Léonard Jacob TS2  /  2019
################################################################################

niveau_1 = [
    "+-------+----------+",
    "|       |          |",
    "+----+  + +-----+  |",
    "|    |          |  |",
    "| +  +------+   |  |",
    "| |         |   |  |",
    "| +---+     +---+  |",
    "|     |            |",
    "+--+  +------------+",
    "|     |            |",
    "+--+  |   +        |",
    "|  |  +   |   +----+",
    "|  |      |        |",
    "|  +------+---+    |",
    "|             |    |",
    "|    +----+   +    |",
    "|    |             |",
    "| +--|   +---------+",
    "|    |             |",
    "+----+-------------+"  ]

def affiche_bordure(taille) :                                                   #Affiche les bordure d'un labyrinthe
    longueur = "+" + taille*"-" + "+"                                           #Definition de la première et dernière ligne (avec pour longueur taille)
    largeur  = "|" + taille*" " + "|"                                           #Definition des lignes intermediaire  (avec pour espace blanc =taille)

    print(longueur)                                                             # print le nombre de ligne definit par la taille du labyrinthe
    for compteur in range (0, taille) :
        print(largeur)
    print(longueur)


def affiche_labyrinthe(lab, col, lin) :
    '''
        lab: labyrinthe
        '''

    print("   ", end="")
    for ligne in range (0, len(lab)) :                                          #fonction qui donne les coordonnées des cases
        print("%1d" % (ligne%10), end="")
    print("  ", col,lin)                                                        # Ce paragraphe affiche les informations de jeu avec le score et les coordonnées

    for ligne in range (0, len(lab)) :
        print("%2d " % ligne, end="")
        if ligne != lin :                                                       #Si la ligne differente de celle du personnage
           print(lab[ligne])                                                    #Imprime la ligne
        else :                                                                  #Sinon ligne du personnage
            print(lab[ligne][0 : col-0]  + '*' +  lab[ligne][col+1 : ])         #Imprime le début du labyrinthe, le personnage puis la fin du labyrinthe



def verification_deplacement(lab, col, lin) :                                   # Cette fonction verifie la possibilité d'un deplacement
    if lin < 0              : return False
    if lin > len(lab)       : return False
    if col < 0              : return False
    if col > len(lab[lin])  : return False
    if lab[lin][col] != ' ' : return False
    print("Déplacement impossible")                                             #Indique un deplacement inpossible
    return True


def choix_joueur() :
    reponse = ' '
    while not (reponse in "ZQSDzqsd2684*") :                                    #Si touche entrée fausse
        reponse = input("Quel déplacement (Z,Q,S,D,2,6,8,4) ou quitter (*) ? ") # Redemande la touche à entrée
    return reponse


def jeu(lab) :                                                                  #Fontion jeu qui definit les condition de depart
    perso_col = 1
    perso_lin = 1
    reponse = ' '

    while reponse != '*' :
        affiche_labyrinthe(lab,perso_col,perso_lin)
        reponse = choix_joueur()
        """
        La programmation est defini dans la fonction jeu mais est dans choix_joueur pour le programme final
        """
        if reponse in "Zz8" : # Monter
            if verification_deplacement(lab, perso_col+0, perso_lin-1) :
                perso_lin -= 1
        if reponse in "Ss2" : # Descendre
            if verification_deplacement(lab, perso_col+0, perso_lin+1) :
                perso_lin += 1
        if reponse in "Qq4" : # Gauche
            if verification_deplacement(lab, perso_col-1, perso_lin+0) :
               perso_col -= 1
        if reponse in "Dd6" : # Droite
            if verification_deplacement(lab, perso_col+1, perso_lin+0) :
                perso_col += 1


def k() :
    jeu(niveau_1)

k()                                                                             #appelle la fonction jeu
