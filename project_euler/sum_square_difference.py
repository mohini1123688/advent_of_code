def sum_square_difference():
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(101):
        sum_of_squares += i**2
        square_of_sum += i

    square_of_sum = square_of_sum**2
    difference = square_of_sum - sum_of_squares

    print(difference)
    
def main():
    sum_square_difference()

if __name__ == '__main__':
    main()