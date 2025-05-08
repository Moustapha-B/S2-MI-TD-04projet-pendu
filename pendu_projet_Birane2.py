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
#Birane
def mettre_a_jour_score(score):
    score_label.config(text=f"Score: {score}")






def verifier():
    lettre = lettre_entree.get().upper() # Récupère la lettre proposée par le joueur et la met en majuscule
    lettre_entree.delete(0, tk.END) # Efface le contenu de l'entrée après avoir récupéré la lettre
    if len(lettre) != 1 or not lettre.isalpha(): # Vérifie si la saisie est invalide
        messagebox.showwarning("Erreur", "Veuillez entrer une seule lettre.")
        return

    if lettre in lettres_proposees: # Vérifie si la lettre a déjà été proposée précédemment
        messagebox.showwarning("Attention", "Vous avez déjà proposé cette lettre.")
        return

    lettres_proposees.add(lettre) # Ajoute la lettre à l'ensemble des lettres proposées

    if lettre in mot_a_deviner:
        for i, l in enumerate(mot_a_deviner): # Vérifie si la lettre proposée est dans le mot à deviner
            if l == lettre:
                mot_trouve[i] = lettre # Remplace les tirets par la lettre trouvée aux bonnes positions
        mot_label.config(text=" ".join(mot_trouve)) # Met à jour l'affichage du mot à deviner
        afficher_lettres_deja_utlisees()
  #Mouss
        if "_" not in mot_trouve: # Vérifie si le mot a été entièrement deviné
            messagebox.showinfo("Félicitations", f"Vous avez trouvé le mot : {''.join(mot_a_deviner)} !")
            recommencer_partie()  # Lance une nouvelle partie
            calculscore()  # Calcule le score obtenu
            mettre_a_jour_score(score)  # Met à jour l'affichage du score
            return

    else:
        # Si la lettre proposée n'est pas dans le mot à deviner
        essaies_restants = essais_restants_label.cget("text")
        essaies_restants = int(essaies_restants.split(": ")[1])
        essaies_restants -= 1
        essais_restants_label.config(text=f"Tentatives restantes : {essaies_restants}")  # Met à jour les tentatives restantes
        dessiner_pendu_mobile(essaies_restants)  # Dessine la partie correspondante du pendu
        afficher_lettres_deja_utlisees()  # Met à jour l'affichage des lettres déjà utilisées

        if essaies_restants == 0:
            # Vérifie si le joueur a épuisé toutes ses tentatives
            messagebox.showinfo("Perdu", f"Vous avez perdu ! Le mot était : {''.join(mot_a_deviner)}.")
            scores_obtenus.append(0) #ajout d'un score nul pour une défaite
            recommencer_partie()  # Lance une nouvelle partie



# Fonction pour dessiner les parties fixes du pendu
def dessiner_pendu(canvas):
    canvas.create_line(20, 200, 120, 200)  # Base
    canvas.create_line(70, 200, 70, 20)    # Poteau vertical
    canvas.create_line(70, 20, 150, 20)    # Poteau horizontal
    canvas.create_line(150, 20, 150, 50)   # Corde

#Boualem
# Fonction pour dessiner les différentes parties mobiles du pendu en fonction des essais restants
def dessiner_pendu_mobile(tentatives_restantes):
    if tentatives_restantes < 6:
        canvas.create_oval(130, 50, 170, 90)   # Tête
    if tentatives_restantes < 5:
        canvas.create_line(150, 90, 150, 150)  # Corps
    if tentatives_restantes < 4:
        canvas.create_line(150, 100, 130, 130) # Bras
    if tentatives_restantes < 3:
        canvas.create_line(150, 100, 170, 130) # Bras droit
    if tentatives_restantes < 2:
        canvas.create_line(150, 150, 130, 180) # Jambe gauche
    if tentatives_restantes < 1:
        canvas.create_line(150, 150, 170, 180) # Jambe droite


def recommencer_partie():
    if messagebox.askyesno("Recommencer", "Voulez-vous recommencer une partie?"):
        global mot_a_deviner, mot_trouve, lettres_proposees
        mot_a_deviner = random.choice(mots)
        mot_trouve = ["_" for _ in mot_a_deviner]
        lettres_proposees = set() # Réinitialisation de l'ensemble des lettres proposées
        essaies = 6
        mot_label.config(text=" ".join(mot_trouve)) # Mise à jour de l'affichage du mot à deviner
        essais_restants_label.config(text=f"Tentatives restantes : {essaies}") # Mise à jour de l'affichage des tentatives restantes
        lettres_deja_utlisees_label.config(text="Lettres déjà utilisées : ") # Réinitialisation de l'affichage des lettres déjà utilisées
        canvas.delete("all") # Effacement du dessin du pendu
        dessiner_pendu(canvas) # Redessin du pendu initial
        dessiner_pendu_mobile(6) # Affichage complet du pendu initial

# Birane
    else:
        if messagebox.askyesno('Alerte', 'Êtes-vous sûr de vouloir quitter?'):
            messagebox.showwarning('Alerte', 'Tant pis...')
            root.quit()
        else:
            messagebox.showinfo('Alerte', 'Continuez à jouer!')