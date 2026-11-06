words = {1:"one", 2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"one hundred"}

def ConverNumToWords(num):
    length = len(str(num))
    if length == 1:
        return words[num]
    if length == 2:
        if num in words:
            return words[num]
        else:
            tens = int(str(num)[0]+"0")
            units = int(str(num)[1])
            return words[tens] + words[units]
    if length == 3:
        hundreds = int(str(num)[0]+"00")
        tens = int(str(num)[1]+"0")
        units = int(str(num)[2])
        WordHundreds = ConverNumToWords(int(str(hundreds)[0])) + "hundred"
        if tens == 0 and units == 0:
            return WordHundreds
        if tens == 0:
            word = WordHundreds +"and"+ ConverNumToWords(units)
            return word
        if units == 0:
            word = WordHundreds +"and"+ ConverNumToWords(tens)
            return word
        else:
            if int(str(num)[1:]) in words:
                return WordHundreds + "and" + words[int(str(num)[1:])]
            else:
                word = WordHundreds +"and"+ ConverNumToWords(tens) + ConverNumToWords(units)
            return word


def Solution():
    total = 0
    for i in range(1,1000):
        total += len(ConverNumToWords(i))
    total += 11 # One thousand
    return total

print(Solution())