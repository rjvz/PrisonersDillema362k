import Prisoner
silent = 0
talk = 1


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


prisoner1 = Prisoner.Prisoner(3)
prisoner2 = Prisoner.Prisoner(2)


for x in range(100):
    prisoners_dilemma(prisoner1, prisoner2)
    prisoner1.set_decision()
    prisoner2.set_decision()
    print("Prisoner 1 spent: ", prisoner1.get_years(), "Prisoner 2 spent: ", prisoner2.get_years())
    print("Prisoner 1 total years: ", prisoner1.get_total_years(), "Prisoner 2 total years: ", prisoner2.get_total_years())
