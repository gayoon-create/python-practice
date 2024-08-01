# 튜플 : 리스트와 비슷하지만 변경할 수 없는(immutable) 자료형(readonly)

# tuple 생성

tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('apple', 'banana', 'cherry')


print(tuple1)

# tuple에서 값 얻어오기
print(tuple1[2])

# list, tuple indexing
list = ['a', 'b', 'c', 'd', 'e', 'f']

# list[시작값 : 종료값(포함안됨)]
print(list[2:5]) # 2, 3, 4번째 index만 나온다.
print(list[1:]) # 종료값이 생략 -> 1번 index부터 끝까지 나온다.

print(list[:-1]) # -1번 index : 마지막 index / 시작값 생략되면 0 <= index <= len(list)

tuple3 = ('apple', 'banana', 'cherry', 'apple')
print(tuple3[2:]) # 2 <= index <= len(tuple3)