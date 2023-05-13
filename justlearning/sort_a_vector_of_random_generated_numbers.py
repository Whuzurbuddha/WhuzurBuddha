import random

print("Enter range of numbers: ")
r = int(input())
print("How many numbers would you like to generate?")
n = int(input())
vec = []
for i in range(0, n):
    vec.append(random.randrange(0, r))

for j in range(1, vec.__len__()):
    for k in range(0, vec.__len__()):
        if vec[j] < vec[k]:
            vec.sort()
counter = 0
for i in vec:
    print(i, end=" ")
    counter += 1
    if counter == 25:
        print("\n", end="")
        counter = 0
        
