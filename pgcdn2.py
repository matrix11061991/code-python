#: The  function that calculates pgcd of 2 numbers:
def pgcd(a,b):
	while b != 0 :
		a,b = b,a % b
	return a

def pgcdn(*n):
	p =  pgcd(n[0], n[1])
	m =  len(n)
	for x in n[2:]:
		p = pgcd(p,x)
	return m,p






