#!/usr/bin/python3.8
#!-*-coding:utf-8-*

from tkinter import *
import os
from tkinter import ttk
from ttkthemes import themed_tk as tk

compteur_montrer1=0 #Variable global
compteur_montrer2=0

# Permet de montrer ou non son mot de passe
def montrer1():
    global compteur_montrer1
    if compteur_montrer1%2==0:
        password_entry.config(show="")
        compteur_montrer1+=1
    else :
        password_entry.config(show="*")
        compteur_montrer1+=1

def montrer2():
    global compteur_montrer2
    if compteur_montrer2%2==0:
        password_entry1.config(show="")
        compteur_montrer2+=1
    else :
        password_entry1.config(show="*")
        compteur_montrer2+=1

# Supprime lorsque la connexion est bonne
def delete2():
    screen3.destroy()
    screen2.destroy()
    #exec(open("./test-bank.py").read()
    screen.destroy()
    os.system("./test-bank.py")

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Sucess").pack()
  Button(screen3, text = "OK", command =delete2).pack()



def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("500x200+700+400")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("500x200+700+400")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()


def register_user():
  print("working")

  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():

  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()



def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("S'enregistrer")
  screen1.geometry("500x200+700+400")

  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Veuillez rentrez vos informations ci-dessous").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Nom d'utilisateur ").pack()

  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()

  Label(screen1, text = "Mot de passe ").pack()
  frame_mdp=Frame(screen1)
  frame_mdp.pack()
  password_entry =  Entry(frame_mdp, textvariable = password, show='*')
  password_entry.pack(side=LEFT)

  photo = PhotoImage(file='eye1.png')
  photo = photo.subsample(32)
  oeil1=ttk.Button(frame_mdp, image= photo, command = montrer1, width=5)
  oeil1.pack(side=RIGHT)

  Label(screen1, text = "").pack()
  Button(screen1, text = "S'enregistrer", width = 10, height = 1, command = register_user).pack()



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
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Mot de passe").pack()

  frame_mdp_oeil=Frame(screen2)#### frame contenant le mot de passe et l'oeil pour qu'ils soient au même niveau
  frame_mdp_oeil.pack()

  photo = PhotoImage(file='eye1.png')
  photo = photo.subsample(32)
  oeil2=ttk.Button(frame_mdp_oeil, image= photo, command = montrer2, width=5)

  password_entry1 = Entry(frame_mdp_oeil, textvariable = password_verify, show='*')
  password_entry1.pack(side=LEFT)
  oeil2.pack(side=RIGHT)

  Label(screen2, text = "").pack()
  Button(screen2, text = "Connexion", width = 10, height = 1, command = login_verify).pack()


def main_screen():
  global screen


  screen = tk.ThemedTk()
  screen.get_themes()
  screen.set_theme("elegance")

  screen.geometry("500x300+700+400")
  screen.title("Identification")
  Label(text = "Connexion à votre gestionnaire de compte bancaire", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Connexion", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "S'enregistrer",height = "2", width = "30", command = register).pack()


  screen.mainloop()

main_screen()
