'''
Question:
Find the largest palindromic number made from the product of 2 3 digit numbers
'''

def FlipString(string):
    NewStr =""
    for i in range(len(string)-1,-1,-1):
        NewStr += string[i]
    return NewStr

def CheckPalindrome(Num):
    StringNum = str(Num)
    if StringNum == FlipString(StringNum):
        return True
    else:
        return False

def CheckProductof2Numbers(Num):
    for i in range(999,99,-1):
        if Num % i == 0 and (Num//i) >99 and (Num//i) < 1000:
            return True
    return False

def Solution():
    for i in range(999*999, 100*100, -1):
        if CheckPalindrome(i) and CheckProductof2Numbers(i):
            return i


print(Solution())