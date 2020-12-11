#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce programme est une version graphique du jeu du pendu
Created on Fri Dec 11 08:16:11 2020
@author: sophie
"""

from tkinter import Tk , Label , Button , StringVar , Entry
import fonctions
import paramètres_pendu 

def proposer():
    global champ
    global nb_vies
    lettre = champ.get()
    vies_maj = int(nb_vies.get())
    _,_,_,vies_maj = fonctions.test_lettre(mot_choisi,lettre,lettres_correctes,lettres_fausses,vies_maj)
    nb_vies.set(str(vies_maj))
    
#Initialisation
mot_choisi = fonctions.choix_mot()
lettres_correctes,lettres_fausses = [],[]
mot_partiel = fonctions.renvoyer_mot(mot_choisi,lettres_correctes)


#Création de la fenêtre principale
mw = Tk()
mw.title('Jeu du pendu')
mw.geometry('1000x1000+300+100')


#Création d'un widget Label pour afficher le mot en cours
label_mot = Label(mw, text = mot_partiel)
label_mot.pack(side = 'top' , pady = 20)

nb_vies = StringVar()
nb_vies.set(str(paramètres_pendu.nb_chances))
label_nb_vies = Label(mw, text = 'nombre de vies', textvariable = nb_vies)
label_nb_vies.pack()


#Création d'un champ de saisi pour soumettre une lettre
lettre = StringVar()
champ = Entry(mw,  textvariable = lettre)
champ.focus_set()
champ.pack(side = 'left' , padx = 20)


#Création du bouton proposer
bouton_proposer = Button (mw , text = 'Proposer cette lettre' , command = proposer)
bouton_proposer.pack(side = 'right' , padx = 20 , pady = 50)



mw.mainloop()