def change(amount, coins):
    if amount == 0:
        return 1
    if coins == []: # No need to check amount here
        return 0
    result = 0
    if coins[0] <= amount:
        result += change(amount - coins[0], coins)
    return result + change(amount, coins[1:])
