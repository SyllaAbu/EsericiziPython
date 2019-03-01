import turtle
#import libreria
#import libreria as lib
#from libreria import l
fib1 = 1
fib2 = 1

k = 0
while k < cont:
    turtle.forward(fib2)
    turtle.right(90)
    k +=1
    fib2 = fib1 + fib2
    fib1 = fib2

turtle.done