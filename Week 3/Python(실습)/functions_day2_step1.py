def add(a, b):
    return a+b
result = add(2, 3)
print(result)

def greet(name, prefix="hello"):
    print(f"{prefix}, {name}!")
greet("상빈")
greet("상빈", "Yo")

def power(base, exponent=2):
    return base ** exponent
print(power(3))
print(power(3, 3))

def introduce(name, age, city):
    print(f"이름: {name}, 나이: {age}, 도시: {city}")
introduce(name= "상빈", age= "25", city= "경기도")
introduce(city= "부산", name= "민수", age= "22" )

def add_all(*nums):
    print(nums)
    return sum(nums)
print(add_all(1, 2, 3))
print(add_all(10, 20, 30 ,40))

def print_info(**info):
    print(info)
print_info(name="상빈", age=25, city="경기도")

def order(drink, size="M", *extras, **customs):
    print(f"음료: {drink}, 사이즈: {size}") #한 줄로 쓰면 안되나?
    print(f"추가옵션: {extras}")
    print(f"세부 설정 {customs}")
order("아메리카노", "L", "샷 추가", "휘핑 x", sugar="적게", ice="보통")

def make_profile(name, age, **info):
    profile = {"name": name, "age": age}
    profile.update(info)
    return profile
p1 = make_profile("상빈", 25, city = "경기도", hobby = "코딩", level = "초보")
print(p1)
