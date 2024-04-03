def maxBottle(numBottle, numExchange):
    ans = numBottles
    emptyBottles = numBottles
    while(emptyBottles >= numExchange):
        ans += 1
        emptyBottles -= numExchange
        emptyBottles += 1
        numExchange += 1
    return ans
        