# Question:
# How many sundays fell on the first day of the month during the 20th century

def Solution():
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    count = 0
    day_of_week = 0
    for i in range(101):
        if i % 4 == 0 and i != 0:
            month_days[1] = 29
        else:
            month_days[1] = 28
        for j in range(12):
            if day_of_week == 6:
                count += 1
            day_of_week = (day_of_week + month_days[j] % 7) % 7
            if i == 0:
                count = 0
    return count

print(Solution())