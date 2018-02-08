#!/usr/bin/python
# Comencem el programeta pelis, per organitzar l'oci ;-)
# 2018 Benicarlo - joan@riseup.net
#

# Modulets
#
from os import listdir
from reportlab.pdfgen import canvas

# Variables
#
fitxer = open ( 'fitxer.txt', 'w' ) 
c = canvas.Canvas("fitxer.pdf")
contador = 0
linia = 750

# Llegim el directori de peli i muntem el fitxer txt resultant
#
for peli in listdir("/mnt/disc1/joancatala/files/Pelis/"):
  	fitxer.write(str(contador) + ' ' + peli + '\n') 
	c.drawString(20, linia, str(contador) + ' ' + peli + '\n')
    	contador=contador+1
	linia=linia-20
fitxer.close()

#c.drawString(20, 750, "hola")
c.showPage()
c.save()
