def factorial(n):
  # Base case: 0! and 1! are both 1 (stops the recursion)
  if n == 0 or n == 1:
    return 1

  # Recursive step: n! = n * (n-1)!
  return n * factorial(n - 1)


# Calculate and print the factorial for n = 5
result = factorial(5)