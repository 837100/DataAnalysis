name = "홍길동"
age = 30
salary = 3500000
tax_rate = 0.1
basic_format = "이름: {}, 나이: {}, 월급: {}원".format(name, age, salary)
index_format = "직원 {0}의 나이는 {1}세이고, {0}의 세후 월급은 {2}원 입니다.".format(
    name, age, int(salary * (1 - tax_rate))
)
keyword_format = (
    "직원정보: 이름: {employee} 나이: {years}세 "
    "월급: {income:,}원 세금: {tax:.1%} 실수령액: {net_income:,}원".format(
        employee=name,
        years=age,
        income=salary,
        tax=tax_rate,
        net_income=int(salary * (1 - tax_rate)),
    )
)
print(basic_format)
print(index_format)
print(keyword_format)
