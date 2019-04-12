from Joueur import Joueur

class TicTacToe:

    joueur1=Joueur()
    joueur2 =Joueur()
    compteurCoupJoue=0
    gagnant=None
    joueurgagnant=None

    def __init__(self,):
        self.grille = [['?','?','?'],['?','?','?'],['?','?','?']]
        self.joueur1.nom="Joueur 1"
        self.joueur1.nom = "Joueur 2"
        self.joueur1.jeton='X'
        self.joueur2.jeton="O"
        self.joueur1.tour=True
        self.joueur2.tour = False
        self.gagnant=False

    def AfficherEtatJeu(self,):
        "Méthode permettant de pouvoir afficher le jeu "
        for i in range (3):
            print (self.grille[i])

    def JouerJeton(self,):

        print ("Veuillez choisir quelle ligne joué ")
        ligneX = int(input())
        print("Veuillez choisir quelle colonne ")
        colonneY = int(input())

        if self.grille[colonneY-1][ligneX-1]==self.joueur1.jeton or self.grille[colonneY-1][ligneX-1]==self.joueur2.jeton :
            while self.grille[colonneY-1][ligneX-1]== self.grille[colonneY-1][ligneX-1]==self.joueur1.jeton or self.grille[colonneY-1][ligneX-1]==self.joueur2.jeton:
                print ("Vous avez joué dans une case déjà prise ... Vous devez rejouer.")
                self.AfficherEtatJeu()
                print("Veuillez choisir quelle ligne joué ")
                ligneX = int(input())
                print("Veuillez choisir quelle colonne ")
                colonneY = int(input())


        if self.compteurCoupJoue %2 == 0:
           self.grille[colonneY-1][ligneX-1] = self.joueur1.jeton
        else:
           self.grille[colonneY - 1][ligneX - 1] = self.joueur2.jeton
        return self.grille

    def VerifierGagnant(self,):


        if self.grille[0][0]=='O' and self.grille[0][1] == 'O' and self.grille[0][2] == 'O':
            finpartie = True
            self.joueurgagnant = "Le joueur 2 à gagné horizontalement"

        elif self.grille[1][0]=='O' and self.grille[1][1] == 'O' and self.grille[1][2] == 'O':
            finpartie=True
            self.joueurgagnant = "Le joueur 2 à gagné horizontalement"
        elif self.grille[2][0] == 'O' and self.grille[2][1] == 'O' and self.grille[2][2] == 'O':
            finpartie=True
            self.joueurgagnant = "Le joueur 2 à gagné horizontalement"

        elif self.grille[0][0]=='O' and self.grille[1][0] =='O' and self.grille[2][0] == 'O':
            finpartie=True
            self.joueurgagnant = "Le joueur 2 à gagné verticalement"

        elif self.grille[0][2] == 'O' and self.grille[1][2] =='O' and self.grille[2][2] == 'O':
            finpartie=True
            self.joueurgagnant = "Le joueur 2 à gagné verticalement"

        elif self.grille[0][1] == 'O' and self.grille[1][1] =='O' and self.grille[2][1] == 'O':
            finpartie=True
            self.joueurgagnant = "Le joueur 2 à gagné verticalement"

        elif self.grille[0][0] == 'O' and self.grille[1][1] =='O' and self.grille[2][2] == 'O':
            finpartie=True
            self.joueurgagnant = "Le joueur 2 à gagné en diagonale"
        elif self.grille[0][2] == 'O' and self.grille[2][2] == 'O' and self.grille[2][0] == 'O':
            finpartie=True
            self.joueurgagnant = "Le joueur 2 à gagné en diagonale"

        elif self.grille[0][0] == 'X' and self.grille[0][1] == 'X' and self.grille[0][2] == 'X':
            finpartie=True
            self.joueurgagnant = "Le joueur 1 horizontalement"
        elif self.grille[1][0] == 'X' and self.grille[1][1]=='X' and self.grille[1][2] == 'X':
            finpartie=True
            self.joueurgagnant = "Le joueur 1 horizontalement"
        elif self.grille[2][0] == 'X' and self.grille[2][1] == 'X' and self.grille[2][2] == 'X':
            finpartie=True
            self.joueurgagnant = "Le joueur 1  horizontalement"

        elif self.grille[0][0] == 'X' and self.grille[1][0] == 'X' and self.grille[2][0] == 'X':
            finpartie=True
            self.joueurgagnant = "Le joueur 1 à la verticale"

        elif self.grille[0][2] == 'X' and self.grille[1][2] == 'X' and self.grille[2][2] == 'X':
            finpartie=True
            self.joueurgagnant = "Le joueur 1 à la verticale"

        elif self.grille[0][1] == 'X' and self.grille[1][1] == 'X' and self.grille[2][1]=='X':
            finpartie=True
            self.joueurgagnant = "Le joueur 1 à la verticale"

        elif self.grille[0][0] == 'X' and self.grille[1][1] == 'X' and self.grille[2][2] == 'X':
            finpartie=True
            self.joueurgagnant = "Le joueur 1 à gagné en diagonale"
        elif self.grille[0][2] == 'X' and self.grille[2][2] == 'X' and self.grille[2][0] == 'X':
            finpartie=True
            self.joueurgagnant = "Le joueur 1 à gagné en diagonale"
        else:
            finpartie=False

        return finpartie
    def VérifierFinPartie(self):
        if self.compteurCoupJoue == 9:  # Vérifie si tous les coups ont été joué
            self.gagnant = True
        else:
            self.gagnant = self.gagnant

            if self.gagnant == True:
                return self.joueurgagnant





























