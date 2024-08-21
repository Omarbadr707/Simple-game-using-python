import turtle
import time
import random

delay = 0.2
score = 0
high_score = 0

# screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=800, height=800)
window.tracer(0)

# set snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"
# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segments=[]


# pen 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Score: 0 High Score: 0",align = "center" , font=("Courier", 24, "normal"))
# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

#  Update score 
def update(score,high_score):
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score),align = "center" , font=("Courier", 24, "normal"))

# set up keyboard
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)



# main game loop
while True:
    window.update()

    #check collision of border 
    if head.xcor()>390 or head.xcor()<-390 or head.ycor()>390 or head.ycor()<-390:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        # hide segaments
        for segment in segments:
            segment.goto(1000,1000)

        #clear segments
        segments.clear()
        score = 0
        delay = 0.2
        update(score,high_score)

    if head.distance(food) < 20:
        x = random.randint(-390, 390)
        y = random.randint(-390, 390)
        food.goto(x, y)

    # Add segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)
        
        score += 10
        if delay > 0.06:
            delay -= 0.015
        if score > high_score:
            high_score = score
        update(score,high_score)
    # move segments append others
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    # move segments to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    #  check for head collision with segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            # hide segaments
            for segment in segments:
                segment.goto(1000,1000)

            #clear segments
            segments.clear()
            score = 0 
            delay = 0.2
            update(score, high_score)
    time.sleep(delay)


window.mainloop()