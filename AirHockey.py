import turtle as trt
import time
import tkinter as tk
import random as rd
import sys

t = trt.Turtle()
wn = trt.Screen()
wn.bgcolor("Gold")
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle 1
pad_a = trt.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.fillcolor("Green")
pad_a.shapesize(stretch_wid=5,stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)
score_a=0

#paddle 2
pad_b = trt.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.fillcolor("Red")
pad_b.shapesize(stretch_wid=5,stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)
score_b=0

#Ball
ball = trt.Turtle()
ball.shape("circle")
ball.color("White")
ball.goto(0,0)
ball.dx=4
ball.dy=4
ball.fillcolor('Blue')
ball.penup()

#pen
pen = trt.Turtle()
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0,280)
pen.write(f"Player A : {score_a}  Playe B : {score_b}",align="center")
#moveup_a
def pad_a_up():
    y = pad_a.ycor()
    y+=20
    pad_a.sety(y)
#movedown_a
def pad_a_down():
    y = pad_a.ycor()
    y-=20
    pad_a.sety(y)
    
#moveup_b
def pad_b_up():
    y = pad_b.ycor()
    y+=20
    pad_b.sety(y)
#movedown_b
def pad_b_down():
    y = pad_b.ycor()
    y-=20
    pad_b.sety(y)
    
#Keyboard Binding
wn.listen()
wn.onkeypress(pad_a_up,"w")
wn.onkeypress(pad_a_down,"s")
wn.onkeypress(pad_b_up,"Up")
wn.onkeypress(pad_b_down,"Down")

def random_side_spawn():
    side = rd.randint(1,2)
    pen.clear()
    pad_a.goto(-350,0)
    pad_b.goto(350,0)
    return side


while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() > 290:
        ball.dy*=-1
        
    if ball.ycor() < -290:
        ball.dy*=-1
        
    if ball.xcor() > 350:
        score_a+=1
        side = random_side_spawn()
        if(side==1):
            ball.goto(290,0)
        else:
            ball.goto(-290,0)
        time.sleep(1)
        ball.dy*=-1
        pen.clear()
        pen.write(f"Player A : {score_a}  Playe B : {score_b}",align="center",font=(24))
        
    if ball.xcor() < -350:
        score_b+=1
        side = random_side_spawn()
        if(side==1):
            ball.goto(290,0)
        else:
            ball.goto(-290,0)
        time.sleep(1)
        ball.dy*=-1
        pen.clear()
        pen.write(f"Player A : {score_a}  Playe B : {score_b}",align="center",font=(24))
        
    if ball.xcor() > 335 and ball.xcor() < 350 and ball.ycor() > pad_b.ycor() - 60 and ball.ycor() < pad_b.ycor() + 60:
        ball.dx*=-1
    if ball.xcor() < -335 and ball.xcor() > -350 and ball.ycor() < pad_a.ycor() + 60 and ball.ycor() > pad_a.ycor() -60:
        ball.dx*=-1
        
    if score_a == 4:
        pen.clear()
        pen.setposition(0,0)
        pen.write("A Wins",align='center',font=('Arial',30,'normal'),move=True)
        time.sleep(2)
        tk.mainloop()
        trt.Screen().bye()
        
    elif score_b == 4:
        pen.clear()
        pen.setposition(0,0)
        pen.write("B Wins",align='center',font=('Arial',30,'normal'),move=True)
        time.sleep(2)
        tk.mainloop()
        trt.Screen().bye()
