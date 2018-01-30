def fizzbuzz(x):
    hasło = ""
    if x % 3 == 0:
        hasło = "Fizz"
    if x % 5 == 0:
        hasło += "Buzz"
    print(x, hasło)


def main():
    for x in range(0, 100):
        fizzbuzz(x)


if __name__ == "__main__":
    main()
