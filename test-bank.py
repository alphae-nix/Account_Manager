#!/usr/bin/python3.8
#!-*-coding:utf-8-*


from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import os
from tkinter import messagebox



page_principale = Tk()
page_principale.title("Bank managment") #Titre de la page

page_principale.update_idletasks()
width = 1400
height = 920
x = (page_principale.winfo_screenwidth() // 2) - (width // 2)
y = (page_principale.winfo_screenheight() // 2) - (height // 2)
page_principale.geometry('{}x{}+{}+{}'.format(width, height, x, y))


########## LES FONCTIONS ######################################################### "loisirs","loyer","voyages","nouriture"

def addBox():
    global test34
    global x,y,z,old_x,old_y,old_z
    x = int(x) #variable qui sert a mémoriser la valeur générale du solde
    y = int(y) #variable qui sert a mémoriqer la valeur générale des dépences
    z = int(z) #variable qui sert a mémoriqer la valeur générale des recettes
    old_x = int(old_x) #variable qui sert a mémoriser l'ancienne valeur générale du solde
    old_y = int(old_y) #variable qui sert a mémoriser l'ancienne valeur générale des dépences
    old_z = int(old_z) #variable qui sert a mémoriser l'ancienne valeur générale des recettes

    val_pOm = pOm.get() #Recupere la valeur du RadioButton pour savoir si l'on est dans une dépence ou une recette (pOm = plus OU moins)
    montant=ent_montant.get() # Recupere la valeur du montant entré dans le entry
    j=ent_jour.get() # Recupere la valeur du jour entré dans le entry
    m=ent_mois.get() # Recupere la valeur du mois entré dans le entry
    a=ent_annee.get() # Recupere la valeur de l'année entré dans le entry
    affiche=entree_depense.get() # Recupere la valeur du descritptif entré dans le entry
    select = combo.get() # Recupere la valeur selectionée dans la liste déroulante

################################################ Test Des Exceptions possibles ########################################
    try : #### Exception pour le Montant qui permet d'afficher un message d'erreur et de stoper la lecture de la fonction si des lettres sont entrées ou si rien n'est entre
        int(montant)
    except ValueError:
        messagebox.showinfo("Attention","Veuillez saisir un nombre pour le montant svp!", icon="warning")
        return

    try : #### Exception pour le Jour qui permet d'afficher un message d'erreur et de stoper la lecture de la fonction si des lettres si rien n'est entré sont entrées ou que la valeur dépasse 31
        test1=int(j)
        assert test1<32
    except ValueError:
        messagebox.showinfo("Attention","Veuillez saisir un nombre pour le jour svp!", icon="warning")
        return
    except AssertionError:
        messagebox.showinfo("Attention","vous avez saissi un numéro supérieur à 31 pour le jour !", icon="warning")
        return

    try : #### Exception pour le Mois qui permet d'afficher un message d'erreur et de stoper la lecture de la fonction si des lettres sont entrées si rien n'est entré ou que la valeur dépasse 12
        test2=int(m)
        assert test2<13
    except ValueError:
        messagebox.showinfo("Attention","Veuillez saisir un nombre pour le mois svp!", icon="warning")
        return
    except AssertionError:
        messagebox.showinfo("Attention","vous avez saissi un numéro supérieur à 12 pour le mois !", icon="warning")
        return

    try : #### Exception pour l'année qui permet d'afficher un message d'erreur et de stoper la lecture de la fonction si des lettres sont entrées
        int(a)
    except ValueError:
        messagebox.showinfo("Attention","Veuillez saisir un nombre pour l'année svp!", icon="warning")
        return

    try : ### Exception pour la liste déroulante qui permet d'afficher un message d'erreur et de stoper la lecture de la fonction si rien n'est selectionner
        test3=select
        assert test3 == "loisirs" or test3 == "voyages" or test3=="loyer" or test3=="alimentation"
    except AssertionError:
        messagebox.showinfo("Attention","Veuillez selectionner un type svp!", icon="warning")
        return
####################################################################################
    if select == "loisirs": #bouton du menu déroulant permettant d'ajouter une ligne de dépense/gain dans la frame des loisirs
         if montant != "" and j!= "" and m != "" and a != "" and affiche != "" and int(j)<32 and int(m)<13 and (val_pOm == 1 or val_pOm == 2): #permet d'éviter d'ajouter une ligne de dépense/gain si une erreur est commise par l'utilisateur par ex il ne peut rentre un numero de jour superieur à 31
             frame = Frame(frame2_HD) # creation d'une ligne de dépense/recette
             frame.pack(side=BOTTOM,fill=Y)
             test34=frame

    if select == "voyages" : #bouton du menu déroulant permettant d'ajouter une ligne de dépense/gain dans la frame des voyages
         if montant != "" and j!= "" and m != "" and a != "" and affiche != "" and int(j)<32 and int(m)<13 and (val_pOm == 1 or val_pOm == 2): #permet d'éviter d'ajouter une ligne de dépense/gain si une erreur est commise par l'utilisateur par ex il ne peut rentre un numero de jour superieur à 31
             frame = Frame(frame2_BG)
             frame.pack(side=BOTTOM,fill=Y)
             test34=frame

    if select == "loyer" :#bouton du menu déroulant permettant d'ajouter une ligne de dépense/gain dans la frame du loyer
         if montant != "" and j!= "" and m != "" and a != "" and affiche != "" and int(j)<32 and int(m)<13 and (val_pOm == 1 or val_pOm == 2): #permet d'éviter d'ajouter une ligne de dépense/gain si une erreur est commise par l'utilisateur par ex il ne peut rentre un numero de jour superieur à 31
             frame = Frame(frame2_HG)
             frame.pack(side=BOTTOM,fill=Y)
             test34=frame

    if select == "alimentation" : #bouton du menu déroulant permettant d'ajouter une ligne de dépense/gain dans la frame de l'alimentaion
         if montant != "" and j!= "" and m != "" and a != "" and affiche != "" and int(j)<32 and int(m)<13 and (val_pOm == 1 or val_pOm == 2): #permet d'éviter d'ajouter une ligne de dépense/gain si une erreur est commise par l'utilisateur par ex il ne peut rentre un numero de jour superieur à 31
             frame = Frame(frame2_BD)
             frame.pack(side=BOTTOM,fill=Y)
             test34=frame

################ actualisation de la frame du haut (solde, recette, dépense) + creation du premier label (celui du montant) pour le remplissage des lignes de dépense/recette dans la frame du milieu ##############################
    if val_pOm == 1: #si la valeur de plus ou moins est égale à 1 c'est à dire à une dépense
        montant=ent_montant.get() # réccupération du montant

        if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)>32 or int(m)>13 or (val_pOm != 1 and val_pOm != 2): # ne rentre pas dans le if si les informations rentrée par l'utilisateur sont incorrectes
            messagebox.showinfo("Attention","Vous avez saisi au moins une information incorrecte !", icon="warning")

### cette fonction créé un label qui va afficher la valeur de la dépence selectionnée
### soustraire au solde actuel (x) la valeur entrée
### et soustraire à la dépence totale actuelle (y) la valeur entrée
        else :
            lbl1 = Label(frame,fg='red', width=20)
            lbl1["text"]="- "+montant+" € " # affiche dans le label 1 le texte correspondant au montant
            lbl1.grid(row=0, column=0)

            if old_x == x : ## si il y a eu une annulation de l'opération précédente
                result = old_x - int(montant)
                result_m = old_y - int(montant)

            else :
                result = x - int(montant)
                result_m = y - int(montant)
            lblS["text"]= result #le texte du label solde change en celui du resultat de la soustraction
            lblD["text"]= result_m #le texte du label des dépences chance en celui du resultat de la soustraction
            old_x = x
            old_y = y
            x = str(result) #actualisation de la valeur x (solde actuel) pour les prochaines entrées
            y = str(result_m) #actualisation de la valeur y (dépences totale actuelles) pour les prochaines entrées
            result = 0
            result_m = 0

    if val_pOm == 2: #si la valeur de plus ou moins est égale à 1 c'est à dire à une recette
        montant=ent_montant.get()


        if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)>32 or int(m)>13 or (val_pOm != 1 and val_pOm != 2):
            messagebox.showinfo("Attention","Vous avez saisi au moins une information incorrecte !", icon="warning")
            print("Tout va bien")

