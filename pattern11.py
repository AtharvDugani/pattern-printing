n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):

        # Print stars on first row, first column and last column
        if i == 1 or j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()  # Move to the next row