# Practical no. 3
# Lab Asignments
# Task 1
print("Pattern 1")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print("\n")


print("Pattern 2")
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()
print("\n")


print("Pattern 3")
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
print("\n")

print("Pattern 4")
for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(1, end="")
        else:
            print(0, end="")
    print()
print("\n")

print("Pattern 5")
num = 2
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()
print("\n")

print("Pattern 6")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