### cette fonction créé un label qui va afficher la valeur de la dépence selectionnée
### additionner au solde actuel (x) la valeur entrée
### et additionner à la recette totale actuelle (z) la valeur entrée
        else :

            lbl1 = Label(frame,fg='#26BD34', width=20)
            lbl1["text"]=montant+" € " # affiche dans le label 1 le texte correspondant au montant
            lbl1.grid(row=0, column=0)

            if old_x == x : ## si il y a eu une annulation de l'opération précédente
                result = old_x + int(montant)
                result_p = old_z + int(montant)

            else :
                result = x + int(montant)
                result_p = z + int(montant)

            old_x = x
            old_z = z
            lblS["text"]= result #le texte du label solde chance en celui du resultat de l'addition
            lblR["text"]= result_p #le texte du label des recttes change en celui du resultat de l'addition

            x = str(result) #actualisation de la valeur x (solde actuel) pour les prochaines entrées
            z = str(result_p) #actualisation de la valeur y (recttes totale actuelles) pour les prochaines entrées
            result = 0
            result_p = 0



################## label 3 cad la description de la dépense ################
    affiche=entree_depense.get()

    if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)>32 or int(m)>13 or (val_pOm != 1 and val_pOm != 2):
        messagebox.showinfo("Attention","Vous avez saisi au moins une information incorrecte !", icon="warning")

    else :
        lbl3 = Label(frame, width=20)
        lbl3["text"]=affiche # affiche dans le label 3 le texte correspondant à la description
        lbl3.grid(row=0, column=1, sticky=(N,S,E,W))


