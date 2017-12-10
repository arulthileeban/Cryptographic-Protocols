def discrete_mod(a,b,p):
    return (a**b)%p
    
def discrete_mod_fast(a,b,p):
	if p==1:
		return 0
	c=1
	for i in range(1,b+1):
		c=(c*a)%p
	return c

if __name__=="__main__":
	print discrete_mod(7,5,4)
	print discrete_mod_fast(7,5,4)
