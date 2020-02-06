#!/usr/bin/python3.8
#!-*-coding:utf-8-*


from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import os
from tkinter import messagebox

page_principale = Tk()
page_principale.title("Bank managment")
page_principale.geometry("1400x920+250+90") # taille et placement de la page


########## LES FONCTIONS ######################################################### "loisirs","loyer","voyages","nouriture"

def addBox():
    global test34
    global x,y,z
    x = int(x)
    y = int(y)
    z = int(z)


    val_pOm = pOm.get()
    print(val_pOm)

    select = combo.get()
    montant=ent_montant.get()
    j=ent_jour.get()
    m=ent_mois.get()
    a=ent_annee.get()
    affiche=entree_depense.get()
    select = combo.get()

################################################ Test Des Exceptions possibles ########################################
    try : #### Exception pour le Montant
        int(montant)
    except ValueError:
        messagebox.showinfo("Attention","Veuillez saisir un nombre pour le montant svp!", icon="warning")
        return

    try : #### Exception pour le Jour
        test1=int(j)
        assert test1<=31
    except ValueError:
        messagebox.showinfo("Attention","Veuillez saisir un nombre pour le jour svp!", icon="warning")
        return
    except AssertionError:
        messagebox.showinfo("Attention","vous avez saissi un numéro infèrieur à 31 pour le jour !", icon="warning")
        return

    try : #### Exception pour le Mois
        test2=int(m)
        assert test2<=12
    except ValueError:
        messagebox.showinfo("Attention","Veuillez saisir un nombre pour le mois svp!", icon="warning")
        return
    except AssertionError:
        messagebox.showinfo("Attention","vous avez saissi un numéro infèrieur à 12 pour le mois !", icon="warning")
        return

    try : #### Exception pour l'année
        int(a)
    except ValueError:
        messagebox.showinfo("Attention","Veuillez saisir un nombre pour l'année svp!", icon="warning")
        return

    try :
        test3=select
        assert test3 == "loisirs" or test3 == "voyages" or test3=="loyer" or test3=="alimentation"
    except AssertionError:
        messagebox.showinfo("Attention","Veuillez selectionner un type svp!", icon="warning")
        return
