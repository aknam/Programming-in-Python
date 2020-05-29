# finding the two number in the list with sum equals k.
def findsum(lst,k):
	lst.sort()
	ind1=0
	ind2=len(lst)-1
	res=[]
	while (ind1 != ind2):
		sum=lst[ind1]+lst[ind2]
		if sum < k:
			ind1+=1
		elif sum > k:
			ind2-=1
		else:
			res.append(lst[ind1])
			res.append(lst[ind2])
			return res
print(findsum([1,3,5,7,9],12)) 
