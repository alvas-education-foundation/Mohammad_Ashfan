def missingNumber(elements):
    max_element = max(elements)
    x =  max_element * (max_element + 1) // 2 - sum(elements)
    if x == 0 and  0 in elements:
        return max_element + 1
    elif x == 0 and 0 not in elements:
        return 0
    return x

elements = [] 
size = int(input('Enter the value of n \n'))
print('Enter the Elements')
for i in range(0, size):
    elements.append(int(input()))
result = missingNumber(elements)
print('The missing number is :',result)