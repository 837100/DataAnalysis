try:
    number = int(input("숫자를 입력하세요: "))
    result = 10 / number

except ValueError:
    print("숫자 입력해")
except ZeroDivisionError:
    print("0으로 못나눈다")
    print(ZeroDivisionError)

