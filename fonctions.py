#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce programme contient les focntions nécessaires pour jouer au jeu du pendu
@author: sophie chauviré
Created on Fri Nov 27 10:55:22 2020
"""


"""ce programme s'appuie sur les bibliothèqes random et string
ainsi que sur le fichier mot.py
"""
from random import randint
import string
from paramètres_pendu import *


def choix_mot():
    """
    cette fonction choisit un mot parmis la liste lines définie dans le fichier paramètres_pendu.py
    entré : aucune
    sortie : renvoie un élement de type str de la liste lines
    """
    m=randint(0,len(lines)-1)
    return lines[m]
 

def entrer_lettre():
    """
    cette fonction renvoie une lettre entrée par l'utilisateur, si ce qu'entre l'utilisateur n'est pas 
    une lettre la fonction est rappelée jusqu'à avoir une lettre
    entrée : aucune
    sortie : renvoie une lettre majusucule
    """
    lettre = input("Entrez une lettre : ")
    
    #On regarde si l'entrée donnée par l'utilisateur est bien une lettre
    if lettre not in string.ascii_letters or len(lettre)>1:
        print("Merci d'entrer une lettre valide")
        return entrer_lettre()
    
    #si c'est bien une lettre, on la met en majuscules 
    else:
        lettre = lettre.upper()
    return lettre
    

def renvoyer_mot(mot_choisi,liste_lettres):
    """
    cette fonction renvoit un mot partiellement construit en fonction des lettres trouvées par l'utilisateur et du mot à trouver
    entrées : le mot à trouver qui a été choisi par la machine
            la liste des lettres contenues dans le mot, trouvées par l'utilisateur
    sortie : renvoie un mot partiellement contruit, affichant les lettres trouvées par l'utilisateur et des '_' pour les lettres qui restent à trouver
    """
    mot_partiel=''
    for i in mot_choisi:
        #la lettre a été trouvée donc on l'affiche
        if i in liste_lettres :
            mot_partiel+=i
        #la lettre n'a pas été trouvée, on affiche _ à la place 
        else :
            mot_partiel+=' _'
    return mot_partiel

