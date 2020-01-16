"""
Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.
"""

#big_range = range(1, 101)
#for n in big_range:
#    print(n)

"""
For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
"""

#big_range = range(1, 101)
#for n in big_range:
#    if n % 5 == 0:
#        print("Chicken")
#    else:
#        print(n)


"""
For the multiples of seven (7, 14, 21, etc.) print "Monkey".
"""

#big_range = range(1, 101)
#for n in big_range:
#    if n % 5 == 0:
#        print("Chicken")
#    elif n % 7 == 0:
#        print("Monkey")
#    else:
#        print(n)

"""For numbers which are multiples of both five and seven print "ChickenMonkey".
To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator. """

big_range = range(1, 101)
for n in big_range:
    if n % 5 == 0:
        print("Chicken")
    if n % 7 == 0:
        print("Monkey")
    if n % 5 == 0 and n % 7 == 0:
        print("ChickenMonkey")
    else:
        print(n)