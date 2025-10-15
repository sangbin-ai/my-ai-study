def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("숫자만 주세요!")
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다!")
    return a / b
try:
    print(divide(10, 0))
except (ValueError, ZeroDivisionError) as e:
    print("에러:", e)