nums = [3, 1, 4, 1, 5, 9]
result = sorted(set(nums), reverse=True) #set() = 중복 제거, sorted(..., reverse=True) = 내림차순 
print(result) #결과 출력

score = {"국어": 90, "영어": 80, "수학": 70}
age = sum(score.values()) / len(score)
print(f"평균 점수는,{age}점입니다") #f"문자열{변수값}문자열"

scores = {"국어": 90, "영어": 80, "수학": 70}
total = 0
for s in scores:
    total += scores[s] #total = 점수의 총합
    
age = total / len(scores)
print("총합은", total,"이고", "평균 점수는", age, "입니다")
# 🧠 오늘 배운 핵심
# 1. 딕셔너리 순회: for s in scores
# 2. 값 접근: scores[s]
# 3. len()으로 개수 세기
# 4. total += scores[s] 로 누적합
# 5. 평균 = total / len(scores)