#!/usr/bin/python

# Modulets
from os import listdir
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    BaseDocTemplate,
    PageTemplate,
    Frame,
    Paragraph
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm

def build_pdf(filename):
    doc = BaseDocTemplate(filename)
    column_gap = 1 * cm

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
       flowables.append (Paragraph( i , ParagraphStyle('default')),)  
    
    doc.build(flowables)

build_pdf('col.pdf')
