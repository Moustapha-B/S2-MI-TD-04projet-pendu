import tkinter as tk
from tkinter import * 
from tkinter.messagebox import *
from tkinter import messagebox
import random
import tkinter.messagebox as mbox

# Safouan
#------------------------------------------------Fonction--------------------------------------------------#
def entrer(event=None):
        verifier()
def aide():
    mbox.showinfo("Comment gagne-t-on au Jeu du Pendu ?","""Commencez par les lettres les plus fréquentes : En français, certaines lettres apparaissent plus fréquemment que d'autres. Les lettres les plus couramment utilisées sont, dans l'ordre, E, A, S, I, N, T, R, U, O, L. Commencez par ces lettres pour avoir plus de chances de trouver celles qui figurent dans le mot.
Prenez en compte la longueur du mot : Si le mot est court, il est plus probable qu'il contienne des lettres moins fréquentes. Si le mot est long, il y a de meilleures chances qu'il contienne plusieurs des lettres les plus courantes.
Utilisez des lettres qui apparaissent souvent ensemble : En français, certaines lettres ont tendance à apparaître ensemble. Par exemple, si vous avez découvert une lettre "Q", il y a de grandes chances que la lettre suivante soit un "U". Si vous avez une lettre "E", il y a de fortes chances que la lettre suivante ou précédente soit un "S" ou un "T".
Rappelez-vous des mots précédents : Si vous jouez plusieurs fois avec le même adversaire, essayez de vous souvenir des mots qu'il a utilisés précédemment. Il y a de bonnes chances qu'il répète certains mots ou qu'il utilise des mots similaires.
Envisagez toutes les possibilités : Lorsque vous avez découvert certaines lettres, essayez de penser à tous les mots possibles qui pourraient correspondre à ce modèle. Cela peut vous aider à choisir la meilleure lettre à essayer ensuite.
Ne vous précipitez pas : Prenez votre temps pour réfléchir à votre prochaine lettre. Il est préférable de passer un peu plus de temps à choisir soigneusement votre lettre que de vous précipiter et de faire une erreur.
Rappelez-vous, cependant, que le Jeu du Pendu est en fin de compte un jeu de hasard. Même si vous utilisez toutes ces stratégies, il y a toujours une chance que vous ne réussissiez pas à deviner le mot à temps. C'est ce qui rend le jeu excitant et amusant à jouer. Bonne chance !""")

def regle_du_jeu():
    mbox.showinfo("Le Jeu du Pendu : Règles du jeu",
  """Le jeu du Pendu est un jeu de devinette simple et amusant qui peut être joué à deux joueurs ou en solo. Voici comment ça marche :

    But du jeu : Le joueur doit deviner un mot mystère en proposant des lettres une par une. Le mot mystère est représenté par des tirets, un pour chaque lettre du mot.

    Déroulement du jeu :
        Le joueur propose une lettre.
        Si la lettre proposée est présente dans le mot mystère, elle est révélée à sa place sur les tirets correspondants.
        Si la lettre proposée n'est pas dans le mot mystère, une partie du pendu est dessinée. Le pendu est généralement représenté par une potence avec plusieurs parties mobiles (tête, corps, bras, jambes).
        Le jeu continue jusqu'à ce que le joueur ait deviné le mot ou que le dessin du pendu soit complet.

    Nombre d'essais : Le joueur dispose d'un nombre limité d'essais pour deviner le mot. Si le pendu est complètement dessiné avant que le joueur ne devine le mot, il perd la partie.

    Indice : Les indices parmettent au joueur d'avoir une lettre sans utiliser de tentative mais l'utilisation de l'indice coûte 3 points 
    
    Points : Lorsque le joueurs gagne une partie, son nombre de points se voit octroyer +6
    
    Streak : C'est le nombre consécutif de parties gagnées, lorsque le joueur perd une partie sa streak revient à 0. Par ailleurs plus la streak du jouer est élevé, plus le nombre de points augmente après une partie gagnée
    
    Nouveau Jeu : permet au joueur de relancer une partie donc de recharger un mot aléatoirement
    
    Gagner ou perdre : Le joueur gagne s'il parvient à deviner le mot avant que le pendu ne soit complètement dessiné. S'il ne parvient pas à deviner le mot dans le nombre d'essais donné, il perd la partie.

Le Jeu du Pendu est un excellent moyen de tester ses compétences en devinette tout en s'amusant ! """)


scores_obtenus = [] #initilisation de la liste, ensuite remplie dans la fonction calculscore
def afficher_scores():
    if scores_obtenus: #vérification si scores_obtenus contient des éléments
        scores_texte = "\n".join([f"Partie {i+1} (mot :{mot_a_deviner}): {score} points" for i, score in enumerate(scores_obtenus)])
        mbox.showinfo("Historique des scores", scores_texte)
    else:
        mbox.showinfo("Historique des scores", "Aucun score n'a été enregistré.")



    


#Mouss
def callback():
    if messagebox.askyesno('Alerte', 'Êtes-vous sûr de vouloir quitter?'):
        messagebox.showwarning('Alerte', 'Tant pis...')
        root.quit()
    else:
        messagebox.showinfo('Alerte', 'Continuez à jouer!')


def calculscore():
    global score # Déclaration du score comme global

    # Calcul du score total
    score += 6 + 1 * streak


    mettre_a_jour_score(score)
    scores_obtenus.append(score) #stockage des scores pour l'affichage de l'historique des scores

    # Mise à jour du score affiché