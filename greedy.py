import cs50
import math

print("How much change is owed?")
change = cs50.get_float()

while change <= 0:
    print("How much change is owed?")
    change = cs50.get_int()
    
# change the amount into cents
change = round(100 * change)

# for each coin denomination, extract out the amount of coins and update the change total 
quarters = math.floor(change / 25)
change = change - (quarters * 25)
    
dimes = math.floor(change / 10)
change = change - (dimes * 10)

nickels = math.floor(change / 5)
change = change - (nickels * 5)

pennies = change

coins = quarters + dimes + nickels + pennies
print(coins)
