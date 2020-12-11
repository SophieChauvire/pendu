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
from paramètres_pendu import*
from jeu_pendu import *


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


def test_lettre(mot_choisi,lettre,lettres_correctes,lettres_fausses,nb_vies):
    """
    Cette fonction renvoie si une lettre fait partie d'un mot ou non, 
    entrées : un mot,une lettre à tester, deux listes de lettres,un entier non nul représentant le nb d'essais
    sorties : un mot, les deux listes entrées modifiées, le nb d'essais modifié
    """
    #1° possilité : la lettre a déja été donnée
    if lettre in lettres_correctes or lettre in lettres_fausses:
        print('Vous avez déjà donné cette lettre')
    
    #2e posibilité : la lettre est dans le mot
    elif lettre in mot_choisi:
            lettres_correctes.append(lettre)
            print('\n Bravo ! Vous avez trouvé une lettre. Il vous reste {} vies'.format(nb_vies))
            
    #3e possibilité : la lettre n'est pas dans le mot, le joueur perd une vie
    else:
            lettres_fausses.append(lettre)
            nb_vies-=1
            print('\n Non, cette lettre ne figure pas dans le mot, il vous reste {} vies'.format(nb_vies))
    mot=renvoyer_mot(mot_choisi,lettres_correctes)
    return(mot,lettres_correctes,lettres_fausses,nb_vies)
    
    

def rejouer():
    """
    Cette fonction relance la fonction jouer_pendu() si l'utilisateur donne un réponse positive
    entrée : aucune
    sortie : aucune
    """
    #on demande à l'utilisateur s'il veut rejouer
    reponse = input('Souhaitez vous relancer une partie ?')
    #on teste sa réponse, elle doit être assez proche du mot oui
    if reponse in ['oui','OUI','O','Oui','o','ok','OK','Ok']:
        jouer_pendu()
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    