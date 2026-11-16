def Solution():
    runs_without_found = 0
    i = 2
    overall_total = 0
    while runs_without_found < 1000000:
        strnum = str(i)
        total = 0
        for j in strnum:
            total += int(j)**5
        if total == i:
            overall_total += i
            runs_without_found = 0
        runs_without_found += 1
        i += 1
    return overall_total

print(Solution())