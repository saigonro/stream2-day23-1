from byotest import *

euro_coins = [200, 100, 50, 20, 10, 5, 2, 1]
us_coins = [100, 50, 25, 10, 5, 1]

def get_change(amount, denominations = euro_coins):
    coins = []
    for coin in denominations:
        while amount >= coin:
            coins.append(coin)
            amount -= coin
    return coins

test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])
test_are_equal(get_change(200),[200])
test_are_equal(get_change(3),[2, 1])
test_are_equal(get_change(7),[5, 2])
test_are_equal(get_change(9),[5, 2, 2])
test_are_equal(get_change(75, us_coins),[50, 25])

print("All tests pass")