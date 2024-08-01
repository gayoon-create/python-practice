# Dictionary : key-value 쌍으로 이루어진 unordered collection. 자바에서의 Map 인터페이스와 유사

# 키의 값은 중복(overwrite)을 허용하지 않으며, value값은 중복을 허용한다.

# list : []
# tuple : ()
# dict : {}

# 딕셔너리 생성
dict1 = {'apple' : '사과', 'banana' : '바나나', 'cherry' : '체리', 'orange' : '오렌지'}

print(dict1)

# key로 value를 얻어오기
print(dict1['cherry'])

# key를 중복해서 넣는다면? 같은 key를 넣으면 해당 key에 대한 value가 overwrite 된다.
dict1['apple'] = '애플회사'
print(dict1)

# value값은 중복 가능
dict1['버낸아'] = '바나나'
print(dict1)

# dictionary에서 모든 key를 가져오기
keys = list(dict1.keys()) # dict.keys() : dict의 키들을 set이라는 자료구조로 변환하는데 -> list로 변환
print(keys)

# dictionary에서 모든 value를 가져오기
values = list(dict1.values()) # dict.values() : dict의 value들을 list로 변환
print(values)

# dict1의 키와 value를 tuple 형태로 반환시키기
print(list(dict1.items()))

# 해당 dictionary에 key가 존재한다면 그 값을 얻어오기
if 'apple' in dict1 :
    print(dict1['apple'])
else : 
    print('없음')

if 'bus' in dict1 :
    print(dict1['bus'])
else : 
    print('없음')


