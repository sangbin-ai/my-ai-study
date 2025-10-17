def bmi(weight, height):
    bmi_value = weight / (height/100)**2
    if bmi_value < 18.5:
        status = "저체중"
    elif bmi_value < 25:
        status = "정상"
    else:
        status = "과체중"
    return round(bmi_value, 2), status
print("▶ BMI 예시")
print(bmi(70,175))
print(bmi(50, 165))
print(bmi(85, 172))
print("-"*30)

students = ["상빈", "지우", "민재", "서윤"]
scores_kor = [85, 90, 75, 95]
scores_eng = [80, 92, 70, 88]
combined = list(zip(students, scores_kor, scores_eng))
print("▶ 학생별 점수 묶기:", combined)
avg_scores = list(map(lambda x: round((x[1] + x[2]) / 2, 1), combined))
print("▶ 평균 점수:", avg_scores)
high_scorers = list(filter(lambda x: (x[1] + x[2]) / 2 >=85, combined))
print("▶ 우수 학생:", high_scorers)
print("-"*30)

def number_classifier(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return even, odd
nums = list(range(1, 11))
print("▶ 짝수/홀수 분류기")
print(number_classifier(nums))
print("-"*30)

def grade_system(students, scores):
    avg = sum(scores) / len(scores)
    grades = []
    for s in scores:
        if s >= 90:
            grades.append("A")
        elif s >= 80:
            grades.append("B")
        elif s >= 70:
            grades.append("C")
        else:
            grades.append("D")
    return list(zip(students, scores, grades)), avg
print("▶ 등급 시스템")
result, avg = grade_system(students, scores_eng)
print("학생별 등급:", result)
print("전체 평균:", round(avg, 1))
