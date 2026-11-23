n = 6
# decreasing loop 
for i in range(n,0,-1):
    # for printing the spaces 
    for j in range(n-i):
        print(" ",end=" ")
    # for printing *
    for _ in range(2 * i -1):
        print("*",end=" ")
    print()