#: The function to reverse a word
def renverse(mot):
	"""Reverse the given word.

    :param string text: word to reverse.

    :returns: the reversed word .
    :rtype: string
    """
	tom,res,l,mot = [],"",len(mot),list(mot)
	for i in range(1,l+1):
		tom.append(mot[l-i]) 
	res = res.join(tom)
	return res
\
def renverso(mot):
	return mot[::-1]

def reversejrs(mot):
	car,rev = '',[]
	[rev.append(mot[-1-i]) for i in range(0,len(mot))]
	return car.join(rev)

renv = renverse("informatique")
print(renv)
