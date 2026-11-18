def Solution():
    coins = [1,2,5,10,20,50,100,200]
    ways = [1] + [0]*200
    for i in coins:
        for amount in range(i, 201):
            ways[amount] += ways[amount-i]
    return ways[200]

print(Solution())