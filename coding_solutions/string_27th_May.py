#Program to Replace Lowercase Characters by Uppercase & Vice-Versa.

a=input()
for i in a:
    if i.islower():
         print(i.upper(),end="")
    else:
        print(i.lower(),end="")

        