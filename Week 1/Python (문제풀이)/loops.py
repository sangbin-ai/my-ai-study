for i in range(5):
    print(i) #for 반복문 (for은 차례대로 출력)

n = 3
while n > 0:
    print("안녕")
    n -= 1 #while 반복문 (while은 조건이 참일 때까지 출력)
    
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}") #for 반복문 구구단

password = "1234"
guess = ""
while guess != password:
    guess = input("비밀번호 입력: ")
print("접속성공!")