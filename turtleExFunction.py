# 아래의 기능을 가진 프로그램을 함수를 이용하여 만들어보자
# 마우스 왼쪽 버튼을 누르며 거북이가 클릭한 지점까지 임의의 색상으로 선을 그리면서 이동하도록 한다.
# 마우스 오른쪽 버튼을 누르면 거북이가 클릭한 지점까지 선을 그리지 않고 이동만 하도록 한다.
# 마우스 가운데 버튼을 누르면 거북이가 임의의 크기만큼 확대 또는 축소되도록 한다.

import turtle
import random

def screenLeftClick(x, y) :
    print(x, ",", y)
    global r, g, b # r, g, b를 전역변수로 선언
    turtle.pencolor((r, g, b)) # pencolor() 함수로 pen color를 변경
    turtle.pendown() 
    turtle.goto(x, y) # x, y 지점으로 이동

def screenRightClick(x, y) : 
    print(x, ",", y)
    turtle.penup()
    turtle.goto(x, y)

def screenMiddleClick(x, y) :
    print(x, ",", y)
    turtleSize = random.randrange(0, 10)
    turtle.shapesize(turtleSize)
    global r, g, b # r, g, b를 전역변수로 선언
    r = random.random()
    g = random.random()
    b = random.random()


penSize = 10 # 기본 pen size
r, g, b = 0.0, 0.0, 0.0 # 기본 RGB color

turtle.title("꼬북이 드로잉")

turtle.shape("turtle")
turtle.pensize(penSize)

turtle.onscreenclick(screenLeftClick, 1) # = 스크린 영역에서 왼쪽 마우스 버튼을 클릭하면
turtle.onscreenclick(screenRightClick, 3)
turtle.onscreenclick(screenMiddleClick, 2)

turtle.done()