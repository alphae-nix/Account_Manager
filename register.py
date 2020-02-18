#!/usr/bin/python3.8
#!-*-coding:utf-8-*

from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time


compteur_montrer1=0 #Variable global
compteur_montrer2=0

# Permet de montrer ou non son mot de passe dans la page Login
def montrer1():
    global compteur_montrer1
    if compteur_montrer1%2==0: #Si la variable global compteur_montrer1 est pair alors le mot de passe est affiché en clair
        password_entry.config(show="")
        compteur_montrer1+=1 #On incrémente la variable
    else :
        password_entry.config(show="*")#Si la variable global compteur_montrer1 est impair alors le mot de passe n'est pas affiché en clair mais remplacé par des *
        compteur_montrer1+=1 #On i  ncrémente la variable

# Permet de montrer ou non son mot de passe dans la page Register
def montrer2(): # Même fonctionnement que pour montrer1 mais pour la page Register
    global compteur_montrer2
    if compteur_montrer2%2==0:
        password_entry1.config(show="")
        compteur_montrer2+=1
    else :
        password_entry1.config(show="*")
        compteur_montrer2+=1

# Supprime lorsque le mot de passe associé au nom d'utilisateur est juste
def delete2():
    screen3.destroy() # ici on ferme les différentes fenêtre ouvertes
    screen2.destroy()
    screen.destroy()
    os.system("./test-bank.py") #On ouvre ici le 2eme fichier qui est l'application de gestionnaire de finance

def delete3(): #Permet de fermer screen4 = page affichant une erreur dans la saisie du mot de passe
  screen4.destroy()

def delete4(): #Permet de fermer screen5 = page affichant une erreur dans la saisie du nom d'utilisateur
  screen5.destroy()

def progress(currentValue): # Fonction permettant la mise à jour de la barre de chargement(cf.fonction suivante)
    progbar["value"]=currentValue

def login_sucess(): # Affiche une page informant à l'utilisateur qu'il à bien réussi à se connecter à son compte
  global screen3
  screen3 = Toplevel(screen) #fenêtre qui possède une existence indépendante de screen
  screen3.title("Succès") #titre de la sous page
  screen3.geometry("500x200+700+400") #taille et positionnement
  Label(screen3, text = "Connexion réussi !").pack()

  global progbar
  progbar= ttk.Progressbar(screen3, orient=HORIZONTAL, length=200) #Création de la barre de chargement
  progbar.pack(pady=50)
  #On initialise différentes valeurs
  maxValue=100
  currentValue=0
  progbar["value"]=currentValue #Valeur courrante de la Progressbar
  progbar["maximum"]=maxValue #Valeur maximum de la Progressbar
  divisions=10
  for i in range(divisions): #Compteur permettant le chargement de la
    currentValue=currentValue+10
    progbar.after(200, progress(currentValue)) #On met à jour(on utilise la fonction progress initialisé plus haut) la barre de chargement toutes les 0.2s
    progbar.update() # barre de chargement est mise à jour
  delete2() #une fois la barre de chargement terminé on exécute la fonction delete2() (cf.plus haut)

def password_not_recognised(): #Fonction permettant d'afficher un message d'erreur pour signaler à l'utilisateur que le mot de passe rentré est faux
  global screen4
  screen4 = Toplevel(screen) #création de la page
  screen4.title("Erreur")
  screen4.geometry("500x200+700+400")
  Label(screen4, text = "Erreur mot de passe").pack()
  Button(screen4, text = "OK", command =delete3).pack()
  screen4.bind_all("<KeyPress-Return>", lambda test4:delete3()) #Raccourcis via la touche "Enter",permet à l'utilisateur de gagner du temps(il n'est pas obligé de se servir de sa souris)
  #Une fois la touche "Enter" appyer cela produira la même action que le bouton (cela appelera la fonction delete3()

def user_not_found(): #Fonction permettant d'afficher un message d'erreur pour signaler à l'utilisateur que le nom d'utilisateur rentré est faux
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Erreur")
  screen5.geometry("500x200+700+400")
  Label(screen5, text = "Utilisateur inconnue").pack()
  Button(screen5, text = "OK", command =delete4).pack()
  screen5.bind_all("<KeyPress-Return>", lambda test5:delete4())


def register_user(): # Fonction permettant l'enregistrement d'un nouveau compte
  global username_info

  username_info = username.get() #récupération de la saisi des information données par l'utilisateur
  password_info = password.get()

  #### Gestion des Exceptions
  if username_info == "" : # On test si l'utilisateur à au moins indiqué un nom d'utilisateur
    messagebox.showinfo("Attention","Veuillez saisir un nom d'utilisateur pour vous enregistrer!", icon="warning")
    return

    # Une fois l'exception passé on enregistre le tout dans un nouveau fichier
  file=open(username_info, "w") #Création d'un nouveau fichier avec pour nom, le nom d'utilsateur donné par la variable "username_info"
  file.write(username_info+"\n") #On écrit sur la première ligne le nom d'utilisateur
  file.write(password_info) # et sur la 2eme ligne le mot de passe
  file.close()

  username_entry.delete(0, END) # On remet les champs à 0 pour pouvoir enregistrer un nouvel utilsateur
  password_entry.delete(0, END)

  messagebox.showinfo("Enregistrement Validé","Enregistrement Réussi") #message de confirmation d'enregistrement
  screen1.destroy() # On quitte la fenêtre et on est de retour au menu


