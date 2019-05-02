#SILLA ABU

#trovo i nodi confinanti in un grafo
m=[[0,1,0,1,0],
   [1,0,1,1,1],
   [0,1,0,1,0],
   [1,1,1,0,0],
   [0,1,0,0,0]]

node = -1

for j in m: 
    cnt=0
    nodo +=1
    vicini = [] 
    for k in j:
        if(k==1):
            vicini.append(cnt)
        cnt +=1

    print("nodo:" + str(nodo) + " = "  + str(vicini))
