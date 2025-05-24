def displayInventory(inventory):
    """Displays inventory in the expected format."""
    print("Inventory:")
    item_total = sum(inventory.values())  # Calculate total item count
    for item, count in inventory.items():
        print(f"{count} {item}")
    print(f"\nTotal number of items: {item_total}")

def addToInventory(inventory, addedItems):
    """Updates inventory with newly acquired items."""
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

# Sample inventory and dragon loot
inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Update inventory
inventory = addToInventory(inventory, dragonLoot)

# Display updated inventory
displayInventory(inventory)