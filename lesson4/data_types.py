# string data type

# literal assignment
first = 'rohit'
last = 'sharma'

print(type(first))
print(type(first) == str)
print(isinstance(first, str))


# constructor function
pizza = str('Pepperoni')

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation
fullname = first + ' ' + last
print(fullname)

fullname += '!'
print(fullname)

# casting a number to string

year = str(1997)
print(type(year))
print(year)


# multiple lines

multiline = """

Hey, How are you?

I was just checking in

                        All Good?

"""

print(multiline)