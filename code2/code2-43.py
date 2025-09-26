employees = {"이지혜": 3000000, "구민준": 5000000, "방서연": 4100000}

adjust_salary = lambda salary: salary * 1.1
updated_salaries = {name: adjust_salary(salary) for name, salary in employees.items()}

print(updated_salaries)
