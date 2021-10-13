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
    lab = niveau_1
    print("   ", end="")
    for ligne in range (0, len(lab)) :                                          #fonction qui donne les coordonnées des cases
        print("%1d" % (ligne%10), end="")
    print("  ", col,lin)

    for ligne in range (0, len(lab)) :                                          # Ce paragraphe affiche les informations de jeu avec les coordonnées
        print("%2d " % ligne, end="")
        if ligne != lin :
           print(lab[ligne])
        else :
            print(lab[ligne][0 : col-0]  + '*' +  lab[ligne][col+1 : ])

def choix_joueur() :
    reponse = ' '
    while not (reponse in "ZQSDzqsd2684*") :                                    #Si entée incorrecte
        reponse = input("Quel déplacement (Z,Q,S,D,2,6,8,4) ou quitter (*) ? ") #redemande l'entrée
    return reponse


def jeu(lab) :                                                                  #Defini le labyrinthe avec la position initial
    perso_col = 1
    perso_lin = 1
    reponse = ' '

    while reponse != '*' :
        print(" ")
        affiche_labyrinthe(lab,perso_col,perso_lin)                             #Affiche le labyrinthe et le choix du joueur
        reponse = choix_joueur()
        print(" ")
        print("Touche actionnée:"+reponse)



def k() :
    jeu(niveau_1)

k()
