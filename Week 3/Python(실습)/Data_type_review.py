a = [1, 2, 3] 
a.append(4)
print(a) #1번

for i in range(5):
    print("현재숫자:", i) #for 반복문
count=0
while count < 5:
    print("반복 횟수", count) #while 반복문
    count+=1

even=0 #무슨 뜻?
odd=0
for i in range(1, 21):
    if i % 2 == 0:
        even +=1 #무슨 뜻?
    else:
        odd +=1 #무슨 뜻?
print("짝수 갯수:", even)
print("홀수 갯수:", odd) 
 
scores= [77, 88, 95, 60, 82]
for s in scores:
    if s >= 90:
        grade = "A"
    elif s >= 80:
        grade = "B"
    else:
        grade = "C"
    print(f"{s}({grade})", end=" | ") #f-string(f"{변수}")로 문자열 포맷을 익히는 게 중요

total=0 #이거 이해 안됨
count=5 #이거 이해 안됨
for i in range(count):
               #이거 이해 안됨
    score = int(input(f"{i+1}번째 점수를 입력하세요: "))
    total += score #이거 이해 안됨

avg = total/count
print("평균 점수:", avg)

if avg >=90:
    print("A")
elif avg >= 80:
    print("B")
else:
    print("C")

scores = [77, 88, 95, 60, 82, 93, 99]
count_A = 0 #이거 이해 안됨
for s in scores:
    if s >= 90:
        count_A += 1 #이거 이해 안됨
print(f"A 등급은 총{count_A}명 입니다!")
                  #이거 이해 안됨
