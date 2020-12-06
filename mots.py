#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:56:58 2020

@author: sophie
"""

with open('liste_mots.txt','r') as f:
    lines=[line.strip('\n') for line in f.readlines()]