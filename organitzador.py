#!/usr/bin/python
#

#################################################################################
# Modulets
#################################################################################
import os
from os import listdir
from reportlab.platypus import ( BaseDocTemplate, PageTemplate, Frame, Paragraph)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm

#################################################################################
# Generem un fitxer de text "pelis_brut.txt"
#################################################################################
def generem_txt(filename):

    fitxer = open ( 'pelis_brut.txt', 'w' )
    contador = 0
    linia = 750

    # Llegim el directori de peli i muntem el "pelis_brut.txt" resultant
    #
    for peli in listdir("/mnt/disc1/joancatala/files/Pelis/"):
            fitxer.write(str(contador) + ' ' + peli + '\n')
            contador=contador+1
            linia=linia-20
    fitxer.close()


#################################################################################
# Netejem el "pelis_brut.txt", generem un "pelis.txt" final i esborrem el brut
#################################################################################
# 
def netegem_fitxer(filename):

    with open('pelis_brut.txt', 'r') as file :
      filedata = file.read()

    # Reemplacem formats
    filedata = filedata.replace('.avi', ' ')
    filedata = filedata.replace('.mkv', ' ')
    filedata = filedata.replace('(Dual)', ' ')
    # Reemplacem merdes de Xvid, DivX, etc...
    filedata = filedata.replace('.HDrip', ' ')
    filedata = filedata.replace('[dvdrip]', ' ')
    filedata = filedata.replace('DVDRip', ' ')
    filedata = filedata.replace('[DVD-Rip]', ' ')
    filedata = filedata.replace('(dvdrip)', ' ')
    filedata = filedata.replace('.Xvid', ' ')
    filedata = filedata.replace('Xvid', ' ')
    filedata = filedata.replace('(HDRip)', ' ')
    filedata = filedata.replace('[HDRIP]', ' ')
    filedata = filedata.replace('[HDRip]', ' ')
    filedata = filedata.replace('5.1', ' ')
    filedata = filedata.replace('AC3', ' ')
    filedata = filedata.replace('[HDrip-XviD-AC3]', ' ')
    filedata = filedata.replace('[BRrip X264 MKV]', ' ')
    filedata = filedata.replace('[HDrip-XviD- ]', ' ')
    filedata = filedata.replace('[DVDrip]', ' ')
    # Reemplacem merdes de webs
    filedata = filedata.replace('[www.newpct1.com]', ' ')
    filedata = filedata.replace('(DVDRip.Divx.Spanish)', ' ')
    filedata = filedata.replace('.www.lokotorrents.com', ' ')
    filedata = filedata.replace('www.lokotorrents.com', ' ')
    filedata = filedata.replace('.Www.LokoTorrents.Com', ' ')
    filedata = filedata.replace(',WwW.LoKoTorrents.CoM', ' ')
    filedata = filedata.replace('.by.jurimu', ' ')
    filedata = filedata.replace('M1080.www.newpct1.com', ' ')
    filedata = filedata.replace('(EliteTorrent.net)', ' ')
    filedata = filedata.replace('[www.zonatorrent.com]', ' ')
    # Reemplacem idioma
    filedata = filedata.replace('Animacion.Spanish', ' ')
    filedata = filedata.replace('[Spanish]', ' ')
    filedata = filedata.replace('[spanish]', ' ')
    filedata = filedata.replace('[  Spanish]', ' ')
    filedata = filedata.replace('[AC3 Spanish]', ' ')
    filedata = filedata.replace('[Castellano]', ' ')
    filedata = filedata.replace('(spanish)', ' ')
    filedata = filedata.replace('( .Spanish)', ' ')
    filedata = filedata.replace('( .Divx.Spanish)', ' ')
    filedata = filedata.replace('[spanish]', ' ')
    # Reemplacem simbols rars
    filedata = filedata.replace('_', ' ')
    filedata = filedata.replace('( )', ' ')
    filedata = filedata.replace('[ ]', ' ')
    filedata = filedata.replace('.', ' ')

    # Escrivim els canvis al fitxer
    with open('pelis.txt', 'w') as file:
       file.write(filedata)

    os.remove('pelis_brut.txt')

#################################################################################
# Generem el fitxer de pdf "pelis.pdf"
#################################################################################
def build_pdf(filename):
    doc = BaseDocTemplate(filename)
    column_gap = 1 * cm

    cos = ParagraphStyle('personalitzat', fontSize=8.5, leading=6, spaceBefore=5)

    doc.addPageTemplates(
        [
            PageTemplate(
                frames=[
                    Frame(
                        doc.leftMargin,
                        doc.bottomMargin,
                        doc.width / 2,
                        doc.height,
                        id='left',
                        rightPadding=column_gap / 2,
                        showBoundary=0  # set to 1 for debugging
                    ),
                    Frame(
                        doc.leftMargin + doc.width / 2,
                        doc.bottomMargin,
                        doc.width / 2,
                        doc.height,
                        id='right',
                        leftPadding=column_gap / 2,
                        showBoundary=0
                    ),
                ]
            ),
        ]
    )

    flowables=[] 
    fitxer = open ( 'pelis.txt', 'r' )
    for i in fitxer: 
       flowables.append (Paragraph( i , cos),)  
    
    doc.build(flowables)

#################################################################################
# Generem el PDF finalment
#################################################################################
generem_txt('pelis_brut.txt')
netegem_fitxer('pelis_brut.txt')
build_pdf('pelis.pdf')
