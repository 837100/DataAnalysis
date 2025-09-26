# try:
#     file = open("data.csv", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("파일없어")
# finally:
#     print("파일 작업 종료")
#     file.close()

# data.csv 가 없으면 open(...) 에서 FileNotFoundError 발생 → 그 즉시 try 블록이 중단되고 except 로 이동.
# 이때 file = ... 대입이 끝나지 않았으므로 변수 file 자체가 생성되지 않음.
# finally 블록은 항상 실행되므로 file.close() 를 호출하려다 file 이 정의되지 않아 NameError (혹은 UnboundLocalError) 발생.
# 결과적으로 원래의 FileNotFoundError 메시지는 가려지고(덮여서) 나중 예외(NameError)만 보이게 됨.
# 즉, file.close() 에 괄호를 붙인 것만으로는 “파일이 열리지 못한 경우”를 처리하지 못합니다.


# try:
#     with open("data.csv", "r", encoding="utf-8") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("파일없어")
# except Exception as e:
#     print(f"다른 예외: {type(e).__name__}: {e}")
# finally:
#     print("파일 작업 종료")

# f = None
# try:
#     f = open("data.csv", "r", encoding="utf-8")
#     content = f.read()
#     print(content)
# except FileNotFoundError:
#     print("파일없어")
# finally:
#     if f is not None:
#         f.close()
#     print("파일 작업 종료")

try:
    with open("data.csv", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("노파일")
finally:
    print("작업 끔")