####################################################################################
    if select == "loisirs":
         if montant != "" and j!= "" and m != "" and a != "" and affiche != "" and int(j)+1<32 and int(m)+1<13 and (val_pOm == 1 or val_pOm == 2):
             frame = Frame(frame2_HD, bg = "cyan")
             frame.pack(side=BOTTOM,fill=Y)
             test34=frame

    if select == "voyages" :
         if montant != "" and j!= "" and m != "" and a != "" and affiche != "" and int(j)+1<32 and int(m)+1<13 and (val_pOm == 1 or val_pOm == 2):
             frame = Frame(frame2_BG, bg = "cyan")
             frame.pack(side=BOTTOM,fill=Y)
             test34=frame

    if select == "loyer" :
         if montant != "" and j!= "" and m != "" and a != "" and affiche != "" and int(j)+1<32 and int(m)+1<13 and (val_pOm == 1 or val_pOm == 2):
             frame = Frame(frame2_HG, bg = "green")
             frame.pack(side=BOTTOM,fill=Y)
             test34=frame

    if select == "alimentation" :
         if montant != "" and j!= "" and m != "" and a != "" and affiche != "" and int(j)+1<32 and int(m)+1<13 and (val_pOm == 1 or val_pOm == 2):
             frame = Frame(frame2_BD, bg = "cyan")
             frame.pack(side=BOTTOM,fill=Y)
             test34=frame


    if val_pOm == 1:
        montant=ent_montant.get()

        if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)+1>32 or int(m)+1>13 or (val_pOm != 1 and val_pOm != 2):
            messagebox.showinfo("Attention","Vous avez saisi au moins une information incorrecte !", icon="warning")
            print("Tout va bien")

        else :
            lbl1 = Label(frame,fg='red', width=20)
            lbl1["text"]="- "+montant+" € "
            lbl1.grid(row=0, column=0)
            result = x - int(montant)
            result_m = y - int(montant)
            print(x)
            lblS["text"]= result
            lblD["text"]= result_m
            x = str(result)
            y = str(result_m)
            result = 0
            result_m = 0

    if val_pOm == 2:
        montant=ent_montant.get()


        if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)+1>32 or int(m)+1>13 or (val_pOm != 1 and val_pOm != 2):
            messagebox.showinfo("Attention","Vous avez saisi au moins une information incorrecte !", icon="warning")
            print("Tout va bien")





        else :

            lbl1 = Label(frame,fg='#26BD34', width=20)
            lbl1["text"]=montant+" € "
            lbl1.grid(row=0, column=0)
            result = x + int(montant)
            result_p = z + int(montant)
            print(x)
            lblS["text"]= result
            lblR["text"]= result_p
            x = str(result)
            z = str(result_p)
            result = 0
            result_p = 0




    affiche=entree_depense.get()

    if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)+1>32 or int(m)+1>13 or (val_pOm != 1 and val_pOm != 2):
        messagebox.showinfo("Attention","Vous avez saisi au moins une information incorrecte !", icon="warning")

    else :
        lbl3 = Label(frame, width=20)
        lbl3["text"]=affiche
        lbl3.grid(row=0, column=1, sticky=(N,S,E,W))

    j=ent_jour.get()
    if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)+1>32 or int(m)+1>13 or (val_pOm != 1 and val_pOm != 2):
        pass

    else :
        choix=jour.get()
        if champ==1:
            print(choix)
            lbl2j = Label(frame, width=6)
            lbl2j["text"]=j+"/"
            lbl2j.grid(row=0, column=2, sticky=(N,S,E,W))
        else:
            print("aucune saisie")

    m=ent_mois.get()
    if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)+1>32 or int(m)+1>13 or (val_pOm != 1 and val_pOm != 2):
        pass

    else :
        choix=mois.get()
        if champ==1:
            print(choix)
            lbl2m = Label(frame, width=6)
            lbl2m["text"]=m+"/"
            lbl2m.grid(row=0, column=3, sticky=(N,S,E,W))
        else:
            print("aucune saisie")

    a=ent_annee.get()
    if montant == "" or j== "" or m == "" or a == "" or affiche == "" or int(j)+1>32 or int(m)+1>13 or (val_pOm != 1 and val_pOm != 2):
        pass
    else :
        choix=annee.get()
        if champ==1:
            print(choix)
            lbl2a = Label(frame, width=6)
            lbl2a["text"]=a
            lbl2a.grid(row=0, column=4)
        else:
            print("aucune saisie")

        if montant != "" and j!= "" and m != "" and a != "" and affiche != "" and int(j)+1<32 and int(m)+1<13 and (val_pOm == 1 and val_pOm == 2):
            all_entries.append( (lbl1, lbl2j,lbl2m,lbl2a, lbl3) )

#------------------------------------
test34=Frame()

def click_j():
    global champ
    champ=1
    jour.set("")
    ent_jour.config(fg="black")

def click_m():
    global champ
    champ=1
    mois.set("")
    ent_mois.config(fg="black")

def click_a():
    global champ
    champ=1
    annee.set("")
    ent_annee.config(fg="black")

def appui_j():
    choix=jour.get()
    if len(choix)+1>2:
        print("STOP")
        ent_jour.delete([1])
    else:
        print(len(choix)+1)

def appui_m():
    choix=mois.get()
    if len(choix)+1>2:
        print("STOP")
        ent_mois.delete([1])
    else:
        print(len(choix)+1)

def appui_a():
    choix=annee.get()
    if len(choix)+1>4:
        print("STOP")
        ent_annee.delete([3])
    else:
        print(len(choix)+1)

def annul():

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

##################SOLDE#######################
lF = LabelFrame(frame2_haut,text='SOLDE', width=250,height=100, bg="#848CE9")
lF.pack(side=LEFT, padx=5)
lF.pack_propagate(0)

