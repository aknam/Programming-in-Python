#find non repeatative integer in the list
def findUnique(lst):
	for ind1 in range(len(lst)):
		ind2=0
		while(ind2<len(lst)):
			if(ind1!=ind2 and lst[ind1]==lst[ind2]):
				break
			ind2+=1
		if ind2==len(lst):
			return lst[ind1]
	
print(findUnique([9,2,3,2,6,6]))