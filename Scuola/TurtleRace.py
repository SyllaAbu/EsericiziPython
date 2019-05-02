#SYLLA ABU

import turtle as t
import random as r

grande = 400    #grandezza campo
n_turtles = 5
t.setup(grande, grande)
divisioniCampo = grande/(n_turtles+1)
l = []
cont = (0-(grande/2))
uscita = True
t.speed(1)  #setto velocita
for i in range(0, n_turtles-1):
    l.append(t.Turtle())                #aggiungo le turtle a un vettore
    l[i].penup()
    l[i].setx(0-(grande/2))             #setto la posizione di partenza delle turtle
    l[i].sety(cont + divisioniCampo)
    ran = r.randrange(0,7)
    if ran == 0:
        l[i].color("red")
    if ran == 1:
        l[i].color("yellow")
    if ran == 2:
        l[i].color("blue")
    if ran == 3:
        l[i].color("orange")
    if ran == 4:
        l[i].color("purple")
    if ran == 5:
        l[i].color("green")
    if ran == 6:
        l[i].color("black")

    cont = cont + divisioniCampo
l.append(t)
t.penup()
ran = r.randrange(0,7)

if ran == 0:
    t.color("red")
if ran == 1:
    t.color("yellow")
if ran == 2:
    t.color("blue")
if ran == 3:
    t.color("orange")
if ran == 4:
    t.color("purple")
if ran == 5:
    t.color("green")
if ran == 6:
    t.color("black")

t.setx(0-(grande/2))
t.sety(cont+divisioniCampo)
cont = cont + divisioniCampo

while uscita:
    for i in range(0, n_turtles):
        l[i].forward(r.randrange(0,16))
        if l[i].xcor() > (grande/2):
            uscita = False
            print("la turtle ")
            print(i+1)
            print("ha vinto!")
t.done()    #permette alle scritte di restare
