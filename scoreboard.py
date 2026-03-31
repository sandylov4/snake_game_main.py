from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.goto(x=0, y=268)
        self.pencolor("white")
        self.speed("fastest")
        self.points = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.points} \n High Score: {self.high_score}", move=False, align='center', font=('Arial', 10, 'bold'))

    def reset_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 10, 'bold'))
        if self.points > self.high_score:
            self.high_score = self.points
            self.points = 0
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

    def add_point(self):
        self.points += 1
        self.show_score()
