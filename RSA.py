import random
import timeit
import getpass
import string
values = dict()
P=0
Q=0
n=0
e=0
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index+1

def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def gen_pubkey():
	primes_list=primes(1000)
	P=random.choice(primes_list)
	Q=random.choice(primes_list)
	n=P*Q
	e=random.randint(2,n-1)
	return P,Q,n,e

def gen_prikey(P,Q,e):
	k=random.randint(1,1000)
	euler_fn=(P-1)*(Q-1)
	d=(k*euler_fn+1)/e
	return d

def get_pair():
    global P,Q,n,e
    (P,Q,n,e) = gen_pubkey()
    d = gen_prikey(P,Q,e)
    return d

def get_time():
    print(timeit.timeit("get_pair()","from __main__ import get_pair", number = 1))

def encode():
    global P,Q,n,e
    data=getpass.getpass()
    fin_pwd=""
    for letter in data:
        print int(values[letter])
        fin_pwd+=str((int(values[letter])**e)%n)
    print fin_pwd

encode()