#################### label 2 cad la date avec lbl2j pour le jour, lbl2m pour le mois et lbl2a pour l'année ####################
    j=ent_jour.get()
    if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)>32 or int(m)>13 or (val_pOm != 1 and val_pOm != 2):
        pass

    else :
        choix=jour.get()
        if champ==1:
            lbl2j = Label(frame, width=6)
            lbl2j["text"]=j+"/" # affiche dans le label 2j le texte correspondant au jour
            lbl2j.grid(row=0, column=2, sticky=(N,S,E,W))
        else:
            print("aucune saisie")

    m=ent_mois.get()
    if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)>32 or int(m)>13 or (val_pOm != 1 and val_pOm != 2):
        pass

    else :
        choix=mois.get()
        if champ==1:
            lbl2m = Label(frame, width=6)
            lbl2m["text"]=m+"/" # affiche dans le label 2m le texte correspondant au mois
            lbl2m.grid(row=0, column=3, sticky=(N,S,E,W))
        else:
            print("aucune saisie")

    a=ent_annee.get()
    if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)>32 or int(m)>13 or (val_pOm != 1 and val_pOm != 2):
        pass
    else :
        choix=annee.get()
        if champ==1:
            lbl2a = Label(frame, width=6)
            lbl2a["text"]=a # affiche dans le label 2a le texte correspondant a l'année
            lbl2a.grid(row=0, column=4)
        else:
            print("aucune saisie")

        if montant != "" and j!= "" and m != "" and a != "" and affiche != "" and int(j)<32 and int(m)<13 and (val_pOm == 1 and val_pOm == 2):
            all_entries.append( (lbl1, lbl2j,lbl2m,lbl2a, lbl3) ) # affiche dans l'odre les un a coté des autres touts les label ecrits

