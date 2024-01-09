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
states_list = states["state"].to_list()
guessed_states = []
# print(states.head())
while game_is_on:
    answer_state = screen.textinput(title=title, prompt=prompt).title()
    if answer_state.title() == "Exit":
        missing_states = [missing_state for missing_state in states_list if missing_state not in guessed_states]
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("missing_states.csv")
        game_is_on = False

    state = states[states["state"] == answer_state]
    if not state.empty:
        score += 1
        turtle_score.goto(x=state.iloc[0, 1], y=state.iloc[0, 2])
        turtle_score.write(state.iloc[0, 0], align=ALIGNMENT, font=FONT)
        guessed_states.append(answer_state.title())
        title = f"{score}/50 state guessed"
        if score == 50:
            game_is_on = False
screen.exitonclick()
