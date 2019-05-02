#SYLLA ABU

from turtle import *

passo = 50      #lunghezza ogni tratto
angolo = 90
t = Turtle()  # instanzio oggetto Turtle
print("Inserisci una stringa di comandi ('f','l','r',)")
comandi = input()   #metto gli input nella stringa
t.begin_poly()      # inizia a disegnare

for comando in comandi:  # while fino alla fine della stringa
    if (comando == "f"):
        t.forward(passo)
    elif comando == "r":
        t.right(90)
    elif comando == "l":
        t.left(90)
    else:
        t.back(passo)
t.end_fill()  # smette di disegnare
done()        # permette al disegno di restare
