#rearrange positive and negative elements in the list
def reArrange(lst):

	return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

print(reArrange([10,-1,20,4,5,-9,-6]))