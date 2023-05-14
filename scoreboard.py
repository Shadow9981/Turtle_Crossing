from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.update_level()

    def game_over(self, dead):
        if dead:
            self.goto(0, 0)
            self.write(arg="GAME OVER", align="center", font=FONT)

    def update_level(self):
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()
