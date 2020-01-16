"""
Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.

quarters
nickels
dimes
pennies

For each coin type, give yourself as many as you like.

Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.

Given the coins shown above, the output would be 7.07 when you call calc_dollars()"""

def calc_dollars():
    piggyBank = {
        "pennies": 342,
        "dimes": 32,
        "nickels": 9
    }
    dollarAmount = (piggyBank["pennies"] / 100) + (piggyBank["dimes"] / 10) + (piggyBank["nickels"] / 20)

    print(dollarAmount)

calc_dollars()

#    +=
#   loop through
#    add all
#    display total