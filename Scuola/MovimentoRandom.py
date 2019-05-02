#SYLLA ABU

from turtle import *
import random

t=Turtle()  #instanzio oggetto Turtle
print("Quante volte vuoi svoltare?")
i=int(input())
t.begin_poly()  #inizia a disegnare
cnt=0

while(cnt<i):       #calcolare la il numero di svolte
    t.forward(10)   #disegna
    if(random.random()<0.5):
        t.left(90)        #gira a sinistra
        t.color("green")  #cambia colore in base alla direzione
    else:
        t.right(90)         #gira a destra
        t.color("yellow")   #cambia colore in base alla direzione
    cnt+=1

t.end_fill()    #smette di disegnare
done()          #permette al disegno di restare
