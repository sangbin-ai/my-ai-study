import random

answer = random.randint(1, 10)  
max_attempts = 3

print("숫자 맞추기 게임! 1부터 10까지. 기회는 3번입니다.")

attempt = 0
while attempt < max_attempts:
    attempt += 1
    try:
        guess = int(input(f"[{attempt}/{max_attempts}] 숫자 입력: "))
    except ValueError:
        print("⚠️ 숫자를 입력해 주세요.")
        attempt -= 1  
        continue

    if guess == answer:
        print("✅ 정답! 역시 넌 천재야 상빈!")
        break
    elif guess < answer:
        print("👉 더 큰 숫자야.")
    else:
        print("👉 더 작은 숫자야.")

else:
    
    print(f"😢 아쉽다..ㅠㅠ 정답은 {answer}이였어.")
