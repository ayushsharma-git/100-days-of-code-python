from turtle import Turtle, Screen

import pandas as pd

IMAGE = "blank_states_img.gif"
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')

screen = Screen()
screen.addshape(IMAGE)
turtle = Turtle(shape=IMAGE)
turtle_score = Turtle()
turtle_score.penup()
turtle_score.hideturtle()

game_is_on = True
title = "Guess the state"
prompt = "What's another state name?"
score = 0
states = pd.read_csv("50_states.csv")
# print(states.head())
while game_is_on:
    answer_state = screen.textinput(title=title, prompt=prompt).title()
    state = states[states["state"] == answer_state]

    if not state.empty:
        print(state.empty)
        score += 1
        turtle_score.goto(x=state.iloc[0, 1], y=state.iloc[0, 2])
        turtle_score.write(state.iloc[0, 0], align=ALIGNMENT, font=FONT)

        title = f"{score}/50 state guessed"
        if score == 50:
            game_is_on = False
screen.exitonclick()
