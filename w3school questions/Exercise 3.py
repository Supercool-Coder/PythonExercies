# Write a Python program to display the current date and time ?
import datetime

present = datetime.datetime.now()
print("This is a current date and time :-")
print(present.strftime("%Y-%m-%d %H:%M:%S")) # Y - year , m - month , d - date , H -hours , M- minutes ,
# S-second

# What does the "yield" keyword do?
# yield is a keyword that is used like return, except the function will return a generator.
# To master yield, you must understand that when you call the function, the code you have written in the
# function body does not run. The function only returns the generator object, this is a bit tricky :-)

# Example :-
# def createGenerator():
#     list = [3]
#     for i in list:
#         yield i*i
#
# mygenerator = createGenerator()
# for i in mygenerator:
#     print(i)
# Output :- 3 x 3 = 9


# To understand what yield does, you must understand what generators are. And before you can understand
# generators, you must understand iterables.

# Generators :- Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store
# all the values in memory, they generate the values on the fly:
# >>> mygenerator = (x*x for x in range(3))
# >>> for i in mygenerator:
# ...    print(i)
# It is just the same except you used () instead of []. BUT, you cannot perform for i in mygenerator a
# second time since generators can only be used once: they calculate 0, then forget about it and calculate
# 1, and end calculating 4, one by one.



# Iterables -:-
# When you create a list, you can read its items one by one. Reading its items
# one by one is called iteration.
# Example -:-
# >>> mylist = [1, 2, 3]
# >>> for i in mylist:
# ...    print(i)
# Output -:-
# 1
# 2
# 3
# >>> mylist = [x*x for x in range(3)]
# >>> for i in mylist:
# >>> print(i)
# output :-
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# Everything you can use "for... in..." on is an iterable; lists, strings, files...

# These iterables are handy because you can read them as much as you wish, but you store all the
# values in memory and this is not always what you want when you have a lot of values.