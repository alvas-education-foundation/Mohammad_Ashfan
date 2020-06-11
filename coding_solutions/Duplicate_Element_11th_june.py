# Python program to remove duplicate elements from a list

n = int(input())
elements = []

for i in range(0, n):
    elements.append(int(input()))

result = list(sorted(set(elements)))

print(result)