def login_verify(): # Fonction permettant la vérification du nom d'utilisateur et du mot de passe

  username1 = username_verify.get() #récupération de la saisi des information données par l'utilisateur
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir() #liste les fichiers
  if username1 in list_of_files: #On regarde si un nom de fichier correspond au nom passé dans la variable username1
    file1 = open(username1, "r") #si oui alors on rentre dans le fichier en question
    verify = file1.read().splitlines()
    if password1 in verify: #2eme étape, on vérifie que le mot de passe stocké dans le fichier est le même que celui stocké dans la variable "password1"
        login_sucess()
    else: # Si pas de mot de passe où que les 2 valeurs sont différentes
        password_not_recognised() # alors on appelle la fontion "password_not_recognised"

  else: #si non alors on sort et appel de la fonction "user_not_found"
        user_not_found()

############################# Page d'Enregistrement ######################################
def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("S'enregistrer")
  screen1.geometry("500x200+700+400")

  global username
  global password
  global username_entry
  global password_entry
  username = StringVar() # Variables permettant de stocker le mot de passe et le nom d'utilisateur
  password = StringVar()

  Label(screen1, text = "Veuillez rentrez vos informations ci-dessous").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Nom d'utilisateur ").pack()

  username_entry = Entry(screen1, textvariable = username) # Entrée ou l'utilisateur saisi un nom d'utilisateur qui sera sauvegarder dans la variable "username"
  username_entry.pack()

  Label(screen1, text = "Mot de passe ").pack()
  frame_mdp=Frame(screen1) #Frame contenant l'entrée de saisi de mot de passe et le boutton oeil permettant ou non d'afficher en clair son mot de passe
  frame_mdp.pack()
  password_entry =  Entry(frame_mdp, textvariable = password, show='*')# Entrée ou l'utilisateur saisi un mot de passe pour son compte, ilsera sauvegarder dans la variable "password"
  password_entry.pack(side=LEFT)

  oeil1=ttk.Button(frame_mdp, image= photo, command = montrer1, width=5) #Bouton oeil pour afficher ou non son mot de passe
  oeil1.pack(side=RIGHT)

  Label(screen1, text = "").pack()
  Button(screen1, text = "S'enregistrer", width = 10, height = 1, command = register_user).pack() # Va appeler la fonction "register_user"

  screen1.bind_all("<KeyPress-Return>", lambda test2:register_user()) # Raccourcis clavier pour le bouton


############################# Page de Connexion ######################################
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Connexion")
  screen2.geometry("500x200+700+400")
  Label(screen2, text = "Veuillez rentrez vos informations ci-dessous").pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify

  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1

  Label(screen2, text = "Nom d'utilisateur").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)# Entrée où l'utilisateur tape son nom d'utilisateur
  #Le nom d'utilisateur sera sauvegarder dans la variable username_verify
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Mot de passe").pack()

  frame_mdp_oeil=Frame(screen2)# frame contenant le mot de passe et l'oeil pour qu'ils soient au même niveau
  frame_mdp_oeil.pack()

  oeil2=ttk.Button(frame_mdp_oeil, image= photo, command = montrer2, width=5) #Boutton oeil pour voir ou non son mot de passe

  password_entry1 = Entry(frame_mdp_oeil, textvariable = password_verify, show='*') # Entrée où l'utilisateur tape son mot de passe
  #Le mot de passe sera sauvegarder dans la variable password_entry1
  password_entry1.pack(side=LEFT)
  oeil2.pack(side=RIGHT)

  Label(screen2, text = "").pack()
  Button(screen2, text = "Connexion", width = 10, height = 1, command = login_verify).pack() # Va appeler la fonction login_verify pour vérifier que le mot de passe et le nom d'utilisateur soient bons

  screen2.bind_all("<KeyPress-Return>", lambda test1:login_verify()) # Création d'un raccourci avec la touche "Enter" du clavier

############################# PAGE D'ACCUEIL ########################################################
def main_screen():
  global screen
  global photo

  screen = Tk()
  photo1 = PhotoImage(file='eye1.png')
  photo = photo1.subsample(32)

  screen.geometry("500x300+700+400") #Taille/emplacement de la page
  screen.title("Identification") #Titre de la page
  Label(text = "Connexion à votre gestionnaire de compte bancaire", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Connexion", height = "2", width = "30", command = login).pack() #Permet d'afficher la page de connexion à son compte
  Label(text = "").pack()
  Button(text = "S'enregistrer",height = "2", width = "30", command = register).pack() #Permet d'afficher la page d'enregistrement d'un compte


  screen.mainloop()

main_screen() #appel de la fonction main_screen
