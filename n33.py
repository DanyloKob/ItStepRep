inventory = ['sword', 'shield', 'poision', 'key', 'map']
print(inventory[0])
print(inventory)

inventory[inventory.index('key')] = 'golden key'
print(inventory)

inventory.remove('shield')
print(inventory)

frieand_inv = ['Sno', 'arrows']
for i in range(len(frieand_inv)):
    inventory.append(frieand_inv[i])
print(inventory)