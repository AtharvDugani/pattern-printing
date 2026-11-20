n = 5
# loop for rows
for i in range(n):
    # loop for column
    for j in range(n):
        # Print stars on the boundary of the square
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()