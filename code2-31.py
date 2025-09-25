monthly_sales = [1200, 1350, 1420, 1500, 1300, 1500, 1620, 1700, 1800, 1850, 1900, 2000]

first, seceond, *remaining = monthly_sales
print(f"1월 판매액: {first}")
print(f"2월 판매액: {seceond}")
print(f"나머지 월 판매액: {remaining}")

first, *middle, last = monthly_sales
print(f"첫 달 (1월) 판매액: {first}")
print(f"마지막 달 판매액: {last}")
print(f"중간 판매액: {middle}")