#------------------------------------
test34=Frame()

###fonction qui supprime le JJ lorsque l'on clic dessus
def click_j():
    global champ
    champ=1
    jour.set("")
    ent_jour.config(fg="black")

###fonction qui supprime le MM lorsque l'on clic dessus
def click_m():
    global champ
    champ=1
    mois.set("")
    ent_mois.config(fg="black")

###fonction qui supprime le AAAA lorsque l'on clic dessus
def click_a():
    global champ
    champ=1
    annee.set("")
    ent_annee.config(fg="black")

###fonction qui limite a 2 caracteres dans l'entry jour
def appui_j():
    choix=jour.get()
    if len(choix)+1>2:
        ent_jour.delete([1])

###fonction qui limite a 2 caracteres dans l'entry mois
def appui_m():
    choix=mois.get()
    if len(choix)+1>2:
        ent_mois.delete([1])

###fonction qui limite a 4 caracteres dans l'entry année
def appui_a():
    choix=annee.get()
    if len(choix)+1>4:
        ent_annee.delete([3])

### fonction qui permet d'annuler l'opération précédente
def annul():
    global x,y,z
    lblS["text"]= old_x
    lblD["text"]= old_y
    lblR["text"]= old_z

    x = old_x
    y = old_y
    z = old_z

    test34.destroy()
    #

#### fonctions du menu supérieur ###########

# Fonctions permettant de quitter la page principale
def quit_app():
    page_principale.destroy()

def autre_compte() :
    page_principale.destroy()
    os.system("./register.py")


#Fonction créant une nouvelle fenêtre pour la partie "A propos"
def nouvelle_fenetre_a_propos():
    a_propos = Toplevel() #Toplevel() permet de créer une nouvelle fenêtre
    a_propos.title("A propos")
    message="Créé par:"+ '\n'+"Ines Fellous" + '\n'+ "Mona Sennelier" + '\n'+ "Laurent Delatte"+ '\n'+'\n'+"Responsable d'Atelier :"+ '\n'+"Mr.Rabiet"
    a_propos.geometry("500x200+700+400")
    Label(a_propos, text=message).pack()
    Button(a_propos, text="Retour", command=a_propos.destroy).pack(pady="10")


# Fonction créant une nouvelle fenêtre pour la partie "Aide"
def aide():
    f_aide=Toplevel()
    f_aide.title("Aide")
    aff="Pour lancer l'application, placer vous dans un terminal et exécuté "+"\'"+"."+"/"+"register.py"+"\'"+"\n"+"Ou sinon éxecuter le code sur IDLE"
    f_aide.geometry("500x200+700+400")
    Label(f_aide, text=aff).pack()
    Button(f_aide, text="Notre Rapport", command=open_rapport).pack(pady="10")
    Button(f_aide, text="Retour", command=f_aide.destroy).pack(pady="10")

def open_rapport(): #Permet d'ouvrir le rapport
    if os.name == "posix": #Permet de connaitre l'os utilisé pour exécuter en fonctions
        os.system('xdg-open '+"./rapport.pdf")
    else :
        os.startfile('xdg-open '+"./rapport.pdf")


######### CODE ###################
all_entries = []
######## Menu supérieur ###############

mon_menu=Menu(page_principale)

mon_menu.add_command(label="Quit", command=quit_app) # "label"=chaine de charactère à afficher
mon_menu.add_command(label="Aide", command=aide)
mon_menu.add_command(label="A propos", command=nouvelle_fenetre_a_propos)
mon_menu.add_command(label="Autre compte", command=autre_compte)

page_principale.config(menu=mon_menu)

######### Barre de navigation gauche #########

##### Frame pour la barre de navigation gauche ##########
frame_gauche=Frame(page_principale, width=150,height=400, bg="#777A79")
frame_gauche.pack(side=LEFT, fill=Y)

