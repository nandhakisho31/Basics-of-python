#variables (strings, int, boolan)
Patient_name = "John smith"
print (Patient_name)
age = 20
is_new = True
print (is_new)
print ("age =", age)

#input function
name = input("what is your name? ")
print ("hellow " + name)

#type conversions
first = input("First: ")
secound = input("Secound: ")

sum = float(first) + float(secound)
print ("Sum: ", sum)

#arthametic operators
#** square mulitiplication, % is to get reminder for devision. != not equale to, ==equale, <= greater then equal to.

#logical operators. and (both), or (at least one) not (justifies).
#example:
price = 50
print (not price > 30)
print (price < 5 or price > 30)
print (price > 5 and price < 100)

#if else and elif statements.
#in python we use indendation for block of code.
temperature = 29

if temperature > 30:
    print ("it's a hot summer day")
    print("drink plenty of water")
elif temperature > 20:
    print ("it's a bit clod")

elif temperature > 10:
    print ("it's bit clod")
else:
    print ("it is to cold")
print ("done")
