def fizzbuzz(number):
    while number > 0:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz!")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
        number -= 1

# fizzbuzz(100)


def newFizz(num):
    for n in range(1, num):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz!")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

newFizz(25)