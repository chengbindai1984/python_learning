
# import collatz


# def collatz():
print ('Please input a number here')
number = int(input())

while True:

    if number == 1:
        print ('0')
        break

    elif number % 2 == 0:
        number = number // 2
        print (number)
    elif number % 2 == 1:
        number = 3 * number + 1
        print (number)
