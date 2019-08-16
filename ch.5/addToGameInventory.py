stuff = {'rope':1, 'torch':6, 'gold coin': 42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    """prints the inventory and prints the total of all the items"""
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    """taking a dict and a list and adding the list to the dict"""
    item_total = 0
    for things in addedItems:
        inventory.setdefault(things, 0)
        inventory[things] = inventory[things] + 1
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
