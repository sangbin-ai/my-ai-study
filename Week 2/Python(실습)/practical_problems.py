ages = [15, 22, 35, 18, 40, 29, 13]#20세 이상 성인만 리스트 추출
adult_ages = [age for age in ages if age >= 20]
print(adult_ages)

scores = [45, 67, 89, 32, 76, 90, 60]#60점 이상인 학생만 리스트 추출
successful_student= [score for score in scores if score >=60]
print(successful_student)

roducts = ["apple", "banana", "airpods", "cherry", "avocado"] #a 들어가는 글자 리스트에서 출력
result = [p for p in roducts if "a" in p]
print(result)

products = ["apple", "banana", "airpods", "cherry", "avocado", "orange"] #o 들어가는 글자 리스트에서 출력
results=[ z for z in products if "o" in z]
print(results)

log = "2025-09-30 11:32:15 | User login success" #2025-09-30 글자 리스트에서 출력 *for문은 하나하나를 꺼내 바구니에 담는것이므로 전체 글자를 출력하는 여기선 for문 x
Date = log[:10]
print(Date)

prices = [1000, 2500, 3000, 1500, 1200] # 현재 가격에서 부가세 10% 붙인 가격을 리스트에서 출력
value = [int(p * 1.1) for p in prices]
print(value)