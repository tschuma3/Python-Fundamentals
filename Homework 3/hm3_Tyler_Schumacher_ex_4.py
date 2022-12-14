'''
Homework 3, Exercise 2
Tyler Schumacher
September 9, 2019
Create and output an inventory
'''

inventory = {'Rope': 1, 'Torch': 1, 'Gold Coin': 42, 'Dagger': 1, 'Arrow': 12}
loot = ['Gold Coin', 'Dagger', 'Gold Coin', 'Torch', 'Arrow']  

#Displays the inventory
def displayInventory(inventory):
  print("Inventory:")
  itemTotal = 0
  for j, c in inventory.items():
    itemTotal += c
    print(str(c) + ' ' + str(j))
  print("Total number of items: " + str(itemTotal))

#Adds to the inventory
def addToInventory(inventory, addItems):
  for j in range(len(addItems)):
    inventory.setdefault(addItems[j], 0)
    inventory[addItems[j]] += 1
  return inventory

updatedInventory = addToInventory(inventory, loot)
displayInventory(updatedInventory)
print("Inventory updated.")