lblS = Label(lF, bg="#848CE9")
lblS.pack(side=LEFT, padx=10)

lble = Label(lF, text=" € ", bg="#848CE9")
lble.pack(side=RIGHT, padx=10)

###################RECETTES#######################
lF2 = LabelFrame(frame2_haut, text="RECETTES", width=250,height=100,  bg="#A0E8A6")
lF2.pack(side=LEFT, padx=5)
lF2.pack_propagate(0)

lblR = Label(lF2, bg="#A0E8A6")
lblR.pack(side=LEFT, padx=10)

lble = Label(lF2, text=" € ", bg="#A0E8A6")
lble.pack(side=RIGHT, padx=10)

###################DEPENSES######################"
lF3 = LabelFrame(frame2_haut, text="DEPENSES", width=250,height=100,  bg="#FF7E65")
lF3.pack(side=LEFT, padx=5)
lF3.pack_propagate(0)

lblD = Label(lF3, bg="#FF7E65")
lblD.pack(side=LEFT, padx=10)

lble = Label(lF3, text=" € ", bg="#FF7E65")
lble.pack(side=RIGHT, padx=10)

l4 = Label(frame2_haut, text="Balances des \n différents comptes", width=25, font="Arial",height=5, bg="#FFEA85").pack(side=LEFT, padx=5)
b4 = Button(frame2_haut, text="Actualiser", font="Arial", width=15, height=2, bg="#8E96A3",activebackground="#C9D7E8", command = addBox).pack(side=LEFT, padx=5)



#################### AJOUTER UNE DEPENSE ######################

######### Frame #####
frame_droite = Frame(page_principale ,width = 200,height = 1000)
frame_droite.pack(side=RIGHT, fill=Y)

frame_test_droite=Frame(frame_droite, relief=GROOVE, bd=5)
frame_test_droite.pack(side = TOP, pady=20)

police1=tkFont.Font(frame_test_droite, size=10, family='Source Code Pro Semibold', underline = 0)

#RadioButton Dépense ou recette
pOm = IntVar()

ajoutDR = Label(frame_test_droite, text="Ajouter une Dépense \n ou une Recette")
ajoutDR.configure(font=police1)
ajoutDR.pack(side=TOP, pady=2)

frame_radiobutton=Frame(frame_test_droite)
frame_radiobutton.pack()


moins = Radiobutton(frame_radiobutton, text="Dépense", variable=pOm, value=1)
moins.configure(font = police1)
moins.pack(side=LEFT)

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
#
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
lbl_slache1 = Label(frame_montant,text=" € ")
lbl_slache1.configure(font = police1)
lbl_slache1.pack(side=RIGHT)
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
jour.set(" JJ")
#
lbl_slache1 = Label(frame_date,text=" / ")
lbl_slache1.grid(row=11,column=2, sticky =(N,S,E,W))
#MOIS
mois=StringVar()
ent_mois = Entry(frame_date, width=3,textvariable=mois)
ent_mois.grid(row=11, column=3, sticky =(N,S,E,W))
ent_mois.bind("<ButtonPress-1>",lambda a:click_m())
ent_mois.bind("<Key>",lambda a:appui_m())
mois.set(" MM")
#
lbl_slache2 = Label(frame_date,text=" / ")
lbl_slache2.grid(row=11,column=4, sticky =(N,S,E,W))
#ANNEE
annee=StringVar()
ent_annee = Entry(frame_date, width=5, textvariable=annee)
ent_annee.grid(row=11, column=5, sticky =(N,S,E,W))
ent_annee.bind("<ButtonPress-1>",lambda a:click_a())
ent_annee.bind("<Key>",lambda a:appui_a())
annee.set(" AAAA")

#Boutton pour annuler l'opération précédente
Annuler=Button(frame_droite, text="Annuler l'opération précédente", command=annul,bd=5,relief=GROOVE, bg="#FF514D").pack(side=TOP)


################### Armature du milieu ##########################


