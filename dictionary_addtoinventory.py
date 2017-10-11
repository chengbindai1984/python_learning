#coding=utf-8


def addToInventory(inventory, addedItems):

# 利用setdefault方法来添加新的Key:Value 至dict   
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1

    return inventory

    # 利用for 循环来 遍历dict 并处理key: value
def displayInventory(invenctory):

    item_total = 0

    print ("Invenctory")


    for k, v in invenctory.items():
        print (str(v) + ' ' + k)
        item_total = item_total + invenctory.get(k, 0)

    print ("Total nuber of items " + str(item_total))


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin',
              'gold coin', 'ruby', 'epic', 'steven dai', 'walking dead']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
