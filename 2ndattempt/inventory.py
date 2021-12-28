from typing import ItemsView


stuff = {'rope': 1, 'sword': 1, 'shield:':1, 'potion': 2, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    item_total = 0
    print("Inventory: ")
    for item, quantity in inventory.items():
        print(item +  ': ' + str(quantity))
        item_total += quantity

    print('Total number of items: ' + str(item_total))

        


# displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', ' ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] 