frame2_gauche=Frame(frame_gauche)
frame2_gauche.pack()

Compte_1=Button(frame2_gauche, text="Compte 1", width=15, height=5,bg="#8E96A3",activebackground="#C9D7E8").pack()

################# Barre d'actualité du compte ###########
frame_haut=Frame(page_principale, width=450, height=100)
frame_haut.pack(side=TOP, fill=X, expand=True)

frame2_haut=Frame(frame_haut)
frame2_haut.pack()

#variable
x=0
y=0
z=0
old_x=0
old_y=0
old_z=0

##################SOLDE#######################
lF = LabelFrame(frame2_haut,text='SOLDE', width=250,height=100, bg="#848CE9")
lF.pack(side=LEFT, padx=10)
lF.pack_propagate(0)

lblS = Label(lF, bg="#848CE9")
lblS.pack(side=LEFT, padx=10)

lble = Label(lF, text=" € ", bg="#848CE9")
lble.pack(side=RIGHT, padx=10)

###################RECETTES#######################
lF2 = LabelFrame(frame2_haut, text="RECETTES", width=250,height=100,  bg="#A0E8A6")
lF2.pack(side=LEFT, padx=10)
lF2.pack_propagate(0)

lblR = Label(lF2, bg="#A0E8A6")
lblR.pack(side=LEFT, padx=10)

lble = Label(lF2, text=" € ", bg="#A0E8A6")
lble.pack(side=RIGHT, padx=10)

###################DEPENSES######################"
lF3 = LabelFrame(frame2_haut, text="DEPENSES", width=250,height=100,  bg="#FF7E65")
lF3.pack(side=LEFT, padx=10)
lF3.pack_propagate(0)

lblD = Label(lF3, bg="#FF7E65")
lblD.pack(side=LEFT, padx=10)

lble = Label(lF3, text=" € ", bg="#FF7E65")
lble.pack(side=RIGHT, padx=10)

l4 = Label(frame2_haut, text="Balances des \n différents comptes", width=25, font="Arial",height=5, bg="#FFEA85").pack(side=LEFT, padx=10)
b4 = Button(frame2_haut, text="Actualiser", font="Arial", width=15, height=2, bg="#8E96A3",activebackground="#C9D7E8", command = addBox).pack(side=LEFT, padx=10)

frame2_haut.bind_all("<KeyPress-Return>", lambda ajout:addBox()) #raccourci clavier enter pour le boutton actualiser


#################### AJOUTER UNE DEPENSE ######################

######### Frame #####
frame_droite = Frame(page_principale ,width = 200,height = 1000)
frame_droite.pack(side=RIGHT, fill=Y)

frame_test_droite=Frame(frame_droite, relief=GROOVE, bd=5)
frame_test_droite.pack(side = TOP, pady=20)

police1=tkFont.Font(frame_test_droite, size=10, family='Source Code Pro Semibold', underline = 0)

#RadioButton Dépense ou recette
pOm = IntVar() #variable PlusOuMoins

ajoutDR = Label(frame_test_droite, text="Ajouter une Dépense \n ou une Recette")
ajoutDR.configure(font=police1)
ajoutDR.pack(side=TOP, pady=2)

frame_radiobutton=Frame(frame_test_droite)
frame_radiobutton.pack()

#selection depense
moins = Radiobutton(frame_radiobutton, text="Dépense", variable=pOm, value=1)
moins.configure(font = police1)
moins.pack(side=LEFT)

## selection recette
plus = Radiobutton(frame_radiobutton, text="Recette", variable=pOm, value=2)
plus.configure(font = police1)
plus.pack(side=RIGHT)

## label nom de la dépense
label_nom_depense = Label(frame_test_droite,text="Description : ")
label_nom_depense.configure(font = police1)
label_nom_depense.pack() #row correspond à la ligne et sticky colle au bord

