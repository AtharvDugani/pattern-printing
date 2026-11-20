n = 5

# Upper half of butterfly
for i in range(1, n + 1):

    # Left stars
    for j in range(i):
        print("*", end=" ")

    # To Print Middle spaces
    for j in range(2 * (n - i)):
        print(" ", end=" ")

    # Right stars
    for j in range(i):
        print("*", end=" ")

    print()

# # Lower half of butterfly
for i in range(n, 0, -1):

    # Left stars
    for j in range(i):
        print("*", end=" ")

    # Middle spaces
    for j in range(2 * (n - i)):
        print(" ", end=" ")

    # Right stars
    for j in range(i):
        print("*", end=" ")

    print()