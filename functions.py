# Functions


# if you don't know how many args you'll recieve in your function, you can use *args
def some_funciton(*args):
        print(args)

some_funciton()
some_funciton('a', 'b', 'c')
some_funciton(1, 2, 3)
some_funciton('a', 'b', 'c', 1, 2, 3)


# if you dont know for sure the name of the argument
def some_another_function(**kwargs):
        some_arg = kwargs.get('some_arg')
        print(some_arg)

        some_another_arg = kwargs.get('some_another_arg')
        print(some_another_arg)

        # in case of call an argument name and didn't found it will display None
        not_found_arg = kwargs.get('not_found_arg')
        print(not_found_arg)

some_another_function(some_arg="hi")
some_another_function(some_another_arg="hello")
# with this the output will be an error
some_another_function('a')
some_another_function(1)


# try catch example
def error_function():
        try:
                10/'a'
        except TypeError:
                print("error", TypeError)
        except NameError:
                print("error", NameError)
        finally:
                print("print that regardless the result")
        
error_function()