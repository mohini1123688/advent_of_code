import math 

def special_pythagorean_triplet():
    # a + b + c = 1000
    # a^2 + b^2 = c^2
    # a + b + sqroot(a^2 + b^2) = 1000

    a_result = 0
    b_result = 0
    for a in range(1001):
        for b in range(1001):
            if a<b:
                if a + b + math.sqrt(a**2 + b**2) == 1000:
                    a_result = a
                    b_result = b
                    c_result = math.sqrt(a_result**2 + b_result**2)
                    break

    print(f'a: {a_result}')
    print(f'b: {b_result}')
    print(f'c: {c_result}')
    print(f'abc: {a_result*b_result*c_result}')

def main():
    special_pythagorean_triplet()

if __name__ == '__main__':
    main()