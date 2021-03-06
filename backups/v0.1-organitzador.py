#!/usr/bin/python
#

# Modulets
#
from os import listdir
from reportlab.platypus import ( BaseDocTemplate, PageTemplate, Frame, Paragraph)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm

# Generem un fitxer de text "fitxer.txt"
#
def generem_txt(filename):

    fitxer = open ( 'fitxer.txt', 'w' )
    contador = 0
    linia = 750

    # Llegim el directori de peli i muntem el "fitxer.txt" resultant
    #
    for peli in listdir("/mnt/disc1/joancatala/files/Pelis/"):
            fitxer.write(str(contador) + '         ' + peli + '\n')
            contador=contador+1
            linia=linia-20
    fitxer.close()


# Generem el fitxer de pdf "fitxer.pdf"
#
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
    fitxer = open ( 'fitxer.txt', 'r' )
    for i in fitxer: 
       flowables.append (Paragraph( i , cos),)  
    
    doc.build(flowables)

# Generem el TXT i el PDF finalment
#
generem_txt('fitxer.txt')
build_pdf('fitxer.pdf')
