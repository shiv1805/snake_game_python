import turtle
import time
import random

delay=0.1

#score---------------------------------------------------------------------
score=0
high_score=0

wn=turtle.Screen()
wn.title("Snake game by @shiv choudhary")
wn.bgcolor("pink")
wn.setup(width=800, height=800)
wn.tracer(0)

# snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#snake body
segments=[]

#pen-----------------------------------------------------------------------
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,360)
pen.write("Score: 0 High Score: 0",align="center",font=("Courier",24,"normal"))


#functions

def go_up():
    if head.direction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":
        head.direction="down"
def go_left():
    if head.direction !="right":
        head.direction="left"
def go_right():
    if head.direction !="left":
        head.direction="right"
    

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
        
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
        
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#keyboard binding

wn.listen()
wn.onkey(go_up,"Up")
wn.onkey(go_down,"Down")
wn.onkey(go_left,"Left")
wn.onkey(go_right,"Right")

        
    
# main gameloop
while True:
    wn.update()

    #check for collision with border
    if head.xcor()>390 or head.xcor()< -390 or head.ycor()>390 or head.ycor()< -390:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

    #hide the segment
        for segment in segments:
            segment.goto(1000,1000)

    #clear the segment
        segments.clear()

    #reset the score----------------------------------------------------------
        score=0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score), align="center",font=("Courier",24,"normal"))
        


    #check for collision with food
    if head.distance(food)<20: #move food to random spot
        x=random.randint(-380,380)
        y=random.randint(-380,380)
        food.goto(x,y)

        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        

      #increase the score--------------------------------------------------------
        score+=10

        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score), align="center",font=("Courier",24,"normal"))   


    #move the end segment 1st in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
        

    move()

    #check for  head collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
            for segment in segments:
                segment.goto(1000,1000)
                
            segments.clear()

            #reset the score--------------------------------------------------
            score=0

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,high_score), align="center",font=("Courier",24,"normal"))
            
    time.sleep(delay)

wn.mainloop()
