# try:
#     result = 10 / 0
# except Exception as e: 
#     print(type(Exception))
#     print(type(Exception).__name__)
#     print(type(e))
#     print(type(e).__name__)
#     print('0으로 나눌 수 없습니다.')

# # except ZeroDivisionError:
# #     print('0으로 나눌 수 없습니다.')

# import logging, traceback

# logging.basicConfig(level=logging.ERROR)

# try:
#     result = 10 / 0
# except Exception as e:
#     logging.error("예외 발생: %s: %s", type(e).__name__, e)
#     logging.error("스택 트레이스:\n%s", traceback.format_exc())

try:
    result = 10 / 2
except Exception as e:
    print("예외 발생:", type(e).__name__, e)
else:
    print("성공! 결과:", result)   # 예외 없을 때만 실행
finally:
    print("리소스 정리 (무조건 실행)")