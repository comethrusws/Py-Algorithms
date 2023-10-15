#This algorithm generates a list of 
#prime numbers within a given range using the Sieve of Eratosthenes algorithm

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

if __name__ == "__main__":
    try:
        n = int(input("Enter the upper limit to find prime numbers up to: "))
        if n < 2:
            print("There are no prime numbers in the specified range.")
        else:
            prime_numbers = sieve_of_eratosthenes(n)
            print(f"Prime numbers up to {n} are: {prime_numbers}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")
