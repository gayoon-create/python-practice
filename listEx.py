#  자바스크립트의 배열과 같은 방식으로 동작하는 list에 대해 알아보기

# 크기가 동적인 배열, 모든 자료형을 다 list에 관리할 수 있다.

list = [1, 2, 3.14, False, 'hello', [1, 2, 3]]
print (list)

# list에 요소를 추가해보자
list.append('world')
print(list)

# list에서 index 2번째 요소값을 가져와 출력
print(list[2]) # 3.14

print(list[5][1]) # 2 list안에 있는 list의 2번째 요소

# list에서 index 2번째 요소를 30으로 변경
list[5][2] = 30
print(list)

# list에서 index 4번째 요소를 삭제
del(list[4])
print(list)

# list에서 마지막 요소를 삭제
print(list.pop()) # 마지막 요소를 꺼낸 후 삭제
print(list)

# list를 오름차순으로 정리
list2 = [10, 8, 12, 16, 5]
list2.sort()
print(list2)

# 역순 정렬
list2.reverse()
print(list2)

# insert
list.insert(3, 'inserted') # 3번째 index에 'inserted' 추가
print(list)

# len -> list의 길이 반환
print(len(list))

# len을 이용하여 list2의 모든 값을 더해서 sum에 저장해보자
sum = 0

for i in range(len(list2)):
    sum += list2[i]

print(sum)


list2.append(10)
print(list2)

print(list2.count(10)) # list2에서 10의 갯수
print(list2.index(10)) 
print(list2.index(10, 3)) # list2에서 10이 3번째 index 이후에 나오는 index