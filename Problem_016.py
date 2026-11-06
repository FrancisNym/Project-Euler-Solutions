# Question: 
# Sum of the digits of the number 2^1000

def MakeNumber():
    BinNum = ""
    for i in range(1000):
        BinNum += "0"
    BinNum = "1" + BinNum
    return int(BinNum, 2)

def Solution():
    StrNum = str(MakeNumber())
    total = 0
    for i in StrNum:
        total += int(i)
    return total

print(Solution())