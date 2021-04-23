def factorial(n):
   if n == 1:
      return n
    else:
      return n * factorial(n-1)


def factorial_2(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num