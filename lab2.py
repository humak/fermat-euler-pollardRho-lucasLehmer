#udl computational tools for problem solving lab2
#humakal
#'19
import math 
import random

#Trial division
def factorization(n):
    a = 2
    while(n%a != 0 and a <= math.sqrt(n)):
        a = a+1
    if (a > math.sqrt(n) ): 
        return n
    else :
        return a

#Fermat factorization
def fermat_factorization(n):
    a = math.ceil(math.sqrt(n))
    while (math.sqrt(a*a-n).is_integer()==False) :
            a = a+1
    return a - math.sqrt((a*a)-n)

#Euler factorization
def euler_factorization(n):
    a = 1
    while((math.sqrt(n- a*a)).is_integer() == False ) :
        a=a+1
        if((n- a*a)<0):   return(1)
    b = int(math.sqrt(n- a*a))
    c = a +1
    while((math.sqrt(n- c*c)).is_integer() == False ) :
        c=c+1
        if((n- c*c)<0):   return(1)
    d = int(math.sqrt(n- c*c))
    x = math.gcd(c-a, d-b)
    y = math.gcd(a+c, d+b)
    r = (c-a)/x
    s = (a+c)/y
    return ( (x/2)*(x/2) + ((y/2)*(y/2)) ), r*r + s*s
    
#Pollard Rho
def fx(x,n):
    c = random.randint(1, n-1)
    return ((x*x)%n+c)%n   
def gcd(m,n):
    if(n != 0):
        return gcd(n, m%n)
    return m
def pollard_rho(n):
    x = 2 
    y = 2
    d = 1
    while(d == 1):
        x = fx(x,n) 
        y = fx(y,n) 
        d = gcd(abs(x-y), n)
    if (d != n):
        return d

#Lucas- Lehmer test for Mersenne numbers
def lucas_lehmer(p):
    ll = [4]
    if (p>2):
        for i in range(1, (p-2)+1):
            n = ((ll[i-1])*(ll[i-1]) - 2) % ((2**p) - 1)
            ll.append(n)
    return ll
def ll_prime(p):
    if lucas_lehmer(p)[-1] == 0:
        return True
    return False


def main():
    print(factorization(1717))
    print(fermat_factorization(1717))
    print(euler_factorization(1717))
    print(pollard_rho(1717))
    print (ll_prime(1717))

if __name__== "__main__":
  main()


