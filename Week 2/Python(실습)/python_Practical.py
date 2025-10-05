score = int(input("점수를 입력하세요:")) #성적 판별기 *숫자를 출력 시 >> int(input())
if score >= 90:
    print("A등급")
elif score >= 80:
    print("B등급")
elif score >= 70:
    print("C등급")
else: 
    print("F등급")

total = 0
scores = [88, 92, 79, 93, 85]
for s in scores:
    total += s
average = total / len(scores)
print("평균 점수는:", average)

def calculate_interest(amount, rate):
    return amount * (1 + rate / 100)
amount = float(input("예금액을 입력하세요:")) #입력값 수사형 변환 신경 *float
rate = float(input("이자율(%)을 입력하세요:"))
result = calculate_interest(amount, rate) #결과라는 새로운 수식을 넣어 전체 호출을 하도록!
print("1년 후 금액:", result,"만원")

