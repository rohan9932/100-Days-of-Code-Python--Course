from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # adds the image as a shape
screen.setup(725,491)

turtle = Turtle()
turtle.shape(image)

# Data Processing
states_data = pd.read_csv("50_states.csv")
all_states = states_data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states] # list comprehension
        data = pd.DataFrame(missing_states)
        data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        # move the name of the state to the location
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
