#Python3 program to print the Minimum String length. 

test_list = ['python', 'java', 'c++'] 
print("The original list : " + str(test_list)) 
res = min(len(ele) for ele in test_list) 
print("Length of minimum string is : " + str(res)) 
