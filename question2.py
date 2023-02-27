# We are creating a function to check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# We are creating unction to calculate number of valid bracelets of length n
def count_bracelets(n):
    arr = [[0, 0] for _ in range(n+1)]
    arr[1][0] = arr[1][1] = 1
    for i in range(2, n+1):
        if is_prime(i):
            arr[i][0] = arr[i-1][0] + arr[i-1][1]
            arr[i][1] = arr[i-1][1]
    return arr[n][0] + arr[n][1]

# main function
if __name__ == '__main__':
    t = int(input("Enter number of testcases: "))
    for i in range(t):
        n = int(input("\nEnter the number of beads in bracelet: "))
        print("Number of bracelets possible: ",count_bracelets(n))



# Explanation:

# We are creating a 2D array dp where arr[i][j] represents the number of valid bracelets of length i that end with j white beads. Here, j can be either 0 or 1, representing black and white beads respectively.

