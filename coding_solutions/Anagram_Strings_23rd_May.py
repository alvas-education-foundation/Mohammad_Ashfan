# program to check wheather the given strings are Anagram

string1 = input('Enter the first string \n')
string2 = input('Enter the second string \n')

if sorted(string1) == sorted(string2):
    print('strings are Anagram')
else:
    print('strings are not Anagram')