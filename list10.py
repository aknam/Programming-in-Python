# rearrange sorted list in max then min then sexond max then second min and so on
def findMaxMin(lst):
	res=[]
	for i in range(len(lst)//2):
		res.append(lst[-(i+1)])
		res.append(lst[i])
	if len(lst) % 2:
		res.append(lst[len(lst)//2])
	return res
print(findMaxMin([1,2,3,4,5,6,7]))

