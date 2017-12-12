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
	return P,Q,n,e

def gen_prikey(P,Q,e):
	k=random.randint(1,1000)
	euler_fn=(P-1)*(Q-1)
	d=(k*euler_fn+1)/e
	return d

(P,Q,n,e) = gen_pubkey()
d = gen_prikey(P,Q,e)
