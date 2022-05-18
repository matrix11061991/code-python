def renverse(mot):
	tom,res,l,mot = [],"",len(mot),list(mot)
	for i in range(1,l+1):
		tom.append(mot[l-i]) 
	res = res.join(tom)
	return res
renv = renverse("informatique")
print(renv)
