import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=player.turtle_move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_car()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over(True)
            game_is_on = False

    if player.ycor() > 280:
        player.turtle_restart()
        scoreboard.increase_level()
        car_manager.increment_speed()

screen.exitonclick()
