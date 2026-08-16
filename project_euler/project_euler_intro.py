# Problem 0 
sum = 0
for number in range(960001):
    if number**2 % 2 != 0:
        print(number)
        sum = sum + number**2
print(sum)