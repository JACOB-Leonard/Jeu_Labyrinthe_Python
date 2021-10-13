################################################################################
#
#           Programmme Final du labyrinthe
#
#           Léonard Jacob TS2  /  2019
#
################################################################################


def affiche_bordure(taille) :                                                   #Affiche les bordure d'un labyrinthe
    longueur = "+" + taille*"-" + "+"                                           #Definition de la première et dernière ligne (avec pour longueur taille)
    largeur  = "|" + taille*" " + "|"                                           #Definition des lignes intermediaire  (avec pour espace blanc =taille)

    print(longueur)
    for compteur in range (0, taille) :                                         # print le nombre de ligne definit par la taille du labyrinthe
        print(largeur)
    print(longueur)

def barre_score(num_niveau) :                                                   # indique le numero du labyrinthe
    print(" niveau : {:3d}".format(num_niveau))                                 # :3d aide à afficher proprement

def affiche_labyrinthe(lab, perso_tete, perso_cl, num_niveau) :
    '''
        lab: labyrinthe
        perso_tete: symbole correspondantau personnage
        num_niveau correspond au premier niveau
    '''
    perso_col = perso_cl[0]
    perso_lin = perso_cl[1]

    print("   ", end="")
    for ligne in range (0, len(lab)) :                                          #fonction qui donne les coordonnées des cases
        print("%1d" % (ligne%10), end="")
    barre_score(num_niveau)                                                     # Ce paragraphe affiche les informations de jeu avec le score et les coordonnées

    for ligne in range (0, len(lab)) :
        print("%2d " % ligne, end="")
        if ligne == perso_lin :
            print(lab[perso_lin][0 : perso_col-0]
                + perso_tete
                + lab[perso_lin][perso_col+1 : ])                               #Imprime le début du labyrinthe, le personnage puis la fin du labyrinthe
        else :
            print(lab[ligne])                                                   #Imprime la ligne



def verification_deplacement(lab, col, lin) :                                   # Cette fonction verifie la possibilité d'un deplacement
    if lin < 0              : return False
    if lin > len(lab)       : return False
    if col < 0              : return False
    if col > len(lab[lin])  : return False
    if lab[lin][col] == '●' : return True                                       #Si le joueur atteind les coordonnées d'arrivé
    if lab[lin][col] == ' ' : return True                                       # ou si il rencontre du vide il peut avancer
    return False


def choix_joueur(lab, perso_cl) :                                               #Programme les deplacements du joueur
    reponse = ' '
    while not (reponse in "ZQSDzqsd2684*") :                                    #Vérifie que la touche de déplacement et valide
        reponse = input("Quel déplacement (Z,Q,S,D,2,6,8,4) ou quitter (*) ? ")
        if reponse == '' : # Réponse vide
            reponse = " "

    if reponse == '*' : # Quitter définitivement
        exit(0)

    perso_col = perso_cl[0]
    perso_lin = perso_cl[1]

    if reponse in "Zz8" : # Monter
        if verification_deplacement(lab, perso_col+0, perso_lin-1) :            #Monte de 1 ligne
            perso_lin -= 1
    if reponse in "Ss2" : # Descendre
        if verification_deplacement(lab, perso_col+0, perso_lin+1) :            #Descend de 1 ligne
            perso_lin += 1
    if reponse in "Qq4" : # Gauche
        if verification_deplacement(lab, perso_col-1, perso_lin+0) :            #Descend de 1 Colonne
           perso_col -= 1
    if reponse in "Dd6" : # Droite
        if verification_deplacement(lab, perso_col+1, perso_lin+0) :            #Monte de 1 Colonne
            perso_col += 1

    return [ perso_col, perso_lin ]                                             #Applique le changement de position


def Fin(lab, perso_cl) :
    print (perso_cl[0],perso_cl[1])
    if lab[perso_cl[1]][perso_cl[0]] == '●' : return True                       #Vérifie si le joueurn est arrivé
    return False


def jeu(lab,num_nivau) :
    perso_Tete = 'X'
    perso_CL = [ 1 , 1 ]                                                        #Position de depart du personnage

    while not Fin(lab, perso_CL) :
        affiche_labyrinthe(lab, perso_Tete, perso_CL,num_niveau)
        perso_CL = choix_joueur(lab, perso_CL)                                  #Change les coordonnées du personnage jusqu'a la fin du labyrinthe


def charge_labyrinthe(nom) :
    f = open(nom + ".txt", "r", encoding='utf-8')                               #Ouvre le fichier / encoding utf8 charge les caractère speciaux
    lab = tuple(f.read().splitlines())                                          # effectue une lecture du labyrinthe ligne par ligne
    f.close()                                                                   #Stop la lecture du fichier
    return lab


#-----------------------------------------------------------
#   Programme principal
#------------------------------------------------------------

nb_niveaux = 30                                                                 #nombre de niveau
#niveau_1 = charge_labyrinthe("niveau_1")

for num_niveau in range(1,nb_niveaux +1) :                                      #Charge le labyrinthe suivant
    niveau = charge_labyrinthe("niveau_"+ str(num_niveau))
    jeu(niveau,num_niveau)