# entrée le nom de la dépense
entree_depense = Entry(frame_test_droite)
entree_depense.pack()
#######################################################

## label type de dépense
lbl_type = Label(frame_test_droite,text="type : ")
lbl_type.configure(font = police1)
lbl_type.pack()

## Combobox pour le menu déroulant
etiquette= StringVar()
combo = ttk.Combobox(frame_test_droite, textvariable =etiquette , values = ("loisirs","loyer","voyages","alimentation"), state="readonly")# le readonly permet à ce que l'utilisateur ne change pas la valeur des mois
combo.configure(font = police1)
combo.pack()
########################################################
#label montant
lbl_montant = Label(frame_test_droite,text="montant : ") #lbl pour label
lbl_montant.configure(font = police1)
lbl_montant.pack()
#

frame_montant=Frame(frame_test_droite)
frame_montant.pack()

ent_montant = Entry(frame_montant)
ent_montant.pack(side=LEFT)
#
lbl_euro = Label(frame_montant,text=" € ")
lbl_euro.configure(font = police1)
lbl_euro.pack(side=RIGHT)
########################################################
# label date
lbl_date = Label(frame_test_droite,text="Date : ")
lbl_date.configure(font = police1)
lbl_date.pack()

frame_date=Frame(frame_test_droite)
frame_date.pack()

#JOUR
champ=0
jour=StringVar()
ent_jour = Entry(frame_date, width=3,textvariable=jour)
ent_jour.grid(row=11, column=1, sticky =(N,S,E,W))
ent_jour.bind("<ButtonPress-1>",lambda a:click_j())
ent_jour.bind("<Key>",lambda a:appui_j())
jour.set(" JJ") # texte "JJ" au démarage
#
lbl_slache1 = Label(frame_date,text=" / ")
lbl_slache1.grid(row=11,column=2, sticky =(N,S,E,W))
#MOIS
mois=StringVar()
ent_mois = Entry(frame_date, width=3,textvariable=mois)
ent_mois.grid(row=11, column=3, sticky =(N,S,E,W))
ent_mois.bind("<ButtonPress-1>",lambda a:click_m())
ent_mois.bind("<Key>",lambda a:appui_m())
mois.set(" MM") # texte "MM" au demarage
#
lbl_slache2 = Label(frame_date,text=" / ")
lbl_slache2.grid(row=11,column=4, sticky =(N,S,E,W))
#ANNEE
annee=StringVar()
ent_annee = Entry(frame_date, width=5, textvariable=annee)
ent_annee.grid(row=11, column=5, sticky =(N,S,E,W))
ent_annee.bind("<ButtonPress-1>",lambda a:click_a())
ent_annee.bind("<Key>",lambda a:appui_a())
annee.set(" AAAA") #texte "AAAA" au demarage

#Boutton pour annuler l'opération précédente
Annuler=Button(frame_droite, text="Annuler l'opération précédente", command=annul,bd=5,relief=GROOVE, bg="#FF514D").pack(side=TOP)


################### Armature du milieu ##########################


framemilieu = Frame(page_principale ,width = 300,height = 150)
framemilieu.pack(fill=X)
 ### Creation des 4 frames Loyer, Loisirs, Voyage et Alimentation ###

frame_HG = Frame(framemilieu ,width = 500,height = 400,bd=5, relief=GROOVE) # frame Haut Gauche
#frame_HG.config(highlightbackground="black")
frame_HG.grid(row=1,column = 1,columnspan = 2, sticky = (E), padx = 10, pady=5)
frame_HG.grid_propagate(False)

frame_BD = Frame(framemilieu ,width = 500,height = 400,bd=5, relief=GROOVE) #frame Bas Droite
frame_BD.grid(row=2,column = 3 ,columnspan = 2,sticky = (E), padx = 10, pady=5)
frame_BD.grid_propagate(False)

