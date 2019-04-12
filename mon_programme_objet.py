from TicTacToe import TicTacToe

JeuApplication = TicTacToe() # Instantiation du jeu.

while JeuApplication.gagnant == False: # Boucle qui fait tourner le jeu

    JeuApplication.AfficherEtatJeu() # Fonction qui me permet d'afficher l'état du jeu.
    JeuApplication.JouerJeton() # Fonction qui permet de faire jouer un joueur
    JeuApplication.gagnant=JeuApplication.VerifierGagnant() # Foncion qui permet de vérifier s'il y a un gagnant.
    JeuApplication.compteurCoupJoue += 1 # Compteur qui permet de vérifier le tour du joueur et voir si les 9 coups on été joués
    JeuApplication.VérifierFinPartie()
JeuApplication.AfficherEtatJeu() # Affiche la grille de jeu pour voir l'état final lors de la fin de partie
print(JeuApplication.VérifierFinPartie())  # Permet d'identifier le joueur gagnant.1

