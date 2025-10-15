import math
import random as rd
from datetime import date

print("sqrt(16)=", math.sqrt(16))
print("sin(90 degrees)=", math.sin(math.radians(90)))
print("랜덤 숫자:", rd.randint(1, 10))
print("랜덤 선택:", rd.choice(["상빈", "민수", "지현", "도윤" ]))
today = date.today()
print("오늘 날짜:", today)

try:
    num = int(input("숫자를 입력하세요:")) # try: 오류가 날 가능성이 있는 코드
    result = 10/num
    print("결과:", result)
except ValueError:                      # except: 오류가 났을 때 실행할 코드, ValueError: 문자열을 숫자로 변환 불가
    print("❌ 숫자가 아닌 값을 입력했습니다!")
except ZeroDivisionError:               # ZeroDivisionError: 0으로 나누기 불가
    print("❌ 0으로 나눌 수 없습니다!")
finally:                                # finally: 무조건 실행되는 코드 (에러 있든 없든)
    print("✅ 프로그램 종료 (예외와 상관없이 실행됨)")
try:
    f = open("없는 파일. txt", "r")
    content = f.read()
except FileNotFoundError:               # FileNotFoundError: 파일 없음
    print("⚠️ 파일을 찾을 수 없습니다.")
finally:
    print("파일 시도 완료")
    # IndexError: 인덱스 범위 초과

def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다!")
    return a / b
try:
    print(divide(10, 0))
except ValueError as e:
    print("❌ 오류 발생:", e)
finally:
    print("✅ 코드 실행 완료")