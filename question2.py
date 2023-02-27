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
    x = [[0, 0] for _ in range(n+1)]
    x[1][0] = x[1][1] = 1
    for i in range(2, n+1):
        if is_prime(i):
            x[i][0] = x[i-1][0] + x[i-1][1]
            x[i][1] = x[i-1][1]
    return x[n][0] + x[n][1]

# main function
if __name__ == '__main__':
    t = int(input("Enter number of testcases: "))
    for i in range(t):
        n = int(input("\nEnter the number of beads in bracelet: "))
        print("Number of bracelets possible: ",count_bracelets(n))
