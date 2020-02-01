N = 9973
g = 1567
A_trovato = 6488

possibili_a = []
for a in range(1, N):
    if (g**a)%N == A_trovato:
        possibili_a.append(a)

print(possibili_a)
