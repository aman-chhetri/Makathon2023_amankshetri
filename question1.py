# First we will be Reading input values
n, m = map(int, input().split())  # using map two take two inputs on same line and split it with a space

# Calculating the minimum number of cuts needed
cuts_needed = n + m - 2

# Printing the output as cut needed
print(cuts_needed)



# Explanation:

# If we look at a single row, we can cut it into n-1 pieces with n-1 cuts. Similarly, we can cut a single column into m-1 pieces with m-1 cuts.

# So, to cut the entire paper into 1x1 squares, we need to make (n-1) cuts horizontally and (m-1) cuts vertically. Therefore, the total number of cuts needed is (n-1) + (m-1) = n + m - 2.

# Hence, the minimum number of cuts required is n + m - 2.

