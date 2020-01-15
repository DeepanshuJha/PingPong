import turtle                               #importing turtle module
import winsound

wn = turtle.Screen()                        #create a screen
wn.title("Ping Pong By @DeepanshuJha")      #give title to frame
wn.bgcolor("#ff8000")                       #give color to frame
wn.setup(width=800, height=600)             #give frame width and height
wn.tracer(0)                                #stops window from updating

# Score

score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()                  #create a turtle object
paddle_a.speed(0)                           #max possible speed for animation
paddle_a.shape("square")                    #choosing shape of object
paddle_a.color("white")                     #choosing color
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #strecthing the length by 5 (vertical)
paddle_a.penup()                            
paddle_a.goto(-350, 0)                      #giving it a position on window center is (0, 0)

# Paddle B
paddle_b = turtle.Turtle()                  #create a turtle object for ball
paddle_b.speed(0)                          
paddle_b.shape("square")                    
paddle_b.color("white")                     
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup()                            
paddle_b.goto(350, 0)                       

# Ball
ball = turtle.Turtle()                      #create a turtle object for ball
ball.speed(0)                         
ball.shape("square")                  
ball.color("white")                     
ball.penup()                            
ball.goto(0, 0)                   
ball.dx = 0.2                               #speed of ball movement in x
ball.dy = 0.2                              #speed of ball movement in y                     


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 20, "bold"))

# Function for moving paddle up and down
def paddle_a_up():
    y = paddle_a.ycor()                     #gives the y coordinate of paddle a
    if y <= 220:
        y += 20                                 # add 20 to it so that it moves by 20 up
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y >= -220:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()                     
    if y <= 220:
        y += 20                                
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y >= -220:
        y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()                                 #listens for keyboard input
# Paddle A control
wn.onkeypress(paddle_a_up, "w")             #binding paddle_a_up() function with "w" key
wn.onkeypress(paddle_a_down, "s")           #binding down() function with "d" key

# Paddle B control
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game loop
while True:
    wn.update()                             #always update window
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1                       # invert the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))

    # Paddle and ball Collision

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)