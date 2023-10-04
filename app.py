a = True
b = 3

if a>b:
    print( str(a) + "is greater than " + str(b))
else:
    print("A not  equal B")

# with elsif

if a == 2:
    print("A is true")
elif a == False:
    print("A is False")
else:
    print("A  is none of the options")
# using or and not 

boy = True
short = True

if boy == True or short == True:
    print("He is a boy or he is short")
elif boy == False:
    print("A is false")
else:
    print("A is none of the above")
# and 
boy = True
short = True

if boy == True and short == False:
    print("He is a boy or he is short")
else:
    print("A is none of the above")


#
value = input("Input a value:")
if type(value) == str:
    print(value + "is a string")
elif type(value) == int:
    print(value + "is an int")
elif type(value) == list:
    print(value + "is a list")
else:
    print("We dont/'t Know the data type of" + value)