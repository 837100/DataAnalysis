name = "홍길동"
age = 30
salary = 3500000
tax_rate = 0.1
basic_format = f"이름: {name}, 나이: {age}, 월급: {salary}원"
index_format = f"직원 {name}의 나이는 {age}세이고, {name}의 세후 월급은 {int(salary * (1 - tax_rate))}원입니다."
keyword_format = f"직원정보: 이름: {name} 나이: {age}세 \
 월급: {salary:,}원 세금: {tax_rate:.1%} \
실수령액: {int(salary * (1-tax_rate)):,}원"
print(basic_format)
print(index_format)
print(keyword_format)