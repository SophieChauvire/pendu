#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:55:22 2020

@author: sophie
"""

import random as rd
import string
from mots import*
from jeu_pendu import*

def choix_mot():
    m=rd.randint(0,len(lines))
    return lines[m]
 

def entrer_lettre():
    lettre = input("Entrez une lettre : ")
    if lettre not in string.ascii_letters or len(lettre)>1:
        print("Merci d'entrer une lettre")
        return entrer_lettre()
    else:
        lettre = lettre.upper()
    return lettre
    
def renvoyer_mot(mot_choisi,liste_lettres):
    mot_partiel=''
    for i in mot_choisi:
        if i in liste_lettres :
            mot_partiel+=i
        else :
            mot_partiel+=' _'
    return mot_partiel

def test_lettre(lettre,mot_choisi):
    if lettre in mot_choisi:
        liste_lettres.append(lettre)
    else:
        liste_lettres_fausses.append(lettre)