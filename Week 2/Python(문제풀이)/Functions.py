def greet():
    return "Hello, Sangbin!"
print(greet())
 
def square(x):
    return x * x
print(square(25))

def add(a, b):
    return a+ b
print(add(3, 7))
print(add(-5, 10))

def check_even(num):
    if num % 2 == 0:
        return f"{num}은 짝수다." #f-string f"문자열{변수}
    else:
        return f"{num}은 홀수다."

print(check_even(4))
print(check_even(7))

def bmi(weight, height):
    return weight / (height/100)**2
print(bmi(72, 170))

def print_squares(numbers):
    for n in numbers:
        print(f"{n}의 제곱은 {n**2}이다")

print_squares([1, 2, 3, 4, 5])
 
def square(x):
    return x**2
print("3의 제곱:", square(3))
print("10의 제곱:", square(10))