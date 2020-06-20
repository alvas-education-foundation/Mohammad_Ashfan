# Python program to concatenate two numbers 
  
def numConcat(num1, num2): 
     digits = len(str(num2)) 
     num1 = num1 * (10**digits) 
     num1 += num2 
     return num1 
  
a = 100
b = 20
print(numConcat(a, b)) 