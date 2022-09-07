from turtle import Turtle,Screen,time
from paddle import Paddle
from ball import Ball
from score import ScoreBoard


screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("PONG GAME")

paddle_right=Paddle((350,0))
paddle_left=Paddle((-350,0))

ball=Ball((0,0))
    
    
    
screen.listen()
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")
screen.onkey(paddle_left.go_up,"a")
screen.onkey(paddle_left.go_down,"z")
screen.onkey(ball.move_ball,"m")

score = ScoreBoard()


game_is_on=True

while game_is_on and score.l_score<10 and score.r_score<10:
    time.sleep(0.1)
    screen.update()
    ball.penup()
    ball.move_ball()
    
    if ball.ycor()>288 or ball.ycor()<-288:
        ball.penup()
        ball.bouncy()
        
    if ((ball.distance(paddle_right))<50 and (ball.xcor())>317) or ((ball.distance(paddle_left))<40 and ((ball.xcor())<-317)) :
        print("Made contact successfully")
        ball.bouncx()
        
        
    if ball.xcor()>380:
        ball.reset_pos()
        score.l_point()
        
    if ball.xcor()<-380:
        ball.reset_pos()
        score.r_point()
        

if score.l_score()>score.r_score():
    print("Left player player won the Game !")
    
elif score.l_score()<score.r_score():
    print("Right player won the Game")
    
else:
    print("Draw -_- ")

screen.exitonclick()