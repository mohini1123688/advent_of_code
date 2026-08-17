def factorial_digit_sum():
    sum = 0
    factorial = 1
    for i in range(1, 101):
        factorial *= i

    while factorial != 0:
        sum += factorial % 10
        factorial = factorial // 10 

    print(sum)
    
def main():
    factorial_digit_sum()

if __name__ == '__main__':
    main()