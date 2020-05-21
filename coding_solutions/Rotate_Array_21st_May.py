# Given an array, rotate the array to the right by k steps, where k is non-negative.

n = int(input('Enter the value for n'))
value = []
for i in range(0,n):
    value.append(int(input())) 
key = int(input())
if key == 0 or len(value) == 1:
    print('Invalid Inputs')
else
    for i in range(0,key):
        value.insert(0,value[-1])
        del value[-1]
    print(value)
