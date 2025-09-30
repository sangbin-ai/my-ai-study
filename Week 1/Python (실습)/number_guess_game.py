import random

# 1부터 10 사이의 랜덤 숫자
answer = random.randint(1, 10)

while True:
    guess = int(input("1부터 10 사이의 숫자를 맞혀보세요: "))

    if guess == answer:
        print("✅ 정답! 축하합니다!")
        break
    elif guess < answer:
        print("👉 더 큰 숫자입니다.")
    else:
        print("👉 더 작은 숫자입니다.")
