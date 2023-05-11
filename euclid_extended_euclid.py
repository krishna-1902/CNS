def print_euclid(q,r1,r2,r):
    i=0
    print("q\tr1\tr2\tr")
    while i < len(q):
        print(f"{q[i]}\t{r1[i]}\t{r2[i]}\t{r[i]}")
        i=i+1
    print(f"_\t{r1[i]}\t{r2[i]}\t_")
    print("===============================\n")

def euclid(m,n):
    q = []
    r1 = []
    r2 = []
    r = []

    r1.append(m)
    r2.append(n)
    i=0
    while r2[i]!=0:
        q.append(r1[i]//r2[i])
        r.append(r1[i]%r2[i])
        r1.append(r2[i])
        r2.append(r[i])
        i=i+1

    print_euclid(q,r1,r2,r)
    print(f"\nGCD of ({m},{n}) is {r1[i]}\n")
    return q,r1[i]

def print_extended(k1,k2,k,ch):
    print(f"{ch}1\t{ch}2\t{ch}")
    i=0
    while i < len(k):
        print(f"{k1[i]}\t{k2[i]}\t{k[i]}")
        i=i+1
    print(f"{k1[i]}\t{k2[i]}\t_")
    print("===============================\n")

def extended_euclid(q):
    s=[]
    s1=[]
    s2=[]
    s1.append(1)
    s2.append(0)
    i = 0
    while i < len(q):
        val=s1[i]-(q[i]*s2[i])
        s.append(val)
        s1.append(s2[i])
        s2.append(s[i])
        i=i+1
    s1.append(s2[i-1])
    s2.append(s[i-1])
    print_extended(s1,s2,s,'s')

    t=[]
    t1=[]
    t2=[]
    t1.append(0)
    t2.append(1)
    i = 0
    while i < len(q):
        val=t1[i]-(q[i]*t2[i])
        t.append(val)
        t1.append(t2[i])
        t2.append(t[i])
        i=i+1
    t1.append(t2[i-1])
    t2.append(t[i-1])
    print_extended(t1,t2,t,'t')
    return s1[i] , t1[i]

if __name__=="__main__":
    m=int(input("Enter first number : "))
    n=int(input("Enter second number : "))
    q,gcd = euclid(m,n)
    s,t = extended_euclid(q)
    print("\ns*m + t*n = gcd")
    print(f"{s}*{m} + {t}*{n} = {(s*m)+(t*n)}")