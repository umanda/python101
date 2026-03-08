


# Number of rows for all patterns
row = 6


# Pattern 1: Left Triangle
print("Pattern 1: Left Triangle")
for i in range(row):
    for j in range(i + 1):
        print("*", end="")
    print()


# Pattern 2: Right Triangle
print("Pattern 2: Right Triangle")
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()


# Pattern 3: Reverse Triangle (Left-aligned Decreasing)
print("Pattern 3: Reverse Triangle")
for i in range(row):
    for j in range(row - i):
        print("*", end="")
    print()


# Pattern 4: Right Reverse Triangle (Right-aligned Decreasing)
print("Pattern 4: Right Reverse Triangle")
for i in range(row):
    for j in range(i):
        print(" ", end="")
    for j in range(row - i):
        print("*", end="")
    print()


# Pattern 5: Centered Pyramid
print("Pattern 5: Centered Pyramid")
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()


# Pattern 6: Inverted Pyramid
print("Pattern 6: Inverted Pyramid")
for i in range(row):
    for j in range(i):
        print(" ", end="")
    for j in range((row - i) * 2 - 1):
        print("*", end="")
    print()


# Pattern 7: Diamond
print("Pattern 7: Diamond")
# Top pyramid
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
# Bottom inverted pyramid (skip the middle row to avoid duplicate)
for i in range(1, row):
    for j in range(i):
        print(" ", end="")
    for j in range((row - i) * 2 - 1):
        print("*", end="")
    print()


# Pattern 8: Number Triangle
print("Pattern 8: Number Triangle")
for i in range(row):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()

# Pattern 9: Floyd's Triangle
print("Pattern 9: Floyd's Triangle")
num = 1
for i in range(row):
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()

# Pattern 10: Hollow Triangle (Centered)
print("Pattern 10: Hollow Triangle (Centered)")
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == row - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Pattern 11: Pascal's Triangle
print("Pattern 11: Pascal's Triangle")
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        val = factorial(i) // (factorial(j) * factorial(i - j))
        print(val, end=" ")
    print()

# Pattern 8: Hollow Triangle (Centered)
print("Pattern 8: Hollow Triangle (Centered)")
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == row - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Pattern 9: Pascal-style Pattern (Pascal's Triangle)
print("Pattern 9: Pascal's Triangle")
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        val = factorial(i) // (factorial(j) * factorial(i - j))
        print(val, end=" ")
    print()