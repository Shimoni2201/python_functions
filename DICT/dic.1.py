x=['xylophone','dagger', 'bedroll','bread loaf']
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : x
}
print(inventory)
x.sort()
pock=['seashell','strange berry','lint']
inventory['pocket']=pock
print(inventory)
x.remove('dagger')
print(inventory)
inventory['gold']=50
print(inventory)