def multiples():
    sum = 0
    for number in range(1000):
        if number % 3==0 or number % 5==0:
            sum = sum + number
    print(sum)
def main():
    multiples()

if __name__ == '__main__':
    main()