def power_digit_sum():
    number = 2**1000 # multiplying 2 'n' times --> O(n)
    print(number)

    sum = 0

    while number != 0:
        print(number)
        sum += number % 10
        print(f'sum: {sum}')
        number = number // 10
        print(number)

    print(sum)

def main():
    power_digit_sum()

if __name__ == '__main__':
    main()