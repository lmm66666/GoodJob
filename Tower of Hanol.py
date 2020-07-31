import turtle as t
import time

A_pole = []
B_pole = []
C_pole = []


def hanoi(n, a_pole, b_pole, c_pole):
    if n == 1:
        draw()
        c_pole.insert(0, a_pole[0])
        del a_pole[0]
        return
    else:
        hanoi(n-1, a_pole, c_pole, b_pole)
        hanoi(1, a_pole, b_pole, c_pole)
        hanoi(n-1, b_pole, a_pole, c_pole)


def draw():
    t.clear()
    # 画柱子
    t.seth(0)
    t.pen(shown=False, pencolor='black', pensize=10, speed=0)
    t.penup()
    t.goto(-400, -200)
    t.pendown()
    t.forward(800)
    t.penup()
    t.seth(90)
    for k in range(1, 4):
        t.goto(-400 + k * 200, -200)
        t.pendown()
        t.forward(500)
        t.penup()
    # 画圈圈
    t.pen(shown=False, pencolor='red', pensize=4, speed=0)
    height = 40
    max_len = 100
    step = 15
    # A
    length = len(A_pole)
    for k in range(length):
        x = -200 - max_len + step * A_pole[-k-1]
        y = -200 + height * k
        t.goto(x, y)
        t.pendown()
        t.seth(90)
        t.forward(height)
        t.seth(0)
        t.forward(2*(max_len - step * A_pole[-k-1]))
        t.seth(270)
        t.forward(height)
        t.penup()
    # B
    length = len(B_pole)
    for k in range(length):
        x = -max_len + step * B_pole[-k-1]
        y = -200 + height * k
        t.goto(x, y)
        t.pendown()
        t.seth(90)
        t.forward(height)
        t.seth(0)
        t.forward(2 * (max_len - step * B_pole[-k-1]))
        t.seth(270)
        t.forward(height)
        t.penup()
    # C
    length = len(C_pole)
    for k in range(length):
        x = 200 - max_len + step * C_pole[-k-1]
        y = -200 + height * k
        t.goto(x, y)
        t.pendown()
        t.seth(90)
        t.forward(height)
        t.seth(0)
        t.forward(2 * (max_len - step * C_pole[-k-1]))
        t.seth(270)
        t.forward(height)
        t.penup()
    time.sleep(1)


# 输入初始化
while 1:
    n = int(input('请输入汉诺塔的层数\n'))
    if 0 < n < 7:
        break
    else:
        print('输入数字太大或输入负数，请重试！')
for i in range(n):
    A_pole.append(n-i)
# 画布初始化
t.screensize(400, 300, "white")
# 汉诺塔
hanoi(n, A_pole, B_pole, C_pole)
draw()
time.sleep(5)
print(A_pole, B_pole, C_pole)