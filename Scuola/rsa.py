def mcd(a, b):
    """Restituisce il Minimo Comune Multiplo tra a e b"""
    while b:
        a, b = b, a%b
    return a

def mcm(a, b):
    return a // mcd(a, b) * b

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

p = int(input("Inserisci p: "))
q = int(input("Inserisci q: "))
a = int(input("Inserisci il numero da cifrare: "))

if is_prime(p) and is_prime(q) and p != q:
    n=p*q
    print("n: " + str(n))
    m = mcm(p-1, q-1)
    print("m: " + str(m))

    c = range(1, m)
    list_c = []
    for c_attemp in c:
        if 1 == mcd(c_attemp, m):
            list_c.append(c_attemp)

    c = int(list_c[-1])
    print(list_c)
    print("c: " + str(c))

    d = range(1, m)
    list_d = []
    for d_attemp in d:
        if 1 == (c*d_attemp)%m:
            list_d.append(d_attemp)
    d = int(list_d[-1])

    print("d: " + str(d))

    b = pow(a,c) % n
    a_again = pow(b, d) % n
    print(f"Chiavi private: {n, p}\nChiavi pubbliche: {m,d}\n\n")

    print("il numero a e' stato cifrato da " + str(a) + " a " + str(b))
    print("il numero b decifrato e' " + str(a_again))


else:
    print("I numeri inseriti non sono entrambi primi o sono uguali")
