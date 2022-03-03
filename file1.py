items = [1,2,3,4,5,6,]
new_items = list(map(lambda x:x*x,items))
print(new_items)

items = [1,2,3,4,5,6,]
new_items = list(filter(lambda x:(x%2==0),items))
print(new_items)

from functools import reduce
items = [1,2,3,4,5,6,]
new_items = reduce((lambda x,y:x+y),items)
print(new_items)






