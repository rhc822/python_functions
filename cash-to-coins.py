import math

""" Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies. """

dollarAmount = 8.69

#take the dollarAmount, handle the quarters first, do the calculation, subtract from the total. From the remainder, concintue on...

piggyBank = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0
}

#while dollarAmount != 0:
piggyBank["quarters"] = math.floor(dollarAmount / 0.25)
dollarAmount -= (math.floor(dollarAmount / 0.25)) / 4
print(dollarAmount)

piggyBank["dimes"] = math.floor(dollarAmount / 0.10)
dollarAmount -= (math.floor(dollarAmount / 0.10)) / 10
print(dollarAmount)

piggyBank["nickels"] = math.floor(dollarAmount / 0.05)
dollarAmount -= (math.floor(dollarAmount / 0.05)) / 20
print(dollarAmount)

piggyBank["pennies"] = math.ceil(dollarAmount / 0.01)
dollarAmount -= (math.ceil(dollarAmount / 0.01)) / 100
dollarAmount = int(dollarAmount)
print(int(dollarAmount))

"""     piggyBank["dimes"] = math.floor(dollarAmount / 0.10)
    piggyBank["nickels"] = dollarAmount / 20,
    piggyBank["pennies"] = dollarAmount / 100

print(piggyBank)
 """
""" def calc_coins():
    for x in piggyBank.values():
        piggyBank["quarters"] = dollarAmount / 4,
        piggyBank["dimes"] = dollarAmount / 10,
        piggyBank["nickels"] = dollarAmount / 20,
        piggyBank["pennies"] = dollarAmount / 100
    print(piggyBank) """

# Your magic Python code here
#That should produce the following output.
#>>> print(piggyBank)
#{ 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }

#calc_coins()