import turtle
import pandas

screen = turtle.Screen()
screen.title("US. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":

        # set1 = set(all_states)
        # set2 = set(guessed_states)
        # left_states = list(set1.symmetric_difference(set2))
        left_states = [state for state in all_states if state not in guessed_states]
        left_data = pandas.DataFrame(left_states)
        left_data.to_csv("left_states.csv")
        print(f"You missing {len(left_states)}.")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
#
# left_states = all_states - guessed_states
# df = pandas.DataFrame(left_states)
# df.to_csv("left_states.csv")
