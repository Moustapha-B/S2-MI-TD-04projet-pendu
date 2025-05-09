import tkinter as tk
from tkinter import * 
from tkinter.messagebox import *
from tkinter import messagebox
import random
import tkinter.messagebox as mbox

#Safouan
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


def calculstreakvictoire():
    global streak
    streak = streak + 1
def calculstreakdefaite():
    global streak
    streak = streak - streak

# Birane
def mettre_a_jour_score(score):
    """
    Cette fonction met à jour le score puis l'affiche

    Paramètres :
        score (int) : Le score actuel du joueur
                      
    Retour:
        aucun

    """
    score_label.config(text=f"Score: {score}")

def mettre_a_jour_streak(streak):
    """
    Cette fonction met à jour le  nombre de parties gagnées consécutives 

    Paramètres:
    streak (int): Le nombre de victoires consécutives

    Retour:
        aucun
    """

    streak_label.config(text=f"Streak: {streak}")





def verifier():
    """
    Cette fonction vérifie que la saisie du  joueur est bien une lettre, que le joueur n'a pas saisie plusieurs fois la même lettre,
    que la lettre est dans le mot à deviner, enfin elle vérifie que le nombre d'essaies du joueur est fini.

    Paramètres: 
        aucun

    Retour:
        aucun

    

    """
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
            calculstreakvictoire()  # Incrémente le streak en cas de victoire
            mettre_a_jour_streak(streak)  # Met à jour l'affichage du streak
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
            calculstreakdefaite()  # Réinitialise le streak en cas de défaite
            mettre_a_jour_streak(streak)  # Met à jour l'affichage du streak
            scores_obtenus.append(0) #ajout d'un score nul pour une défaite
            recommencer_partie()  # Lance une nouvelle partie


# Fonction pour dessiner les parties fixes du pendu
def dessiner_pendu(canvas):
    """
    Cette fonction dessine le support du pendu

    Paramètres: 
        canvas(tk.Canvas) : Le canevas utilisé pour dessiner le support

    Retour:
        aucun

    
    """
    canvas.create_line(20, 200, 120, 200)  # Base
    canvas.create_line(70, 200, 70, 20)    # Poteau vertical
    canvas.create_line(70, 20, 150, 20)    # Poteau horizontal
    canvas.create_line(150, 20, 150, 50)   # Corde

#Boualem
# Fonction pour dessiner les différentes parties mobiles du pendu en fonction des essais restants
def dessiner_pendu_mobile(tentatives_restantes):
    """
    Cette fonction dessine le corps du pendu en fonction du nombre de tentatives restantes

    Paramètres: 
        tentatives_restantes(int): nombre de tentatives qu'il reste au joueur

    Retour:
        aucun


    
    """
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
    """
    Cette fonction demande au joueur s'il veut recommencer une partie une fois qu'il y a plus de tentatives restantes.

    Paramètres: 
        aucun

    Retour:
        aucun

    
    """
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

# Safouan
def obtenir_indice():
    """
    Cette fonction aide le joueur mais seulement si son score le permet.

    Paramètres: 
        aucun

    Retour:
        aucun


    """
    global score
    if score >= 3 : # Vérification si le joueur a suffisamment de points pour obtenir un indice 
        confirmation = messagebox.askyesno("Indice", "Attention : Cet indice vous coûtera 3 points. Êtes-vous sûr de vouloir continuer ?")

        if confirmation:
            if len(lettres_proposees) < len(mot_a_deviner):
                lettre_indice = random.choice([l for l in mot_a_deviner if l not in lettres_proposees])
                messagebox.showinfo("Indice", f"Indice : La lettre '{lettre_indice}' est dans le mot.")
                score -= 3
                mettre_a_jour_score(score)
    else:
        messagebox.askyesno("Indice", "Attention : Vous n'avez pas les points requis pour cette action. Il vous faut 3 points pour débloquer un indice")


def afficher_lettres_deja_utlisees():
    """
    Cette fonction trie les lettres du set lettres_proposees les change en une liste triée puis en chaine de caractère

    Paramètres: 
        aucun

    Retour:
        aucun

    """

    lettres_deja_utlisees = ', '.join(sorted(lettres_proposees))
    lettres_deja_utlisees_label.config(text=f"Lettres déjà utilisées : {lettres_deja_utlisees}")

