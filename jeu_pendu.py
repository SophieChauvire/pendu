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
from paramètres_pendu import*
from fonctions import*


def jouer_pendu():
    """
    cette fonction sert à jouer au pendu
    entrée : aucune
    sortie : affiche si l'utilisateur a gagné ou perdu,l'éventuel meilleur score
    """
    mot_choisi = choix_mot()
    lettres_correctes = []
    lettres_fausses = []
    nb_vies = nb_chances
    mot = renvoyer_mot(mot_choisi,lettres_correctes)
    print('\n Prêt à juer ? le score à battre est de {} \n Le mot à trouver est: {}\n'.format(meilleur_score,mot))
    
    #Le joueur commence la partie et propose des lettres 
    while mot != mot_choisi and nb_vies > 0 :
        lettre = entrer_lettre()
        
        #1e possibilité : la lettre a déjà été donnée
        if lettre in lettres_correctes or lettre in lettres_fausses :
            print('Vous avez déjà donné cette lettre')
            
        #2e posibilité : la lettre est dans le mot
        elif lettre in mot_choisi:
            lettres_correctes.append(lettre)
            print('\n Bravo ! Vous avez trouvé une lettre. Il vous reste {} vies'.format(nb_vies))
            
        #3e possibilité : la lettre n'est pas dans le mot, le joueru perd une vie
        else:
            lettres_fausses.append(lettre)
            nb_vies-=1
            print('\n Non, cette lettre ne figure pas dans le mot, il vous reste {} vies'.format(nb_vies))
        mot = renvoyer_mot(mot_choisi,lettres_correctes)
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
        
    #Si le joueur souhaite relancer une partie:
    reponse = input('Souhaitez vous relancer une partie ?')
    if reponse in ['oui','OUI','O','Oui','o']:
        jouer_pendu()

        
        