def is_non_trivial(fraction):
    strfrac = str(fraction)
    top = strfrac.split("/")[0]
    bottom = strfrac.split("/")[1]
    num = int(top)/int(bottom)
    if top == bottom or (top[1]+top[0]) == bottom or ("0" in top or "0" in bottom):
        return False
    for i in top:
        if i in bottom and i != 0:
            top =top.replace(i,"")
            bottom =bottom.replace(i,"")
            if top == "" or bottom == "":
                return False
            if int(top)/int(bottom) == num:
                return True
    return False

def Solution():
    total = []
    for i in range(11,100):
        for j in range(i+1, 100):
            if is_non_trivial(str(i)+"/"+str(j)):
                total.append(str(i)+"/"+str(j))
    return total

print(Solution())