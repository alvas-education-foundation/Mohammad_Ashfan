# Python3 program to find compound interest for given values. 
  
def compound_interest(principle, rate, time): 
  
    CI = principle * (pow((1 + rate / 100), time)) 
    print("Compound interest is", CI) 

principle = int(input("Enter the priciple amount \n"))
rate = float(input("Enter the rate \n"))
time = int(input("Enter the year \n"))
compound_interest(principle, rate, time) 
  
  