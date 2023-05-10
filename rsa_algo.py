import math

def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return result


def rsa():
    p = int(input("First prime number : "))
    q = int(input("Second prime number : "))
    n = p*q
    print("Value of n :",n)
    phi = (p-1) * (q-1)
    print("Value of toint :",phi)
    e = int(input(f"Enter value of e 1<e<{phi} and e is coprime to {phi} : "))
    while (math.gcd(e,phi)!=1):
        print("Not a valid number!")
        e = int(input(f"Enter value of e 1<e<{phi} and e is coprime to {phi} : "))

    # d is multiplicative inverse of e
    i = 1
    while True:
        if ((phi*i)+1)%e==0:
            d = ((phi*i)+1)/e
            break
        i = i+1

    print("value of d is :",d)

    print("=============================")
    print("Encryption process\n")
    plain=int(input("Enter a plain text number : "))
    cipher= mod_exp(plain,e,n)
    print("\nPlain text :",plain)
    print("Cipher text",cipher)

    print("\n=============================")
    print("Decryption process\n")
    print("Cipher text",cipher)
    plain1=mod_exp(cipher,d,n)
    print("Plain text :",plain1)

if __name__=="__main__":
    rsa()