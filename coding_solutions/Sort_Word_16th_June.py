# Program to sort the word in an alphabetical order

my_str = "Hello World"
words = my_str.split()
words.sort()
print("The sorted words are:")
for word in words:
   print(word)