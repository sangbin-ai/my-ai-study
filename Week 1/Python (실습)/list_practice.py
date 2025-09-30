# 리스트 만들기
fruits = ["사과", "바나나", "포도"]

# 리스트 출력
print("과일 목록:", fruits)

# 인덱스로 접근 (0부터 시작)
print("첫 번째 과일:", fruits[0])
print("두 번째 과일:", fruits[1])

# 리스트에 값 추가
fruits.append("망고")
print("추가 후:", fruits)

# 리스트에서 값 제거
fruits.remove("바나나")
print("제거 후:", fruits)

# 리스트 길이
print("리스트 길이:", len(fruits))

# 반복문으로 출력
for fruit in fruits:
    print("과일:", fruit)
