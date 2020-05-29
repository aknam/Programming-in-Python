#Remove even elements from the list using list comprehension
def removeEven(list):
	return [number for number in list if number%2 != 0]
print(removeEven([1,2,3,4,5,6,7]))

# 0(n)