#Mouss
#---------------------------------------------------Interface--------------------------------------------
root = tk.Tk()
root.title("Jeu du Pendu")
mots = [
    "POUR", "MILLIONS", "FONCTION", "GESTION", "OCCASION",
    "RENDRE", "COMPRENDRE", "SAIT", "DONNE", "ORDRE", "MOYEN", "TERME", "ATTENTION",
    "EUROPE", "NOUVEAUX", "PLEIN", "ENVIRON", "PERIODE", "REGARD", "DIFFERENTES",
    "UTILISATION", "REPONSE", "PRISE", "PRESENTS","COQ"
]


mot_a_deviner = random.choice(mots)
mot_trouve = ["_" for _ in mot_a_deviner] 

lettres_proposees = set()
essaies = 6
score = 0
streak = 0

#Safouan
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 16))
score_label.pack()

streak_label = tk.Label(root, text=f"Streak: {streak}", font=("Arial", 16))
streak_label.pack()

mot_label = tk.Label(root, text=" ".join(mot_trouve), font=("Arial", 24))
mot_label.pack()

essais_restants_label = tk.Label(root, text=f"Tentatives restantes : {essaies}", font=("Arial", 16))
essais_restants_label.pack()


#Boualem
canvas = tk.Canvas(root, width=200, height=250)
canvas.pack()
dessiner_pendu(canvas)

lettre_entree = tk.Entry(root, font=("Arial", 18))
lettre_entree.pack()


lettres_deja_utlisees_label = tk.Label(root, text="Lettres déjà utlisées : ", font=("Arial", 16))
lettres_deja_utlisees_label.pack()


bouton_verifier = tk.Button(root, text="Vérifier", command=verifier, bg="green", height=2, width=20)
bouton_verifier.pack()
root.bind("<Return>", entrer)
bouton_indice = tk.Button(root, text="Indice", command=obtenir_indice, bg="yellow", height=2, width=20)
bouton_indice.pack()
bar = tk.Menu(root)

#Birane
# Le premier menu
menu_jeu = tk.Menu(bar)
# Le menu qui contient 'Nouveau jeu' et 'Quitter'
menu_jeu.add_command(label="Nouveau jeu", command=recommencer_partie, underline=0)
menu_jeu.add_command(label="Quitter", command=callback, underline=0)
# On ajoute ce menu a la barre
bar.add_cascade(label="Jeu", menu=menu_jeu, underline=0)

#Mouss
# Le menu 'Aide', avec la regle et un 'À propos'
menu_aide = tk.Menu(bar)
menu_aide.add_command(label="Règle du jeu", command=regle_du_jeu, underline=0)

#Safouan
#menu_aide.add_command(label="À propos", command=a_propos, underline=2)
menu_aide.add_command(label="Comment gagne-t-on au Jeu du Pendu ?",command=aide,underline=4)
# On ajoute ce menu a la barre
bar.add_cascade(label="Aide", menu=menu_aide, underline=0)

#Boualem
# Le menu 'scores', avec l'historique des scores''
menu_scores = tk.Menu(bar)
menu_scores.add_command(label="Voir l'historique des scores",command=afficher_scores,underline=4)
# On ajoute ce menu a la barre
bar.add_cascade(label="Scores", menu=menu_scores, underline=0)

# On ajoute la barre de menus a la masterêtre
root.config(menu=bar)


root.mainloop()


#---------------------------------------------------Sources--------------------------------------------

# https://docs.python.org/3/library/tkinter.messagebox.html
# https://docs.python.org/fr/3/library/tkinter.html
# https://www.commentcoder.com/python-liste-tuple-set-dict/
# https://datascientest.com/docstring-tout-savoir#:~:text=Je%20vais%20maintenant%20vous%20montrer%20comment%20cr%C3%A9er%20des,%2A%2AautoDocString%20%E2%80%93%20Python%20DocString%20Generator%2A%2A%20%C3%A0%20votre%20IDE.
# https://www.pythontutorial.net/tkinter/tkinter-menu/
# https://mot-pendu.com/