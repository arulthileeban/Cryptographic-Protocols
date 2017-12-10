def discrete_mod(a,b,p):
    return (a**b)%p
    
def discrete_mod_fast(a,b,p):
	if p==1:
		return 0
	c=1
	for i in range(1,b+1):
		c=(c*a)%p
	return c

