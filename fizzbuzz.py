def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        hasło_fb = "FizzBuzz"
        print(x, hasło_fb)
    elif x % 3 == 0:
        hasło_f = "Fizz"
        print(x, hasło_f)
    elif x % 5 == 0:
        hasło_b = "Buzz"
        print(x, hasło_b)
    else:
        print(x)


for x in range(0, 100):
    fizzbuzz(x)

