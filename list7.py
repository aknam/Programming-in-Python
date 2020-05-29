#find the second max in the list
def SecondMaximum(lst):
    firstMax = float('-inf')
    secondMax = float('-inf')
    for item in lst:
        if item > firstMax:
            firstMax = item
    for item in lst:
        if item != firstMax and item > secondMax:
            secondMax = item
    return secondMax


print(SecondMaximum([9, 2, 3, 6]))