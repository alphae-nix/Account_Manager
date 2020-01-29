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

##### Frame pour la barre de navigation gauche ##########
frame_gauche=Frame(page_principale, width=150,height=1000, bg="#707070")
frame_gauche.grid(row=0, column=0, rowspan=1000)
frame_gauche.grid_propagate(0)

b1=Button(frame_gauche, text="Compte 1", width=15, height=5,bg="#8E96A3",activebackground="#C9D7E8").grid( row=0, column=0)
b2=Button(frame_gauche, text="Dépense", width=15, height=3,bg="#FFA67D", activebackground='#FEC1A2').grid( row=1, column=0)
b3=Button(frame_gauche, text="Gain", width=15, height=3,bg="#B2EB83", activebackground="#CDEB9A").grid( row=2, column=0)

################# Barre d'actualité du compte ###########
frame_haut=Frame(page_principale)
frame_haut.grid(row=0, column=1, sticky=(N,S,E,W), columnspan=5)
frame_haut.columnconfigure(0,weight=1)
frame_haut.rowconfigure(0, weight=1)
frame_haut.config(bg='black')

l1 = Label(frame_haut, text="solde", width=30, font="Arial",height=5 ,bg="#848CE9").grid(row=0, column=1, padx=15)
l2 = Label(frame_haut, text="Entrée d'argent", width=25,font="Arial",height=5,  bg="#A0E8A6").grid(row=0, column=2, padx=5)
l3 = Label(frame_haut, text="Sortie d'argent", width=25, font="Arial",height=5, bg="#FF7E65").grid(row=0, column=3, padx=5)
l4 = Label(frame_haut, text="Economies", width=25, font="Arial",height=5, bg="#FFEA85").grid(row=0, column=4, padx=5)
b4 = Button(frame_haut, text="Actualiser", font="Arial", width=15, height=2, bg="#8E96A3",activebackground="#C9D7E8").grid(row=0, column=5, padx=30)




################### Armature du milieu ##########################


framemilieu = Frame(page_principale ,width = 300,height = 150, bg='purple')
framemilieu.grid(row=1,column = 1, rowspan = 1000,sticky = (N,S,E,W), columnspan=5  )
framemilieu.grid_propagate(False)




lbl_resume = Label(framemilieu,text="resumé des dépenses : ") #lbl pour label
lbl_resume.grid(row=1, column = 5, sticky = (N,S,E,W))
barre = Canvas(framemilieu, width = 20 , height = 10, background="red")
barre2 = Canvas(framemilieu, width = 30 , height = 10, background="black")

#Canvas.framemilieu(barre,width = 1400, height=900)
barre.grid(column = 10 , row = 5)
barre2.grid(column = 5 , row = 5)

#framemilieugauche = Frame(framemilieu ,width = 300,height = 150, bg='blue')
#framemilieugauche.grid(row=1,column = 1,columnspan = 4, rowspan = 1000  ,sticky = (E))
#framemilieugauche.grid_propagate(False)



#framemilieudroite = Frame(framemilieu ,width = 300,height = 150, bg='pink')
#framemilieudroite.grid(row=1,column = 2,columnspan = 4, rowspan = 1000  ,sticky = (E))
#framemilieudroite.grid_propagate(False)





#################### AJOUTER UNE DEPENSE ######################


framedroite = Frame(page_principale ,width = 200,height = 1000, bg='green')
framedroite.grid(row=1,column = 5, sticky = (E))

framedroite.grid_propagate(False)

Button(framedroite, text = "ajouter une dépense", relief = RAISED).grid(row = 0, column =0)


lbl_depense = Label(framedroite,text="nom de la dépense") #lbl pour label
lbl_depense.grid(row=1, column = 0, sticky = (N,S,E,W)) #row correspond à la ligne et sticky colle au bord
ent_depense = Entry(framedroite)
ent_depense.grid(row=2,column=0, sticky = (N,S,E,W))

lbl_type = Label(framedroite,text="type de dépense : ") #lbl pour label
lbl_type.grid(row = 3, column = 0, sticky = (N,S,E,W))
ttk.Radiobutton(framedroite,text="loisirs", value = 1).grid(row = 4, column =0, sticky = (N,S,E,W))
ttk.Radiobutton(framedroite,text="loyer", value = 2).grid(row = 6, column = 0, sticky = (N,S,E,W))
ttk.Radiobutton(framedroite,text="voyages", value = 3).grid(row=5, column =0, sticky = (N,S,E,W))
ttk.Radiobutton(framedroite,text="nouriture", value = 4).grid(row=7, column =0, sticky = (N,S,E,W))
lbl_montant = Label(framedroite,text="montant : ") #lbl pour label
lbl_montant.grid(row = 8, column = 0, sticky = (N,S,E,W))
ent_montant = Entry(framedroite)
ent_montant.grid(row=9,column=0, sticky = (N,S,E,W))









#########################





page_principale.mainloop()
