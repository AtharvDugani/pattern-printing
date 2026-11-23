n = 6
for i in range(6):
    # first print the spaces
    for j in range(n-i):
        print(" ", end=" ")

    # now print the * 
    for _ in range(2*i-1):
        print("*", end=" ")
    print()
