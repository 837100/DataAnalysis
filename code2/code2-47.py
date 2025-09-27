employees = [
    {'name': '김지원', 'salary': 37000000},
    {'name': '도민준', 'salary': 70000000},
    {'name': '이서연', 'salary': 44000000},
    {'name': '정현우', 'salary': 35000000},
]
updated_employees = list(map(lambda emp: {'name': emp['name'], 'salary': emp['salary'] * 1.1}, employees))

print('\n급여 인상 후:')
for emp in updated_employees:
    print(f'{emp['name']}: {int(emp['salary']):,}원')