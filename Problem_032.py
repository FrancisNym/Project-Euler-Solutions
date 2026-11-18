def Solution():
    all_products = []
    sum = 0
    for num1 in range(1,10000):
        for num2 in range(1,100):
            product = num1 * num2
            str1 = str(num1)
            str2 = str(num2)
            str3 = str(product)
            totalstr = str1+str2+str3
            if len(totalstr) == 9:
                for i in range(1,10):
                    if str(i) not in totalstr:
                        break
                    if i==9 and product not in all_products:
                        all_products.append(product)
                        sum += product
    return sum, all_products

print(Solution())