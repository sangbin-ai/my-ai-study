x = 7
y = 2.5
z = "Ai Tech"

print([x * y]) #자료형 (숫자형)
print(" ".join([z] * 3)) # Ai Tech 띄어쓰기 (문자형)

age = int(input("나이를 입력하세요: "))

if age >= 19:
    print("성인입니다")
elif age >= 13:
    print("청소년입니다") # 여기서 이미 19살 이상은 걸러져서, 13~19 자동 처리
else:
    print("어린이입니다")

menu = input("메뉴를 입력하세요:") #다시 한번 풀어보자 ★중요
if menu == "햄버거":
    print("햄버거를 주문하셨습니다")
elif menu == "피자":
    print("피자를 주문하셨습니다")
elif menu == "샐러드":
    print("샐러드를 주문하셨습니다")
else:
    print("메뉴에 없는 주문입니다")

for m in range(3):
    menus = input("메뉴를 입력하세요") #다시 한번 풀어보자 ★중요

    if menus == "햄버걸":
        print("햄버걸 주문하셨습니다")
    elif menus == "피짜":
        print("피짜를 주문하셨습니다")
    elif menus == "샐러디":
        print("샐러디를 주문하셨습니다")
    else:
        print("주문표에 없는 메뉴입니다")

total = 0  #for문 *많이 헷갈린다* ★★중요
for i in range(1, 11):
     total += i
print("for문 합계", total)

total = 0  #while문 *많이 헷갈림* ★★중요
i = 1
while i <= 10: #i가 10 이하일 동안 반복
    total += i
    i += 1     #i = i + 1 (증가시키지 않으면 무한반복!)
print("while문 합계:", total)

