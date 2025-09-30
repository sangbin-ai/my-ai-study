print("✨ BMI 계산기 ✨")
print("------------------------")


name = input("이름을 입력하세요: ")
weight = float(input(f"{name}님, 체중(kg)을 입력하세요: "))
height = float(input(f"{name}님, 키(cm)를 입력하세요: "))


height_m = height / 100  # cm -> m
bmi = weight / (height_m ** 2)


print("\n------------------------")
print(f"{name}님의 BMI는 {bmi:.2f}입니다.")  # 소수점 2자리
print("------------------------")


if bmi < 18.5:
    status = "저체중"
elif 18.5 <= bmi < 24.9:
    status = "정상 체중"
elif 25 <= bmi < 29.9:
    status = "과체중"
else:
    status = "비만"

print(f"체중 상태: {status} 🩺")
print("------------------------")
print("건강을 위해 적절한 식습관과 운동을 유지하세요! 💪")