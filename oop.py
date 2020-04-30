# OOP


# class class_name(inherits_from)
class Person(object):
        # remember to add the init funcition, self and the arguments/atributes
        def __init__(self, name):
                # initialize all those parameters
                # self is like 'this' refer of himself
                self.name = name
        # method
        def reveal_identity(self):
                print("My name is {}").format(self, name)

class Super_Hero(Person):
        # initialize of an base class
        def __init__(self, name, hero_name):
                super(Super_Hero, self).__init__(name)
                self.hero_name = hero_name

        # overwrite method
        def reveal_identity(self):
                super(Super_Hero, self).reveal_identity()
                print("...And I am {}").format(self.hero_name)

# instances of a class
felipe = Person('Felipe')
felipe.reveal_identity()

bruce = Super_Hero('Bruce Wayne', 'Batman')
bruce.reveal_identity()


# -----------------------------------------------------------------


# implicit inherit
class Cake:
        # default atribute
        cake_format = "square"

        def __init__(self, flavor, eggs, stories):
                self.flavor = flavor
                self.eggs = eggs
                self.stories = stories

        def _cook(self):
                print("bake")

        def _serve(self):
                print("done")

# instances of a class
chocolate_cake = Cake('chocolate', 4, 1)
print(chocolate_cake.flavor, chocolate_cake.cake_format)
chocolate_cake._cook()
chocolate_cake._serve()

strawberry_cake = Cake('strawberry', 12, 3)
print(strawberry_cake.flavor, strawberry_cake.cake_format)
strawberry_cake._cook()
strawberry_cake._serve()


# -----------------------------------------------------------------


# more inherit example
class Animal(object):
        paws = 4

        def __init__(self, name, owner):
                self.name = name
                self.owner = owner

        def _eat(self):
                print('nhom nhom...')

class Cat(Animal):
        def __init__(self, breed, name, owner):
                super(Cat, self).__init__(name, owner)
                self.breed = breed

        def _meow(self):
                print('meow')

class Dog(Animal):
        def _bark(self):
                print('BARK')
        
        def another_function(self):
                pass

# suppose you are designing a new class with some methods that you don't want to implement, yet
# use pass to act as a placeholder
# means if you call the function another_function(), do absolutely nothing

some_cat = Cat('Persian', 'Dory', 'Felipe')
some_cat._eat()
some_cat._meow()

some_dog = Dog('Zed', 'Felipe')
some_dog._eat()
some_dog._bark()

print('the cat has {} paws as well as the dog that also have {} paws'.format(some_cat.paws, some_dog.paws))
