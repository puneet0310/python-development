from turtle import Turtle
class Score(Turtle):
    score=0
    def __init__(self) :
        super().__init__()
        self.score=0
        self.color("White")
        self.penup()
        self.goto(0,270)
        
        self.hideturtle()
        self.update_scorebard()
    def update_scorebard(self):
        self.write(f"Score:{self.score}",align="center",font=("Arial", 24, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial", 60, "normal"))
    
    def inc_score(self):
        self.score =+1
        self.clear()
        self.update_scorebard()
        

        
        

    
    