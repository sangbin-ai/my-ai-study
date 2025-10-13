def func(x):
    if x % 2 == 0:
        return "짝수"
    else:
        return"홀수"
for i in range(3, 8):
    print(i, func(i))

def check_temp(t):
    if t >= 30:
        return "더움" 
    else:
        return "적당함"
for temp in [25, 32, 18, 30, 29]:
    print(temp, "도는", check_temp(temp)) # check_temp은 함수 그 자체(=코드 덩어리) 를 가리킴
                                        # check_temp()은 함수를 실행해서 나온 결과값을 받음 (return 한 값)   


