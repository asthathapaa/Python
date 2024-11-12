# print("Twinkle, twinkle, little star \n\t How I wonder what you are! \n \t \t Up above the world so high \n \t \t Like a diamond in the sky.\nTwinkle,Twinkle, little start, \n\t How I wonder what you are")

# import platform
# print(platform.python_version_tuple())

# import datetime
# now = datetime.datetime.now()
# print("Current date and time:")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# from math import pi
# r = float(input("r = "))
# print("Area =" + str(pi*r*r))
# # area = pi * r *

# firstn = input("Enter your first name: ")
# lastn = input("Enter your last name: ")
# print(str(lastn ) +str(" ") + str(firstn))

a ,b , c= input("Enter no: " ).split()

list = a.split(",") + b.split(",") + c.split(",")
tuple = tuple(list)
print("List :" , list)
print("tuple :", tuple)