frame_HD = Frame(framemilieu ,width = 500,height = 400, bd=5, relief=GROOVE) #frame Haut Droite
frame_HD.grid(row=1,column = 3,columnspan = 2,sticky = (E), padx = 10, pady=5)
frame_HD.grid_propagate(False)

frame_BG = Frame(framemilieu ,width = 500,height = 400, bd=5, relief=GROOVE) #frame Bas GAuche
frame_BG.grid(row=2,column = 1, columnspan = 2,sticky = (E), padx = 10, pady=5)
frame_BG.grid_propagate(False)

## On partage encore chaque frame en 2 pour que la ligne de dépense/recette s'affiche au bon endroit ##

frame1_HG = Frame(frame_HG, width = 400, height = 160)
frame1_HG.grid(row = 1, column = 1, sticky=(W))
frame1_HG.grid_propagate(False)
frame2_HG = Frame(frame_HG, width = 500, height = 200)
frame2_HG.grid(row = 2, column = 1, sticky = (EW))
frame2_HG.grid_propagate(False)


frame1_HD = Frame(frame_HD, width = 400, height = 160)
frame1_HD.grid(row = 1, column = 1, sticky=(W))
frame1_HD.grid_propagate(False)
frame2_HD = Frame(frame_HD, width = 500, height = 200)
frame2_HD.grid(row = 2, column = 1, sticky = (EW))
frame2_HD.grid_propagate(False)

frame1_BD = Frame(frame_BD, width = 400, height = 160)
frame1_BD.grid(row = 1, column = 1, sticky=(W))
frame1_BD.grid_propagate(False)
frame2_BD = Frame(frame_BD, width = 500, height = 200)
frame2_BD.grid(row = 2, column = 1, sticky = (EW))
frame2_BD.grid_propagate(False)

frame1_BG = Frame(frame_BG, width = 400, height = 160)
frame1_BG.grid(row = 1, column = 1, sticky=(W))
frame1_BG.grid_propagate(False)
frame2_BG = Frame(frame_BG, width = 500, height = 200)
frame2_BG.grid(row = 2, column = 1, sticky = (EW))
frame2_BG.grid_propagate(False)



######################### Cadre haut gauche de la Frame Centrale ##########################



photo_house = PhotoImage(file = 'house.png')
house = Label(frame1_HG, image = photo_house )
house.grid(row = 0 , column = 0 , sticky = W)

police_loyer=tkFont.Font(frame1_HG, size=20, family='URW Gothic', weight = 'bold', underline = 1)

lbl_loyer = Label(frame1_HG,text="Loyer :") #lbl pour label
lbl_loyer.configure(font = police_loyer)
lbl_loyer.grid(padx = 5, pady = 5, sticky = (N,E) , row = 0, column =1)

################## frame21_HG correspondant au titre des colonnes
frame21_HG=Frame(frame2_HG, relief=RAISED, borderwidth=1,width=10, bg='#96B3C0')
frame21_HG.pack(side=TOP,padx=2)

lbl_montant_HG=Label(frame21_HG, text="Montant", width=19, bg='#96B3C0')
lbl_montant_HG.grid(pady= 10,row=0, column=0)

lbl_date_HG=Label(frame21_HG, text="Description", width=20, bg='#96B3C0')
lbl_date_HG.grid(pady= 10,row=0, column=1)

lbl_des_HG=Label(frame21_HG, text="Date", width=20, bg='#96B3C0')
lbl_des_HG.grid(pady= 10,row=0, column=2, columnspan=3)
####################



######################### Cadre haut droit de la Frame Centrale ##########################

photo_loisirs = PhotoImage(file = 'loisirs.png')
loisirs = Label(frame1_HD, image = photo_loisirs )
loisirs.grid(row = 0 , column = 0 , sticky = W)

police_loisirs=tkFont.Font(frame1_HD, size=20, family='URW Gothic', weight = 'bold', underline = 1)

