def check_temp(temp):
    if temp >= 30:
        print("너무 더워요")   # 1번 문제 print()는 “화면에 결과를 보여주는 것
    elif temp <= 15:          # return은 “값을 함수 밖으로 돌려주는 것
        print("너무 추워요!")   # 단순히 결과를 출력하고 싶으면 → print()만
    else:                      # 나중에 다른 계산에 다시 써야 하면 → return
        print("적당합니다!") 
check_temp(15)

menu = [1500, 2300, 1200]
total = 0                     # 2번 문제
for price in menu:            # print()를 for문 밖으로 빼야지 총합만 나옴 << for문 안이면 누적합이 나옴
    total += price          
print("총 주문 금액", total)

for i in range(1, 21):       # !는 "같지 않다"라는 뜻
    if i % 2 != 0:           # continue는 "해당 반복문은 건너 뛰고 다음걸로" 라는 뜻
        continue
    print(i,"짝수")    