#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:57:00 2020

@author: sophie
"""

from mots import*
from fonctions import*

def jouer_pendu():
    mot_choisi=choix_mot()
    liste_lettres=[]
    liste_lettres_fausses=[]
    mot=renvoyer_mot(mot_choisi,liste_lettres)
    print(mot)
    while mot!=mot_choisi :
        lettre = entrer_lettre()
        test_lettre(lettre,mot_choisi)
        mot = renvoyer_mot(mot_choisi,liste_lettres)
        print(mot)
        