

# --------------------
# Strings Methods
# ----------------------------

# index(SubString, Start, End)
a = "I Love Python"
print(a.index("P", 0, 10))

print(a.index("P", 0, 5))


# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P", 0, 10))

print(b.find("P", 0, 5))


# rjust(Width, Fillchar) 

s = "salar"
print(s.rjust(10))
print(s.rjust(10 , "#"))

# ljust(Width, Fillchar)

s = "salar"
print(s.ljust(10))
print(s.ljust(10 , "#"))


# Splitlines()
e = ''' First Line
Second Line
Third Line'''
print(e.splitlines())

# istitle()
one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

# isspace()
three = " "
four = ""
print(three.isspace())
print(four.isspace())

# islower()
five = "i love python"
six = "I Love Python"

print(five.islower())
print(six.islower())

# isidentifier()

seven = "salarissa"
eight = "Salar-issa"
nine = "salarissa1995"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())


# isalpha()
x = "AaaaaaBbbbbbbb"
y = "AaaaaaBbbbbbbb4739539"
print(x.isalpha())
print(y.isalpha())

# isalnum()

t = "AaaaaaBbbbbbbb"
g = "AaaaaaBbbbbbbb4739539"
print(t.isalnum())
print(g.isalnum())


# replace(Old Value, New Value , Count)

a = "Hello One Two Three One One"
print(a.replace("One", "1", ))
print(a.replace("One", "1", 1 ))
print(a.replace("One", "1", 2 ))


# Join(Iterable)

mylist = ["Salar" , "Issa" , "Issa"]
print("-".join(mylist))
print(" ".join(mylist))
print(" , ".join(mylist))
print(type(" , ".join(mylist)))




