    
def displayInventory(invenctory):

    item_total = 0

    print ("Invenctory")

    for k, v in invenctory.items():
        print (str(v) + ' ' + k)
        item_total = item_total + invenctory.get(k, 0)
        print (item_total)

    print ("Total nuber of items " + str(item_total))


stuff = {'rple': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(stuff)
