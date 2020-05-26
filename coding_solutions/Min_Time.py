# Micro and Array update

testcase = int(input('Enter the number of testcase \n'))
while testcase != 0:
    elements = []
    differece = 0
    count = 0
    n = int(input('Enter the value for n \n'))
    key = int(input('Enter the key \n'))
    print('Enter the elements')
    for i in range(0, n):
        elements.append(int(input()))
    for i in range(len(elements)):
        if elements[i] < key:
            differece += (key - 1) - elements[i]
    print('The minimum amount of time is :',differece)
    testcase -= 1







