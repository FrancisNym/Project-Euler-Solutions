'''
Question:
Find the pythagorean triplet where a+b+c = 1000, return abc
'''

def Solution():
    for a in range(1,1001):
        for b in range(a+1,1001):
            c = (a**2+b**2)**0.5
            if c.is_integer and a+b+c==1000:
                return a*b*c

print(Solution())