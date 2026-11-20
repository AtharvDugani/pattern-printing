# No of rows
n = 5
# upper half of the diamond 
for i in range(1,n+1):
    # Following loop is to print spaces to center the pyramid
    for j in range(n-i):
        print(" ",end=" ")
    # below is the loop to print * 
    for k in range(2*i-1):
        print("*",end=" ")
    print()
# Lower half of the diamond
for i in range(n,0,-1):
    for j in range(n - i):
        # to print spaces before *
        print(" ",end=" ")

    #to print decreaseing no of stars* 
    for _ in range(2*i-1):
        print("*",end=" ")
    print()