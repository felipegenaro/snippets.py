# Data Structures

# array -> data sequence
# pointer -> dynamic memory allocation
# list -> set of chained elements
# queue -> First In First Out
# pile -> Last In First Out
# tree -> non-linear structure

# List - simple array
my_list = [10, 'hi', 5, 'hello']
for j in my_list:
        print(j)


# Tuple - immutable/unchangeable list
my_tup = (1, 2, 'hi', 5, 4, 'hello')
for k in my_tup:
        print(k)


# Dictionary - is an hash table
my_dict = { 'name': 'Felipe', 'age': '22', 'occupation': 'Software Engineer' }
# iteritems() gives us one result back at the time (like xrange) and item() puts all of the items into memory (like range)
for key, val in my_dict.iteritems(): 
        print("My {} is {}".format(key, val))


# Set - list without repeated values, even with you have repeated values, only the different ones will be shown
my_set = { 10, 20, 30, 40, 50, 10, 20, 30, 50 }
for l in my_set:
        print(l)


# Comprehensions - short hands
another_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# The squared of each number without usign statements or loops
squares = [num * num for num in another_list]
print(squares)

# tree
# binary tree class
class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

        def __str__(self):
                return str(self.__class__) + ": " + str(self.__dict__)

# instance of the binary tree
root = Node(12, 6, 4)

print(root)