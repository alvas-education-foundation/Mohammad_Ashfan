# Python program to find the largest number among the three input numbers

num1 = 10
num2 = 20
num3 = 40

if (num1 >= num2) and (num1 >= num3):
   largest = num1
   print("The largest number is :",largest)
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
   print("The largest number is :",largest)
else:
   largest = num3
   print("The largest number is :",largest)
