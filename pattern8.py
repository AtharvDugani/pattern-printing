# No of rows
n = 5
# Outer loop starts from 5 and decreases to 1 
for i in range(n,0,-1):
    for j in range(n - i):
        # to print spaces before *
        print(" ",end=" ")

    #to print decreaseing no of stars* 
    for _ in range(2*i-1):
        print("*",end=" ")
    print()