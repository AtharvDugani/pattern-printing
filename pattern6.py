n = 5
for i in range(1, n+1):
    # print the spaces before stars
    for j in range(n-i):
        print(" ",end=" ")
    # to print the stars 
    for k in range(i):
        print("*",end=" ")
    print()