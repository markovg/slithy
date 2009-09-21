


import reportlab
from reportlab.pdfgen import canvas
import reportlab.lib.pagesizes as pagesizes

pagesize = pagesizes.landscape(pagesizes.A4)
width,height = pagesize

c = canvas.Canvas("mypdf.pdf", pagesize=pagesize)

#c.drawImage(im,0,0,width,height)

import os
files = os.listdir('.')

for file in files:
    if 'slithy' and '.png' in file:

        c.drawImage(file,0,0,width,height)
        c.showPage()









c.save()

