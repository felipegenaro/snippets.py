# Fizz Buzz
def Fizz_Buzz(end_number):
        for i in range(0, end_number):
                if i % 5 == 0 and i % 3 == 0:
                        print("FizzBuzz")
                elif i % 3 == 0:
                        print("Fizz")
                elif i % 5 == 0:
                        print("Buzz")
                else:
                        print(i)

def Improved_Fizz_Buzz(end_number):
        for j in range(0, end_number):
                output = ''
                if j % 3 == 0:
                        output += 'Fizz'
                if j % 5 == 0:
                        output += 'Buzz'

                print(output or j)

def Minified_Fizz_Buzz(end_number):
        for k in range(0, end_number):
                output = 'Fizz' if k % 3 == 0 else ''
                output += 'Buzz' if k % 5 == 0 else ''

        print(k) if output == '' else print(output)

Fizz_Buzz(101)
Improved_Fizz_Buzz(101)
Minified_Fizz_Buzz(101)