import turtle
t = turtle.Turtle()
n = int(input("한변의 길이는?"))
t.circle(n)
t.penup()
t.forward(n)
t.left(90)
t.pendown()
t.forward(2*n)
t.left(90)
t.forward(2*n)
t.left(90)
t.forward(2*n)
t.left(90)
t.forward(2*n)