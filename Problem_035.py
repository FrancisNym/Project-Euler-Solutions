def is_prime(num):
    if num <2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num %i == 0:
                return False
    return True

def GenPerms(lst):
    all_lsts = []
    if len(lst) == 1:
        return [lst]
    
    for i in range(len(lst)):
        start_val = lst[i]
        rest = lst[:i] + lst[i+1:]
        perms_rest = GenPerms(rest)
        for j in perms_rest:
            all_lsts.append([start_val]+j)
    return all_lsts
    



def Solution():
    total = 1
    nums = list(range(3,1000000))
    for i in nums:
        numlist = list(map(int,str(i)))
        all_perms = GenPerms(numlist)
        flag = True
        for j in all_perms:
            j = map(str,j)
            string = "".join(j)
            if not is_prime(int(string)):
                flag = False
            if int(string) in nums:
                nums.remove(int(string))
        if flag:
            total += len(numlist)
    return total-1 #account for 11


print(Solution())