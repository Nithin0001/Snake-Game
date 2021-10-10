from turtle import Turtle
ALIGN = "center"
FONT = ("Poppins", 24, "bold")
FONT_GAME_OVER = ("Poppins", 50, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 330)
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGN, font=FONT_GAME_OVER)
        self.goto(0, -50)
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)
        self.score = 0
