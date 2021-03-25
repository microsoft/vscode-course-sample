#iterative approach

numTerms = int(input("How many terms of Fibonacci sequence to print? "))

# main method

def fibonacci(n):
    if (n <= 1):
      return n
    else:
      x = 0
      y = 1
      for i in range(1, n):
        z = (x + y)
        x = y
        y = z
      return y

# check if the number of terms is valid
if numTerms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(numTerms):
        print(fibonacci(i))
