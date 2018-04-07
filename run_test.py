import Prisoner
# These are the "Class Variables" that store the appropriate responses for certain values,
# to make the code more readable.
silent = 0
talk = 1
# These are variables for the options in behavior.
random = 0  # complete random behavior
flip_flop = 1  # switches every time
best_for_self = 2  # chooses what outcome they have had the most relative success with
morals = 3  # chooses strictly off moral principle
best_for_group = 4  # chooses the solution that seems to get the least number of years for the group as a whole.
always_silent = 5  # always silent
always_talks = 6  # always talks
whim_vs_knowledge = 7  # uses the learned knowledge of what the best option would be to benefit himself,
# but has the decision weighed against the right choice of not selling out his partner in the moment.
human_control = 8  # A person can play vs any CPU or another player depending on the behavior of the other prisoner.


def prisoners_dilemma(p1, p2):

    p1_decision = p1.get_decision()
    p2_decision = p2.get_decision()
    # Both Rat out the other.
    if (p1_decision == talk) and (p2_decision == talk):
        p1.set_years(2)
        p2.set_years(2)

    # Prisoner 1 rats Prisoner 2 is silent
    if (p1_decision == talk) and (p2_decision == silent):
        p1.set_years(0)
        p2.set_years(3)

    # Prisoner 1 is silent Prisoner 2 rats
    if (p1_decision == silent) and (p2_decision == talk):
        p1.set_years(3)
        p2.set_years(0)

    # Both remain Silent
    if(p1_decision == silent) and (p2_decision == silent):
        p1.set_years(1)
        p2.set_years(1)

    # Update the years as group.
    p1.set_group_years(p2)
    p2.set_group_years(p1)


def start_round_text():

    print("Welcome to 'The Prisoner Dilemma!'")
    print()
    print("Please input the type of behavior you would like for Prisoner 1.")
    print(options())
    p1_string = input("What behavior would you like to use? (No space please): ")
    p1_x = convert_int(p1_string)
    p1_behav = check_val(p1_x)
    res = [p1_behav]
    if p1_behav == 9:
        return res
    else:
        print()
        print("Please input the type of behavior you would like for Prisoner 2.")
        p2_string = input("What behavior would you like to use? (No space please): ")
        p2_x = convert_int(p2_string)
        p2_behav = check_val(p2_x)
        res.append(p2_behav)
        return res


def options():
    print("Options:")
    print("Input 0 for 'Random' behavior")
    print("Input 1 for 'Flip - Flop' behavior")
    print("Input 2 for 'Best Choice' behavior")
    print("Input 3 for 'Moral' behavior")
    print("Input 4 for 'Best For Group' behavior")
    print("Input 5 for 'Always Silent' behavior")
    print("Input 6 for 'Always Talk' behavior")
    print("Input 7 for 'Whim vs Knowledge' behavior")
    print("Input 8 for 'Human Control'")
    print("Input 9 for default player settings.")
    print()


def convert_int(str1):
    try:
        val = int(str1)
    except ValueError:
        print("I'm sorry,", str1, "is not an int value.")
        print("")
        str2 = input("Please enter an appropriate int value: ")
        return convert_int(str2)
    return val


def check_val(val):
    if val >= 0 or val <= 9:
        return val
    else:
        print("I'm sorry,", val, "is not a valid value.")
        print("")
        str_here = input("Please enter a valid value between 0-9: ")
        x_here = convert_int(str_here)
        return check_val(x_here)


res_list = start_round_text()
if res_list[0] == 9:
    prisoner1 = Prisoner.Prisoner(random)
    prisoner2 = Prisoner.Prisoner(best_for_self)
else:
    prisoner1 = Prisoner.Prisoner(res_list[0])
    prisoner2 = Prisoner.Prisoner(res_list[1])


for x in range(100):
    prisoner1.set_decision()
    prisoner2.set_decision()
    prisoners_dilemma(prisoner1, prisoner2)
    p1_round_decision = prisoner1.get_prev_decision()
    if p1_round_decision == 1:
        p1_round_decision = "Talked"
    else:
        p1_round_decision = "Silent"
    p2_round_decision = prisoner2.get_prev_decision()
    if p2_round_decision == 1:
        p2_round_decision = "Talked"
    else:
        p2_round_decision = "Silent"
    print("")
    print("Prisoner 1 Decision: ", p1_round_decision, "Prisoner 2 Decision: ", p2_round_decision)
    print("Prisoner 1 total years: ", prisoner1.get_total_years(), "Prisoner 2 total years: ", prisoner2.get_total_years())
