lst=[]
print("Type: ",type(lst))
names= ["John","Alice", "Bob"]
print("Names in the list: ",names)

mixed_list=[5,"Hello World",99.9, False]
print("Mixed List is also supported: ",mixed_list)

### Accessing list elements
fruits = ["Apple","banana","cherry","kiwi","gauva"]
print("Value in First index is : ",fruits[0])

### List Methods
fruits.append("Mango")
print("After append: ",fruits)

fruits.insert(5,"Jackfruit")
print("List after adding one more fruit(jaclfruit): ",fruits)

fruits.remove("Mango")
print("List after removing mango: ",fruits)

### Remove and return the last item
popped_fruits=fruits.pop()
print("Popped fruit: ",popped_fruits)
