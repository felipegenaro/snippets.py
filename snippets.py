# Snippets

# Fizz Buzz
def Fizz_Buss(end_number):
        for n in range(0, end_number):
                if n % 5 == 0 and n % 3 == 0:
                        print("FizzBuzz")
                elif n % 3 == 0:
                        print("Fizz")
                elif n % 5 == 0:
                        print("Buzz")
                else:
                        print(n)

Fizz_Buss(101)


# Fibonacci Sequence
def Fibonacci_Sequence(fib_numbers):
        a, b = 0, 1
        for i in range(0, fib_numbers):
                print(a)
                a, b = b, a + b

Fibonacci_Sequence(11)


# differences between range and xrange
# xrange performes better with generators
# xrange is from python2, is faster and require less memory than the range statement
# xrange yields one result at the time
# range puts the inteire range of numbers into memory at once


# Fibonacci Generator
def Fibonacci(fib_nums):
        a, b = 0, 1
        for j in xrange(0, fib_nums):
                yield "{}: {}".format(j+1, a)   # yield = generator
                a, b = b, a + b

# loop through the generator
for item in Fibonacci(6):
        print(item)
