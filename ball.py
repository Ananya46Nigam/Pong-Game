from turtle import Turtle


from turtle import Turtle


class Ball(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.goto(position)
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1
        
    def move_ball(self):
         new_x=self.xcor()+self.xmove
         new_y=self.ycor()+self.ymove
         self.goto(new_x,new_y)
            
             
    def bouncy(self):
        self.ymove*=-1
        
        
    def bouncx(self):
        self.xmove*=-1
        self.move_speed*= 0.5
        
    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bouncx()
