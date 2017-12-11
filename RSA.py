import random
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
	return n,e

gen_pubkey()
