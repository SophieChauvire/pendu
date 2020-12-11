#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce programme définit les données qui seront utilisées pour le programme jeu_pendu, ie les paramètres du jeu
@author: sophie chauviré
Created on Fri Nov 27 10:56:58 2020
reste à faire: enregistrer les dernières données, comme le nb de vie
"""

#Nombre de chances qu'à le joueur :
nb_chances = 8

#Meilleur score de la partie :
with open('meilleur_score.txt','r') as ms :
    m_s = ms.readline()
    meilleur_score=int(m_s)
    ms.close()

#Création de la liste de jeu avec laquelle on joue :
with open('liste_mots.txt','r') as f:
    lines = [line.strip('\n') for line in f.readlines()]
    f.close()