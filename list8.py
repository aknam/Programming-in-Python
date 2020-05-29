# rotate the list from nth element
def rightRotateList(lst,n):
	n=n%len(lst)
	print(n)
	return lst[-n:]+lst[:-n]
print(rightRotateList([10,20,30,40,50],abs(4)))