lbl_loisirs = Label(frame1_HD,text="Loisirs :") #lbl pour label
lbl_loisirs.configure(font = police_loisirs)
lbl_loisirs.grid(padx = 5, pady = 5, sticky = (N,E) , row = 0, column =1)
##################

frame21_HD=Frame(frame2_HD,bg='#96B3C0',relief=RAISED, borderwidth=1,width=10) #frame21_HD correspondant au titre des colonnes
frame21_HD.pack(side=TOP, padx=2)

lbl_montant_HD=Label(frame21_HD, text="Montant", width=19,bg='#96B3C0')
lbl_montant_HD.grid(pady= 10,row=0, column=0)

lbl_date_HD=Label(frame21_HD, text="Description", width=20,bg='#96B3C0')
lbl_date_HD.grid(pady= 10,row=0, column=1)

lbl_des_HD=Label(frame21_HD, text="Date", width=20,bg='#96B3C0')
lbl_des_HD.grid(pady= 10,row=0, column=2, columnspan=3)
####################

######################### Cadre bas gauche de la Frame Centrale ##########################

photo_voyages = PhotoImage(file = 'voyages.png')
voyages = Label(frame1_BG, image = photo_voyages )
voyages.grid(row = 0 , column = 0 , sticky = W)

police_voyages=tkFont.Font(frame1_BG, size=20, family='URW Gothic', weight = 'bold', underline = 1)

lbl_voyages = Label(frame1_BG,text="Voyages :") #lbl pour label
lbl_voyages.configure(font = police_voyages)
lbl_voyages.grid(padx = 5, pady = 5, sticky = (N,E) , row = 0, column =1)

##################
frame21_BG=Frame(frame2_BG,bg='#96B3C0', relief=RAISED, borderwidth=1,width=10) #frame21_BG correspondant au titre des colonnes
frame21_BG.pack(side=TOP, padx=2)

lbl_montant_BG=Label(frame21_BG, text="Montant", width=19,bg='#96B3C0')
lbl_montant_BG.grid(pady= 10,row=0, column=0)

lbl_date_BG=Label(frame21_BG, text="Description", width=20,bg='#96B3C0')
lbl_date_BG.grid(pady= 10,row=0, column=1)

lbl_des_BG=Label(frame21_BG, text="Date", width=20,bg='#96B3C0')
lbl_des_BG.grid(pady= 10,row=0, column=2, columnspan=3)
####################

######################### Cadre bas droit de la Frame Centrale ##########################

photo_alimentation = PhotoImage(file = 'alimentation.png')
alimentation = Label(frame1_BD, image = photo_alimentation )
alimentation.grid(row = 0 , column = 0 , sticky = W)

police_alimentation=tkFont.Font(frame1_BD, size=20, family='URW Gothic', weight = 'bold', underline = 1)

lbl_alimentation = Label(frame1_BD,text="Alimentation :") #lbl pour label
lbl_alimentation.configure(font = police_alimentation)
lbl_alimentation.grid(padx = 5, pady = 5, sticky = (N,E) , row = 0, column =1)

##################
frame21_BD=Frame(frame2_BD,bg='#96B3C0',relief=RAISED, borderwidth=1,width=10) #frame21_BD correspondant au titre des colonnes
frame21_BD.pack(side=TOP, padx=2)

lbl_montant_BD=Label(frame21_BD, text="Montant", width=19,bg='#96B3C0')
lbl_montant_BD.grid(pady= 10,row=0, column=0)

lbl_date_BD=Label(frame21_BD, text="Description", width=20,bg='#96B3C0')
lbl_date_BD.grid(pady= 10,row=0, column=1)

lbl_des_BD=Label(frame21_BD, text="Date", width=20,bg='#96B3C0')
lbl_des_BD.grid(pady= 10,row=0, column=2, columnspan=3)
####################

########################################################################################################################################


page_principale.mainloop()
