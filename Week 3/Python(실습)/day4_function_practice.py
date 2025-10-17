def add(a, b):
    return a+b
result = add(3, 5)
print("결과:", result)

x = 10
def change():
    x = 5
    print("함수 안:", x)
change()
print("함수 밖", x)

numbers= [1, 2, 3, 4, 5]
print(sum(numbers))
print(list(map(lambda x: x*2, numbers)))
print(list(filter(lambda x: x%2==0, numbers)))
print(list(zip(["a", "b", "c"], [1, 2, 3])))