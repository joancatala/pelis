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
from reportlab.rl_config import defaultPageSize
from reportlab.pdfgen import canvas

#################################################################################
# Generem un fitxer de text "pelis_brut.txt"
#################################################################################
def generem_txt(filename):

    fitxer = open ( 'pelis_brut.txt', 'w' )
    contador = 1

    # Llegim el directori de peli i muntem el "pelis_brut.txt" resultant
    #
    for peli in sorted(os.listdir('/mnt/disc1/Pelis/')):        
            fitxer.write(str(contador) + " - " + peli + "\n")
            contador=contador+1
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
    filedata = filedata.replace('.AVI', ' ')
    filedata = filedata.replace('.mkv', ' ')
    filedata = filedata.replace('(Dual)', ' ')
    filedata = filedata.replace('(2010)', ' ')
    # Reemplacem merdes de Xvid, DivX, etc...
    filedata = filedata.replace('.HDrip', ' ')
    filedata = filedata.replace('(hdrip)', ' ')
    filedata = filedata.replace('[dvdrip]', ' ')
    filedata = filedata.replace('DVDRip', ' ')
    filedata = filedata.replace('[DVD-Rip]', ' ')
    filedata = filedata.replace('[DivX]', ' ')
    filedata = filedata.replace('[BRSCR]', ' ')
    filedata = filedata.replace('[ESP]', ' ')
    filedata = filedata.replace('(dvdrip)', ' ')
    filedata = filedata.replace('.Xvid', ' ')
    filedata = filedata.replace('Xvid', ' ')
    filedata = filedata.replace('(HDRip)', ' ')
    filedata = filedata.replace('HDRip', ' ')
    filedata = filedata.replace('[HDRIP]', ' ')
    filedata = filedata.replace('[HDRip]', ' ')
    filedata = filedata.replace('[XviD-Mp3]', ' ')
    filedata = filedata.replace('DivX-Mp3', ' ')
    filedata = filedata.replace('MP3', ' ')
    filedata = filedata.replace('XviD', ' ')
    filedata = filedata.replace('dvdrip', ' ')    
    filedata = filedata.replace('(Dual + subs)', ' ')
    filedata = filedata.replace('5.1', ' ')
    filedata = filedata.replace('AC3', ' ')
    filedata = filedata.replace('[HDrip-XviD-AC3]', ' ')
    filedata = filedata.replace('[DVDRIP]', ' ')
    filedata = filedata.replace('[BRrip X264 MKV]', ' ')
    filedata = filedata.replace('[HDrip-XviD- ]', ' ')
    filedata = filedata.replace('mp4', ' ')
    filedata = filedata.replace('mpg', ' ')
    filedata = filedata.replace('flv', ' ')
    filedata = filedata.replace('rar', ' ')
    filedata = filedata.replace('-EVO-spa', ' ')
    filedata = filedata.replace('BluRay', ' ')
    filedata = filedata.replace('720p', ' ')
    filedata = filedata.replace('HD1080p', ' ')
    filedata = filedata.replace('HD 1080p', ' ')
    filedata = filedata.replace('[dvdrip divx 5]', ' ')
    filedata = filedata.replace('[DVDrip]', ' ')
    filedata = filedata.replace('XviD -EVO', ' ')
    filedata = filedata.replace('HDTV', ' ')
    filedata = filedata.replace('DVDRIP', ' ')
    filedata = filedata.replace('DVDrip', ' ')    
    filedata = filedata.replace('[DVDRIP]', ' ')
    filedata = filedata.replace('[DVDrip-DivX]', ' ')
    filedata = filedata.replace('(DvDRiP XviD+Mp3]', ' ')
    filedata = filedata.replace('-spa', ' ')
    filedata = filedata.replace('[BRRip]', ' ')
    filedata = filedata.replace('(720x304)', ' ')
    filedata = filedata.replace('AAC', ' ')
    filedata = filedata.replace('.AAC', ' ')
    filedata = filedata.replace('x264', ' ')
    filedata = filedata.replace('X264', ' ')
    filedata = filedata.replace('1080p', ' ')
    filedata = filedata.replace('-dual', ' ')
    filedata = filedata.replace('BRSCR', ' ')
    filedata = filedata.replace('M1080', ' ')
    filedata = filedata.replace('divx', ' ')
    filedata = filedata.replace('DvDRip', ' ')
    filedata = filedata.replace('hdrip', ' ')            
    
    # Reemplacem merdes de webs
    filedata = filedata.replace('[www.newpct1.com]', ' ')
    filedata = filedata.replace('(DVDRip.Divx.Spanish)', ' ')
    filedata = filedata.replace('.www.lokotorrents.com', ' ')
    filedata = filedata.replace('www.lokotorrents.com', ' ')
    filedata = filedata.replace('.Www.LokoTorrents.Com', ' ')
    filedata = filedata.replace(',WwW.LoKoTorrents.CoM', ' ')
    filedata = filedata.replace('[www.tumejortv.com]', ' ')
    filedata = filedata.replace('.by.jurimu', ' ')
    filedata = filedata.replace('M1080.www.newpct1.com', ' ')
    filedata = filedata.replace('(EliteTorrent.net)', ' ')
    filedata = filedata.replace('[www.zonatorrent.com]', ' ')
    filedata = filedata.replace('www.DivxTotaL.com]', ' ')
    filedata = filedata.replace('enlace 5BDVDScr5D', ' ')
    filedata = filedata.replace('jfcm92', ' ')
    filedata = filedata.replace('www.DESCARGASMIX.com', ' ')
    filedata = filedata.replace('[WwW.RiojaTorrent.CoM]', ' ')
    filedata = filedata.replace('[www divxatope com]', ' ')
    filedata = filedata.replace('(www.elitetorrent2.net)', ' ')
    filedata = filedata.replace('(Elitetorrent net)', ' ')
    filedata = filedata.replace('(Elitetorrent.net)', ' ')
    # Reemplacem idioma
    filedata = filedata.replace('Animacion.Spanish', ' ')
    filedata = filedata.replace('[spanish dvdRip]', ' ')
    filedata = filedata.replace('[Spanish]', ' ')
    filedata = filedata.replace('Spanish', ' ')
    filedata = filedata.replace('[spanish]', ' ')
    filedata = filedata.replace('[  Spanish]', ' ')
    filedata = filedata.replace('[AC3 Spanish]', ' ')
    filedata = filedata.replace('[Castellano]', ' ')
    filedata = filedata.replace('Castellano900', ' ')
    filedata = filedata.replace('(spanish)', ' ')
    filedata = filedata.replace('(Spanish)', ' ')
    filedata = filedata.replace('( .Spanish)', ' ')
    filedata = filedata.replace('[SPANISH]', ' ')
    filedata = filedata.replace('( .Divx.Spanish)', ' ')
    filedata = filedata.replace('[spanish]', ' ')
    filedata = filedata.replace('spanish]', ' ')
    filedata = filedata.replace('Spanish )', ' ')
    filedata = filedata.replace('[Castellano ]', ' ')
    filedata = filedata.replace('Vose', ' ')
    filedata = filedata.replace('VOSE', ' ')
    filedata = filedata.replace('ESP', ' ')
    
    # Reemplacem simbols rars
    filedata = filedata.replace('.', ' ')
    filedata = filedata.replace('_', ' ')
    filedata = filedata.replace('( )', ' ')
    filedata = filedata.replace('(1)', ' ')
    filedata = filedata.replace('[ ]', ' ')
    filedata = filedata.replace('{}', ' ')

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

    cos = ParagraphStyle('personalitzat', fontSize=8, leading=9, spaceBefore=1)
    
    doc.addPageTemplates(
        [
            PageTemplate(
                frames=[
                    Frame(
                        doc.leftMargin - 60,
                        doc.bottomMargin,
                        doc.width / 3 + 40,
                        doc.height,
                        id='ThreeCol',
                        rightPadding=column_gap / 8,
                        showBoundary=0  # set to 1 for debugging
                    ),
                    Frame(
                        doc.leftMargin + doc.width / 3 - 20,
                        doc.bottomMargin,
                        doc.width / 3 + 40,
                        doc.height,
                        id='ThreeCol',
                        leftPadding=column_gap / 8,
                        showBoundary=0
                    ),
                    Frame(
                        doc.leftMargin + doc.width / 3 + 171,
                        doc.bottomMargin,
                        doc.width / 3 + 40,
                        doc.height,
                        id='ThreeCol',
                        leftPadding=column_gap / 8,
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
