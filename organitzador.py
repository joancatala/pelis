#!/usr/bin/python
# Comencem el programeta pelis, per organitzar l'oci ;-)
# 2018 Benicarlo - joan@riseup.net
#

# Modulets
#
from os import listdir

# Variables
#
fitxer = open ( 'fitxer.txt', 'w' ) 
contador = 0

# Llegim el directori de peli i muntem el fitxer txt resultant
#
for peli in listdir("/mnt/disc1/joancatala/files/Pelis/"):
    #print contador, " ", peli
    fitxer.write(str(contador) + ' ' + peli + '\n') 
    contador=contador+1

fitxer.close()
