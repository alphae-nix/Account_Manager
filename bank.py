#!/usr/bin/python3.8
#!-*-coding:utf-8-*


from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont


page_principale = Tk()
page_principale.title("Bank managment")
page_principale.geometry("1400x900+250+100") # taille et placement de la page

########## LES FONCTIONS #########################################################

#### fonctions du menu supérieur ###########

# Fonctions permettant de quitter la page principale
def quit_app():
    page_principale.destroy()

#Fonction créant une nouvelle fenêtre pour la partie "A propos"
def nouvelle_fenetre_a_propos():
    a_propos = Toplevel() #Toplevel() permet de créer une nouvelle fenêtre
    a_propos.title("A propos")
    message="Créé par:"+ '\n'+"Ines Fellous" + '\n'+ "Mona Sennelier" + '\n'+ "Laurent Delatte"+ '\n'+"Responsable d'Atelier :"+ '\n'+"Mr.Rabiet"
    a_propos.geometry("300x150+250+100")
    Label(a_propos, text=message).pack()
    Button(a_propos, text="Retour", command=a_propos.destroy).pack(pady="10")

######### CODE ###################

######## Menu supérieur ###############

mon_menu=Menu(page_principale)

mon_menu.add_command(label="Quit", command=quit_app) # "label"=chaine de charactère à afficher
mon_menu.add_command(label="Aide")
mon_menu.add_command(label="A propos", command=nouvelle_fenetre_a_propos)

page_principale.config(menu=mon_menu)

######### Barre de navigation gauche #########

##### Frame pour la barre de navigation gauche ##########
frame_gauche=Frame(page_principale, width=150,height=400, bg="#707070")
frame_gauche.pack(side=LEFT, fill=Y)

frame2_gauche=Frame(frame_gauche)
frame2_gauche.pack()

Compte_1=Button(frame2_gauche, text="Compte 1", width=15, height=5,bg="#8E96A3",activebackground="#C9D7E8").pack()

################# Barre d'actualité du compte ###########
frame_haut=Frame(page_principale, width=450, height=100, bg="black")
frame_haut.pack(side=TOP, fill=X, expand=True)

frame2_haut=Frame(frame_haut, bg="yellow")
frame2_haut.pack()

l1 = Label(frame2_haut, text="solde", width=30, font="Arial",height=5 ,bg="#848CE9").pack(side=LEFT, padx=5)
l2 = Label(frame2_haut, text="Entrée d'argent", width=25,font="Arial",height=5,  bg="#A0E8A6").pack(side=LEFT, padx=5)
l3 = Label(frame2_haut, text="Sortie d'argent", width=25, font="Arial",height=5, bg="#FF7E65").pack(side=LEFT, padx=5)
l4 = Label(frame2_haut, text="Economies", width=25, font="Arial",height=5, bg="#FFEA85").pack(side=LEFT, padx=5)
b4 = Button(frame2_haut, text="Actualiser", font="Arial", width=15, height=2, bg="#8E96A3",activebackground="#C9D7E8").pack(side=LEFT, padx=5)



#################### AJOUTER UNE DEPENSE ######################

######### Frame #####
frame_droite = Frame(page_principale ,width = 200,height = 1000, bg='green')
frame_droite.pack(side=RIGHT, fill=Y)

## label nom de la dépense
label_depense = Label(frame_droite,text="nom de la dépense") #lbl pour label
label_depense.grid(row=1, column = 0, sticky = (N,S,E,W)) #row correspond à la ligne et sticky colle au bord

# entrée le nom de la dépense
entree_depense = Entry(frame_droite)
entree_depense.grid(row=2,column=0, sticky = (N,S,E,W))
##################
## label type de dépense
lbl_type = Label(frame_droite,text="type de dépense : ") #lbl pour label
lbl_type.grid(row = 3, column = 0,sticky = (N,S,E,W))
#
etiquette= StringVar()
combo = ttk.Combobox(frame_droite, textvariable =etiquette , values = ("loisirs","loyer","voyages","nouriture"), state="readonly")# le readonly permet à ce que l'utilisateur ne change pas la valeur des mois
combo.grid(row=4, column=0, sticky=(N,S,E,W))
####################
#label montant
lbl_montant = Label(frame_droite,text="montant : ") #lbl pour label
lbl_montant.grid(row = 8, column = 0, sticky = (N,S,E,W))
#
ent_montant = Entry(frame_droite)
ent_montant.grid(row=9,column=0, sticky = (N,S,E,W))

################### Armature du milieu ##########################


framemilieu = Frame(page_principale ,width = 300,height = 150, bg='purple')
framemilieu.pack(fill=X)


frame_HG = Frame(framemilieu ,width = 500,height = 400,bd=5)
frame_HG.config(highlightbackground="black")
frame_HG.grid(row=1,column = 1,columnspan = 2, sticky = (E), padx = 10, pady = 10)
frame_HG.grid_propagate(False)

frame_BD = Frame(framemilieu ,width = 500,height = 400, bg='pink')
frame_BD.grid(row=2,column = 1 ,columnspan = 2,sticky = (E), padx = 10)
frame_BD.grid_propagate(False)

frame_HD = Frame(framemilieu ,width = 500,height = 400, bg='pink')
frame_HD.grid(row=1,column = 3,columnspan = 2,sticky = (E), padx = 10)
frame_HD.grid_propagate(False)

frame_BG = Frame(framemilieu ,width = 500,height = 400, bg='blue')
frame_BG.grid(row=2,column = 3, columnspan = 2,sticky = (E), padx = 10)
frame_BG.grid_propagate(False)




######################### Cadre haut gauche de la Frame Centrale ##########################



photo = PhotoImage(file = 'house.png')
house = Label(frame_HG, image = photo )
house.grid(row = 0 , column = 0 , sticky = W)

police=tkFont.Font(frame_HG, size=20, family='URW Gothic', weight = 'bold', underline = 1)

lbl_loyer = Label(frame_HG,text="Loyer :  ") #lbl pour label
lbl_loyer.configure(font = police)
lbl_loyer.grid(padx = 5, pady = 5, sticky = (N,E) , row = 0, column =1)

####################################################################

page_principale.mainloop()
