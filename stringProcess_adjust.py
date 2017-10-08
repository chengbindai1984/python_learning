print ('Hello'.rjust(20))

print ('Hello World'.rjust(20))


print ('Hello'.ljust(20))

print ('Hello World'.ljust(20))

print ('Hello'.center(20))

print ('Hello World'.center(20))


print ('Hello'.rjust(20, '>'))

print ('Hello World'.rjust(20, '>'))


print ('Hello'.ljust(20, '<'))

print ('Hello World'.ljust(20, '<'))

print ('Hello'.center(20, '='))

print ('Hello World'.center(20, '='))


def printPicnic(itemsDict, leftWidth, rightWidth):
    print ("PICNIC ITEMS".center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print (k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 5, 'oranges': 900}

printPicnic(picnicItems, 10, 10)
printPicnic(picnicItems, 20, 6)
