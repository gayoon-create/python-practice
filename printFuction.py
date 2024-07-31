# print 함수의 다양한 출력 방법을 알아보자.

# print 함수는 다양한 서식을 제공한다.
# %d : 10진 정수
# %f : 실수
# %s : 문자열

print("10진 정수 : %d" % 10)
print("%d * %d = %d" % (3, 5, 15))

print("실수 : %f" % 3.14)
print("실수 : %5.2f" % 3.14)

print("Hello, World!", end=" ") # print() 함수에서 end=" "를 사용하면 문자열 출력 후 줄바꿈을 하지 않는다.
print("We are the World!")