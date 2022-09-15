import turtle
from label import Label
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_data = data.state.to_list()

correct_states_guessed = []

while len(correct_states_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states_guessed)}/50 States Correct.", prompt="What's another state").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_data if state not in correct_states_guessed]
        # missing_states = []
        # for state in state_data:
        #     if state not in correct_states_guessed:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_data:
        correct_states_guessed.append(answer_state)
        state_row = data[data.state == answer_state]
        Label(answer_state, int(state_row.x), int( state_row.y))
