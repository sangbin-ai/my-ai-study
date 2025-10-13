def greet(name):
    return "안녕,"+ name + "\n오늘도 파이썬 멋지게 해보자!" # ,(콤마)는 print() 함수 안에서만 쓸 수 있어서 print() 를 제외 한 곳에선 문자열끼리 연결하려면 +를 써야 함
result = greet("상빈")                                  # \n (역슬래시 n)은 줄 바꿈이다         예시) text = "안녕\n상빈"
print(result)                                                                                            #print(text)  >> 결과 안녕
                                                                                                                              #상빈
def check_temp(temp):
    if temp >= 30:
        return "⚠️ 너무 더워요!"
    elif temp <= 15:
        return "❄️ 너무 추워요!"
    else:
        return "😊 적당합니다."
Current_temperature = int(input("현재 온도를 입력하세요:"))
print(check_temp(Current_temperature))

def calc_total(order_list):
     prices = {"치킨너겟": 1500, "미니버거": 2300, "고구마스틱": 1200}
     total = 0
     for item in order_list:
       total += prices[item]
     return total

orders = ["치킨너겟", "미니버거"]
print("총 금액은",calc_total(orders),"입니다!")