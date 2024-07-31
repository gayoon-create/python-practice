# 파이썬에서의 주석

# 파이썬에서의 변수 선언은 따로 키워드가 있지 않다.
num1 = 3
num2 = 5
print(num1 + num2)

print(type(num1))  # int

pi = 3.14159265358979 
print(type(pi)) # float

# 반지름이 5cm인 원의 넓이
radius = 5
circleArea = pi * (radius ** 2)
print("원 넓이 : ", circleArea)

# boolean
근영이가핸섬 = True
오늘은토요일인가 = False

print(type(근영이가핸섬)) #bool

# str
name = "홍길동"
print(type(name)) # str

# None(null)
myStr = None
if(myStr == None) :
    print("myStr is None")
else : 
    print("myStr is not None")

# 기초 자료형은 위와 같다. 하지만 위의 기초 자료형 이외에도 list(ArrayList), tuple(읽기 전용 ArrayList), dict(Map) 등이 있다.