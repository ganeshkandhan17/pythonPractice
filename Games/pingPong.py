import turtle

window = turtle.Screen()

window.screensize(500,500)
window.bgcolor('blue')
window.title('Ping pong game')
window.tracer(0)

scoreA = 0 
scoreB = 0

# padding
pdy=35

# Left pad
leftPad = turtle.Turtle()
leftPad.penup()
leftPad.shape(name='square')
leftPad.shapesize(stretch_len=0.5,  stretch_wid=3)
leftPad.color('white')
leftPad.goto(-330,0)

# Right pad
rightPad = turtle.Turtle()
rightPad.penup()
rightPad.shape(name='square')
rightPad.shapesize(stretch_len=0.5,  stretch_wid=3)
rightPad.color('white')
rightPad.goto(325,0)

# Ball
ball = turtle.Turtle()
ball.shape(name='circle')
ball.color('white')
ball.shapesize(1,1,1)
ball.penup()
dx=0.3
dy=0.3

# Pen
pen= turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color('white')
pen.goto(0,250)
pen.write('Player A = {}, Player B = {}'.format(scoreA, scoreB),align='center',font='(arial,10)')

window.listen()
window.onkeypress(lambda : leftPad.sety(leftPad.ycor() if leftPad.ycor()>220 else leftPad.ycor()+pdy), 'w')
window.onkeypress(lambda : leftPad.sety(leftPad.ycor() if leftPad.ycor()<-220 else leftPad.ycor()-pdy), 's')

window.onkeypress(lambda : rightPad.sety(rightPad.ycor() if rightPad.ycor()>220 else rightPad.ycor()+pdy), 'Up')
window.onkeypress(lambda : rightPad.sety(rightPad.ycor() if rightPad.ycor()<-220 else rightPad.ycor()-pdy), 'Down')

printed = False

def printOnce(string):
    global printed
    if printed : 
        return 0
    print(string)
    printed=True



while True:
    window.update()
    ball.sety(ball.ycor()+dy)
    ball.setx(ball.xcor()+dx)
    
    # If it hit the right wall
    if(ball.xcor() > 320):        
        dx=dx*-1

    # If ball hit the top  wall
    if(ball.ycor()>270):
        dy*=-1

    # If the ball hit the left wall
    if(ball.xcor() <- 330):
        dx=dx*-1

    # If the ball hit the down wall
    if(ball.ycor() <-270):
        dy*=-1    

    # If ball hit the right pad
    if(ball.xcor()>310 and ball.ycor() < rightPad.ycor() + 50 and ball.ycor() > rightPad.ycor() -50):        
        printOnce(f'!!!!Hit right pad!!!\nball: {ball.xcor(), ball.ycor()}\nright padding : {rightPad.ycor()}')
        dx*=-1 

    # Else if ball hit the right wall
    elif(ball.xcor()>320 and not (ball.ycor() < rightPad.ycor() + 50 and ball.ycor() > rightPad.ycor() -50)):
        scoreB+=1
        pen.clear()
        pen.write('Player A = {}, Player B = {}'.format(scoreA, scoreB),align='center',font='(arial,10)')
        print('hit the right wall')        
        printed=False
        ball.goto(0,0)

    # If ball hit left pad
    if(ball.xcor()<-310 and ball.ycor() < leftPad.ycor() + 50 and ball.ycor() > leftPad.ycor() -50):        
        printOnce(f'!!!!Hit left pad!!!\nball: {ball.xcor(), ball.ycor()}\nleft padding : {leftPad.ycor()}')
        dx*=-1 

    # If ball hit left wall
    elif(ball.xcor()<-320 and not (ball.ycor() < leftPad.ycor() + 50 and ball.ycor() > leftPad.ycor() -50)):
        scoreA+=1
        pen.clear()
        pen.write('Player A = {}, Player B = {}'.format(scoreA, scoreB),align='center',font='(arial,10)')
        print('hit the left wall')        
        printed=False
        ball.goto(0,0)

