# looks at numbers 1 - 100
for i in range(1, 101):
    # checks if number is both divisible by 3 and 5 then returns FizzBuzz if so
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    # checks if number is divisible by 3 only then returns Fizz if so
    elif i % 3 == 0:
        print("Fizz")
    # checks if number is divisible by 5 only then returns Fizz if so
    elif i % 5 == 0:
        print("Buzz")
    # if none then returns the number 
    else:
        print(i)