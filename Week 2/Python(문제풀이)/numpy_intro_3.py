import numpy as np
a = np.array([2, 3])
b = np.array([4, 5]) #리스트를 넘파이 배열로 바꿈 (벡터 연산이 수학처럼 자연스럽게 작동시키기 위함)
dot = np.dot(a, b) #np.dot(): 내적(dot product)을 계산하는 함수, 내적=각 성분끼리 곱해서 더한 것 즉, 2*4 + 3*5 = 8 + 15 = 23 결국 dot 값은 23!
print("백터 a:", a) # 벡터 a를 출력
print("백터 b:", b) # 벡터 b를 출력
print("a * b =", dot) # dot값을 출력
manual = a[0]*b[0] + a[1]*b[1] # a[0]은 첫 번째 원소(2), a[1]은 두 번째 원소(3). 따라서 2*4 + 3*5 = 23 np.dot(a, b)와 값이 같다는걸 증며하려고 넣은것!
print("내가 계산 =", manual) #내적을 직접 손으로 계산한 것
cosine_similarity = dot / (np.linalg.norm(a) * np.linalg.norm(b)) #★★중요 np.linalg.norm()은 벡터의 길이(크기)를 구하는 함수, np.linalg = "선형대수"의 약자
                                                                  #공식은 수학적으로 >> <cos(0) = (a*b) / (|a| * |b|)>
                                                                  #두 벡터의 방향이 얼마나 비슷한지를 나타내는 공식, 
                                                                  # 결과가 0.99면 거의 같은 방향 
                                                                  # 0이면 직각
                                                                  # -1이면 반대 방향
print("코사인 유사도 =", cosine_similarity)