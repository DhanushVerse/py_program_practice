# Set is Unordered Unchangable and Unindexed and do not allow Duplicate keys
# True and 1 are considered both as duplicates in sets it take one
# False and 0 are considered as duplicates in sets
# We Cannot Change the item instead of we do add or remove items

name = {'Dhanush','Siva','Vengat'}
print(name)

# Set Methods:

# 1.add() -> We can add a specific item in set use add method.
name = {'Dhanush','Siva','Vengat'}
name.add('logu')
print(name)

# 2.update() -> we use update for add an another set or another list to a current set
color1 = {'black','blue','green'}
color2 = {'yellow','red','orange'}
color1.update(color2)
print(color1)
