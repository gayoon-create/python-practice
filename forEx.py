# for 문

# for 변수 in range(시작값, 끝값, 증가감값) :         -> 증가감값을 생략하면 1로 간주
#     반복 수행할 코드 

# 구구단의 단을 입력받아 해당 단의 구구단을 출력

# num = int(input("숫자 입력 >>"))

# print("num : %d" % num)

# for i in range(1, 10) :
#     print("%d * %d = %d" % (num, i, num * i))

# 구구단 1단~9단까지 전체 출력하는 프로그램을 이중 for문으로 작성

# for i in range(1, 10) :
#     for num in range(1, 10) :
#         print("%d * %d = %d" % (i, num, i * num), end="  ")
#     print() # 줄바꿈



# while문으로 구구단의 단을 입력받아 해당 단의 구구단을 출력
# num = int(input("숫자 입력 >>"))
# i = 1
# while i < 10 :
#     print("%d * %d = %d" % (num, i, num * i))
#     i += 1


# 자매품 continue, break도 자바와 똑같다.