# Let's create a fun snake game!
import turtle
import time
import random

# Set initial configurations
delay = 0.1
score = 0
high_score = 0

# Set up the game window
screen = turtle.Screen()
screen.title("My Snake Game")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the snake's head
head = turtle.Turtle()
head.shape("square")
head.color("darkgreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create the food for the snake
food = turtle.Turtle()
food_shape = random.choice(['circle', 'square', 'triangle'])
food_color = random.choice(['red', 'blue', 'orange'])
food.shape(food_shape)
food.color(food_color)
food.penup()
food.goto(0, 100)

# Create the score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "normal"))

# Functions to move the snake
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

# Assign key bindings
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

segments = []

# Main gameplay loop

while True:
    screen.update()

    # Move the snake
    if head.direction != "stop":
        # Update the position of the snake's head based on its direction
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        elif head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        elif head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        elif head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    # Check for collision with wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        # Reset the game if the snake hits the wall
        # Your collision handling code here
        pass

    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a random position if the snake eats it
        # Your food collision handling code here
        pass

    # Check for collision with own body
    for segment in segments:
        if segment.distance(head) < 20:
            # Reset the game if the snake collides with itself
            # Your body collision handling code here
            pass

    time.sleep(delay)




screen.mainloop()
