#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce programme contient le jeu du pendu
@author: sophie chauviré
Created on Fri Nov 27 10:57:00 2020
"""

"""
Ce programme s'appuie sur les fichiers fonctions.py et mots.py"
"""
from paramètres_pendu import lines , meilleur_score
from fonctions import*


def jouer_pendu():
    """
    cette fonction sert à jouer au pendu
    entrée : aucune
    sortie : affiche si l'utilisateur a gagné ou perdu,l'éventuel meilleur score
    """
    #initialisation
    mot_choisi = choix_mot()
    lettres_correctes = []
    lettres_fausses = []
    nb_vies = nb_chances
    mot = renvoyer_mot(mot_choisi,lettres_correctes)
    print('\n Prêt à jouer ? le score à battre est de {} \n Le mot à trouver est: {}\n'.format(meilleur_score,mot))
    
    #Le jouer commence à jpuer et propose des lettres
    while mot != mot_choisi and nb_vies > 0 :
        lettre = entrer_lettre()
        mot,lettres_correctes,lettres_fausses,nb_vies = test_lettre(mot_choisi,lettre,lettres_correctes,lettres_fausses,nb_vies)
        print(mot)
              
    #le mot a été trouvé 
    if mot == mot_choisi :
        #on enregistre l'éventuel meilleur score
        if nb_vies > meilleur_score:
            print('\n Vous avez battu le meilleur score, le nouveau meilleur score est: {}'.format(nb_vies))
            with open('meilleur_score.txt','w') as ms:
                ms.write(str(nb_vies))
                ms.close()
        print('\n Félicitations vous avez trouvé le mot:', mot_choisi)
        
    #le nombre de vies du jouer est tombé à 0
    else :
        print('\n Perdu, vous avez gaspillé toutes vos chances sans trouver le mot')
        print('Le mot à trouver était: {}'.format(mot_choisi))
    
    rejouer()


        
        