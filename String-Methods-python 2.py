

# --------------------
# Strings Methods
# ----------------------------

# index(SubString, Start, End)
a = "I Love Python"
print(a.index("P", 0, 10)) # 7

print(a.index("P", 0, 5)) # ValueError: substring not found


# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P", 0, 10)) # 7

print(b.find("P", 0, 5)) # -1


# rjust(Width, Fillchar) 

s = "salar"
print(s.rjust(10)) #      salar
print(s.rjust(10 , "#")) # #####salar

# ljust(Width, Fillchar)

s = "salar"
print(s.ljust(10)) # salar     
print(s.ljust(10 , "#")) # salar#####


# Splitlines()
e = ''' First Line
Second Line
Third Line'''
print(e.splitlines()) # [' First Line', 'Second Line', 'Third Line']

# istitle()
one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle()) # True
print(two.istitle()) # False

# isspace()
three = " "
four = ""
print(three.isspace()) # True
print(four.isspace()) # False

# islower()
five = "i love python"
six = "I Love Python"

print(five.islower()) # True
print(six.islower()) # False

# isidentifier()

seven = "salarissa"
eight = "Salar-issa"
nine = "salarissa1995"
print(seven.isidentifier()) # True
print(eight.isidentifier()) # False 
print(nine.isidentifier()) # True


# isalpha()
x = "AaaaaaBbbbbbbb"
y = "AaaaaaBbbbbbbb4739539"
print(x.isalpha()) # True
print(y.isalpha()) # False

# isalnum()

t = "AaaaaaBbbbbbbb" 
g = "AaaaaaBbbbbbbb4739539" 
print(t.isalnum()) # True
print(g.isalnum()) # True 


# replace(Old Value, New Value , Count)

a = "Hello One Two Three One One"
print(a.replace("One", "1", )) # Hello 1 Two Three 1 1
print(a.replace("One", "1", 1 )) # Hello 1 Two Three One One
print(a.replace("One", "1", 2 )) # Hello 1 Two Three 1 One


# Join(Iterable)

mylist = ["Salar" , "Issa" , "Issa"]
print("-".join(mylist)) # Salar-Issa-Issa
print(" ".join(mylist)) # Salar Issa Issa
print(" , ".join(mylist)) #  Salar , Issa , Issa
print(type(" , ".join(mylist))) # <class 'str'>




