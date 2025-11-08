import numpy as np

print("Quiz 1:")
print("Questions #1")
list_numbers = np.array([1,2,3,4,5,6,7,8,9,10])
print(list_numbers)
a = list_numbers*3
print(a)
b = np.sum(a)
print(b)
print()

print("Questions #2")
a = np.arange(10,21)
b = a*2
c = b+10
d = np.sum(c)
print(a)
print(b)
print(c)
print(d)
print()

print("Questions #3")
list_numbers = np.array([2,3])
sum = 0
for i in list_numbers:
    sum += 5*i
print(sum)
print()

print("Questions #4")
sum = 0
list_numbers = np.array([1,2,3])
for i in list_numbers:
    sum +=(4*i*i+2*i+6)*(4*i*i+2*i+6)
print(sum)
