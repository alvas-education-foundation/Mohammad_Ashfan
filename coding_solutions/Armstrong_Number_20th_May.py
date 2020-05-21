#Python program to check wheather the given number is an Amtrong number. 

import math
number = int(input('Enter a number \n'))
temp = number
elements = []
count = 0
total_sum = 0
while number != 0:
    rem = number % 10
    number = number // 10
    count += 1
    elements.append(rem)
for i in range(0, count):
    total_sum += int(math.pow(elements[i], count))
if total_sum == temp:
    print('Amstrong number')
else:
    print('not an Amstrong number')
    

