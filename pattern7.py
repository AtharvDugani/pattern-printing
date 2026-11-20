# No of rows
n = 5
# Outer loop for no of rows 
for i in range(1,n+1):
    # Following loop is to print spaces to center the pyramid
    for j in range(n-i):
        print(" ",end=" ")
    # below is the loop to print * 
    for k in range(2*i-1):
        print("*",end=" ")
    print()