def getCount(inputStr):
    num_vowels = 0
    # your code here
    newList = list(inputStr)
    vowelsList = ['a','e','i','o','u']

    for vowel in vowelsList:
        num_vowels= newList.count(vowel)+num_vowels
    return num_vowels