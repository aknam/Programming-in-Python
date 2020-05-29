# finding min number in the list
def findmin(lst):
	if (len(lst) <= 0):
		return none
	min=lst[0]
	for i in lst:
		if i<min:
			min=i
	return min
print(findmin([9,2,3,6]))