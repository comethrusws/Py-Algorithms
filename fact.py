# Calculate the factorial of a number using recursion.

#so since its jus factorial and i have beendoing it in sm other languages at basic lvl, imma jus use n*fact(n-1) fmla wit recursion

def factorial(n):
    if n == 0:
        return 1  # Base case here chai is: 0! = 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(f"Factorial of 5 is {result}")