framemilieu = Frame(page_principale ,width = 300,height = 150)
framemilieu.pack(fill=X)


frame_HG = Frame(framemilieu ,width = 500,height = 400,bd=5, relief=GROOVE)
#frame_HG.config(highlightbackground="black")
frame_HG.grid(row=1,column = 1,columnspan = 2, sticky = (E), padx = 10, pady=5)
frame_HG.grid_propagate(False)

frame_BD = Frame(framemilieu ,width = 500,height = 400,bd=5, relief=GROOVE)
frame_BD.grid(row=2,column = 3 ,columnspan = 2,sticky = (E), padx = 10, pady=5)
frame_BD.grid_propagate(False)

frame_HD = Frame(framemilieu ,width = 500,height = 400, bd=5, relief=GROOVE)
frame_HD.grid(row=1,column = 3,columnspan = 2,sticky = (E), padx = 10, pady=5)
frame_HD.grid_propagate(False)

frame_BG = Frame(framemilieu ,width = 500,height = 400, bd=5, relief=GROOVE)
frame_BG.grid(row=2,column = 1, columnspan = 2,sticky = (E), padx = 10, pady=5)
frame_BG.grid_propagate(False)

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

##################
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

frame21_HD=Frame(frame2_HD,bg='#96B3C0',relief=RAISED, borderwidth=1,width=10)
frame21_HD.pack(side=TOP, padx=2)

lbl_montant_HD=Label(frame21_HD, text="Montant", width=19,bg='#96B3C0')
lbl_montant_HD.grid(pady= 10,row=0, column=0)

lbl_date_HD=Label(frame21_HD, text="Description", width=20,bg='#96B3C0')
lbl_date_HD.grid(pady= 10,row=0, column=1)

lbl_des_HD=Label(frame21_HD, text="Date", width=20,bg='#96B3C0')
lbl_des_HD.grid(pady= 10,row=0, column=2, columnspan=3)
####################

######################### Cadre bas droit de la Frame Centrale ##########################

photo_voyages = PhotoImage(file = 'voyages.png')
voyages = Label(frame1_BG, image = photo_voyages )
voyages.grid(row = 0 , column = 0 , sticky = W)

police_voyages=tkFont.Font(frame1_BG, size=20, family='URW Gothic', weight = 'bold', underline = 1)

lbl_voyages = Label(frame1_BG,text="Voyages :") #lbl pour label
lbl_voyages.configure(font = police_voyages)
lbl_voyages.grid(padx = 5, pady = 5, sticky = (N,E) , row = 0, column =1)

##################
frame21_BG=Frame(frame2_BG,bg='#96B3C0', relief=RAISED, borderwidth=1,width=10)
frame21_BG.pack(side=TOP, padx=2)

lbl_montant_BG=Label(frame21_BG, text="Montant", width=19,bg='#96B3C0')
lbl_montant_BG.grid(pady= 10,row=0, column=0)

lbl_date_BG=Label(frame21_BG, text="Description", width=20,bg='#96B3C0')
lbl_date_BG.grid(pady= 10,row=0, column=1)

lbl_des_BG=Label(frame21_BG, text="Date", width=20,bg='#96B3C0')
lbl_des_BG.grid(pady= 10,row=0, column=2, columnspan=3)
####################

######################### Cadre bas gauche de la Frame Centrale ##########################

photo_alimentation = PhotoImage(file = 'alimentation.png')
alimentation = Label(frame1_BD, image = photo_alimentation )
alimentation.grid(row = 0 , column = 0 , sticky = W)

police_alimentation=tkFont.Font(frame1_BD, size=20, family='URW Gothic', weight = 'bold', underline = 1)

lbl_alimentation = Label(frame1_BD,text="Alimentation :") #lbl pour label
lbl_alimentation.configure(font = police_alimentation)
lbl_alimentation.grid(padx = 5, pady = 5, sticky = (N,E) , row = 0, column =1)

##################
frame21_BD=Frame(frame2_BD,bg='#96B3C0',relief=RAISED, borderwidth=1,width=10)
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
