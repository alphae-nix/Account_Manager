#!/usr/bin/python3.8
#!-*-coding:utf-8-*


from tkinter import *
from tkinter import ttk


page_principale = Tk()
page_principale.title("bank")
page_principale.geometry("1400x900+250+100") # taille et placement de la page

########## LES FONCTIONS ##########
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
b1=Button(page_principale, text="Compte 1", width=15, height=5,bg="#8E96A3",activebackground="#C9D7E8").grid( row=0, column=0)
b2=Button(page_principale, text="Dépense", width=15, height=3,bg="#FFA67D", activebackground='#FEC1A2').grid( row=1, column=0)
b3=Button(page_principale, text="Gain", width=15, height=3,bg="#B2EB83", activebackground="#CDEB9A").grid( row=2, column=0)

##########################################
page_principale.mainloop()
