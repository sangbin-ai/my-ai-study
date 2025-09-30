#Python(문자형)
head = "Python"
tail = " is fun!"
print(head + tail)
#Python(문자*숫자)
a = " Python"
print(a * 3)
#Python(문자*숫자 응용)
print("=" * 50)
print("My Program")
print("=" * 50)
#Python(문자열 길이 구하기)
a = "Life is too shrot"
print(len(a))
print(a[3]) #Python (인덱싱 활용) *0부터 시작
print(a[12])
#Python (슬라이싱 활용) *[a:b] a 이상 b 미만
print(a[0:4])
a = "20250922Sun"
date = a[:8]
weater = a[8:11]
print(date)
print(weater)
#문자열 포매팅 (f-string)
a = f"나는 공부를 {80}% 했다" 
print(a)