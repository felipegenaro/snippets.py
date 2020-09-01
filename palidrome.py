# """"
# Check for Palidrome
#
# Given a string, determine if there is a way to arrange the string
# such that the string is a palidrome. If such arrangement exists,
# return a palidrome (there coudl be many arrangements).
# Otherwise return None.
#
# """"

from collections import defaultdict

def Find_Palidrome(s):
        char_count = defaultdict(int)

        for c in s:
                char_count[c] += 1

        odd_char = ""
        palidrome = ""

        for c, cnt in char_count.items():
                if cnt % 2 == 0:
                        palidrome += c * (cnt // 2)
                elif not odd_char:
                        odd_char = c
                        palidrome += c * (cnt // 2)
                else:
                        return None

        return palidrome[::-1] + odd_char + palidrome

print(Find_Palidrome("test"))
print(Find_Palidrome("civic"))
print(Find_Palidrome("level"))
print(Find_Palidrome("not"))
print(Find_Palidrome("madam"))
print(Find_Palidrome("noon"))
print(Find_Palidrome("palidrome"))
print(Find_Palidrome("radar"))

# ---

from pythonds.basic import Deque

def Palidrome_Checker(some_string):
        char_deque = Deque()

        for char in some_string:
                char_deque.addRead(char)

        still_equal = True

        while char_deque.size() > 1 and still_equal:
                first = char_deque.removeFront()
                last = char_deque.removeRear()

                if first != last:
                        still_equal = False

        return still_equal

print(Palidrome_Checker("test"))
print(Palidrome_Checker("civic"))
print(Palidrome_Checker("level"))
print(Palidrome_Checker("not"))
print(Palidrome_Checker("madam"))
print(Palidrome_Checker("noon"))
print(Palidrome_Checker("palidrome"))
print(Palidrome_Checker("radar"))