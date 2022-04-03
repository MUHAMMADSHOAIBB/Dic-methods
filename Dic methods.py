bike = {
  "Name": "Honda",
  "model": "Old",
  "year": 1999
}
# clear method
# Rempoves all the elements from the bike list
# bike.clear()
# print(bike)
# copy method
#returns the copy of bike
# print(bike.copy())
#fromkeys method
#Returns a dictionary with the specified keys and value
# x = ('key1', 'key2', 'key3')
# y = 4,5,6
# keyss = dict.fromkeys(x, y)
# print(keyss)
#get method
#The get() method returns the value of the item with the specified key.
print(bike.get('Model'))
#items method
#Returns the value of the specified key
x= bike.items()
print(x)
#Keys method
# returns a line containing the dic. keys
print(bike.keys())
#pop method
#removes the element from specifies key
print(bike.pop("model"))
#pop item
#removes the last inserted key value pair
print(bike.popitem())
#update method
#update the dic.with specifies key value pairs
bike.update({"gear":"four"})
print(bike)
#values
#returns a lsit of all values in dic.
print(bike.values())

