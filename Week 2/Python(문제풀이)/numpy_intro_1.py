import numpy as np 
#import: 다른 사람이 만들어둔 라이브러리를 불러오는 명령어
#numpy: 숫자 계산용 라이브러리 이름
#as np: "numpy"대신 짧게 "np"라고 쓰겠다는 뜻
py = [1, 2, 3, 4] #리스트 생성
np_arr = np.array([1, 2, 3, 4]) #np.array(): 넘파이 배열(array)을 만드는 함수
                                #리스트와 비슷하지만, "수학적 계산"에 특화된 자료형
                                #넘파이 배열은 덧셈, 곱셈 같은 연산이 전체 원소에 한꺼번에 적용
try:                            
    print("list * 2 =>", py * 2) #"리스트에 *2 연산을 하면 어떻게 될까?"를 테스트, 리스트는[1, 2, 3, 4]*2 : [1, 2, 3, 4, 1, 2, 3, 4] (즉, 숫자 계산이 아니라 "반복이 일어남")
except Exception as e: #try ~ except: 오류(에러)가 날 수도 있을 때 안전하게 실행시키는 구조
    print("list * 2 error:", e) 
print("numpy * 2 =>", np_arr * 2) #넘파이는 다르다! [1, 2, 3, 4]*2 = [2, 4, 6, 8] 즉, 각 원소에 "곱하기 2"가 적용됨 << 이것을 "벡터화"라고 부름
print("list sum =>", sum(py)) #sum(): 리스트 전체의 합을 구함
print("numpy sum =>", np_arr.sum(),"mean=>", np_arr.mean()) #np_arr.sum(): 넘파이 배열의 합 (함수형으로 쓰는 대신, 객체에 붙임)
                                                            #np.arr.mean: 평균(mean)을 구함             
#sum()은 총합, mean()은 평균
#리스트는 전부 더 하고 총합을 구하고 각 수에 *2를 하려면 수식을 넣어야 하는데 numpy는 훨씬 간단함