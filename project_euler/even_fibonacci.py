def even_fibonacci():
    sum = 0

    number1 = 1
    number2 = 2
    while number2 < 4000000:
        if number2 % 2 == 0:
            sum += number2

        number3 = number1 + number2
        number1 = number2
        number2 = number3

    print(sum)

def main():
    even_fibonacci()

if __name__ == '__main__':
    main()