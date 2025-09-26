list1 = ['사과', '복숭아', '바나나']
list2 = ['주스', '잼', '통조림']
pairs = [ ]
for fruit in list1:
    for product in list2:
        pairs.append((fruit, product))
print(pairs)