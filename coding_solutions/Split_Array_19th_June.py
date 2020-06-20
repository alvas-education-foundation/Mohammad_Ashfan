# Python program to split array and move first part to end. 
  
def splitArr(a, n, k):  
   b = a[:k] 
   return (a[k::]+b[::]) 
          
arr = [10, 20, 30, 40, 50, 60] 
n = len(arr) 
position = 2
arr = splitArr(arr, n, position) 
for i in range(0, n):  
    print(arr[i], end = ' ') 