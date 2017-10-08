
while True:
    print ('Enter your age:')
    age = str(input())
    if age.isdecimal():
        break
    print ('Please enter a number for your age')

while True:
    print ('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print ('Passworkds can only have letters and numbers.')
