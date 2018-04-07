import random

# The Prisoner has some basic accessors and different methods to
# Manipulate the decisions in order to test an array of behaviors


class Prisoner:
    def __init__(self, behavior_num):
        self.__morality = None
        self.__decision = None  # 0 he's silent 1 he talks
        self.__prev_decision = None
        self.__year_in_jail = 0
        self.__total_years_in_jail = 0
        self.__total_years_talk = 0
        self.__total_years_silent = 0
        self.__years_talk_group = 0
        self.__years_silent_group = 0
        self.__num_test = 0
        self.__num_talk = 1  # starts at one to simplify calcs
        self.__num_silent = 1  # starts at one to simplify calcs
        self.__behavior_num = behavior_num  # Number between 0 and n. This number should not change.

    # First some accessors
    # returns the morality of prisoner
    def get_morality(self):
        return self.__morality

    # returns the decision of prisoner
    # When you get the decision you set the previous decision to your current one.
    def get_decision(self):
        # This updates the number of each decision
        if self.__decision == 0:
            self.__num_silent += 1
        if self.__decision == 1:
            self.__num_talk += 1
        # Update the number of test as a whole.
        self.__num_test += 1
        self.__prev_decision = self.__decision
        return self.__decision

    # returns the previous decision of prisoner
    def get_prev_decision(self):
        return self.__prev_decision

    # returns the years in set to jail "This round"
    def get_years(self):
        return self.__year_in_jail

    # returns the total years in jail "Up to the nth experiment"
    def get_total_years(self):
        return self.__total_years_in_jail

    # returns the number of years done while talking.
    def get_years_talk(self):
        return self.__total_years_talk

    # returns the number of years done while silent
    def get_years_silent(self):
        return self.__total_years_silent

    # This sets the morality based on how you would like to.
    # This is used for some types of behavior
    # I expect a Number n such that 0 <= n <= 1
    # Higher means higher sense of "Personal code" lower means less
    def set_morality(self, moral_num):
        self.__morality = moral_num

    # Sets a morality that is random based on some behaviors
    def set_rand_morality(self):
        self.__morality = random.random()

    # Sets the decision based on the behavior type.
    def set_decision(self):
        if self.__behavior_num == 0:
            self.__decision = self.__get_decision_0()
        if self.__behavior_num == 1:
            self.__decision = self.__get_decision_1()
        if self.__behavior_num == 2:
            self.__decision = self.__get_decision_2()
        if self.__behavior_num == 3:
            self.__decision = self.__get_decision_3()
        if self.__behavior_num == 4:
            self.__decision = self.__get_decision_4()
        if self.__behavior_num == 5:
            self.__decision = self.__get_decision_5()
        if self.__behavior_num == 6:
            self.__decision = self.__get_decision_6()
        if self.__behavior_num == 7:
            self.__decision = self.__get_decision_7()
        if self.__behavior_num == 8:
            self.__decision = self.__get_decision_8()

    # This here to set the number of years for a current round.
    # This also increase the total number of years spent in jail.
    def set_years(self, num_years):
        self.__year_in_jail = num_years
        self.__total_years_in_jail += num_years
        # After establishing the basic years for this round and total years altogether,
        # It then determines the number of years per answer choice.
        if self.__decision == 0:
            self.__total_years_silent += num_years
        else:
            self.__total_years_talk += num_years

    # This method requires information from the other prisoner. The idea is to keep track of the total outcome of the
    # group over time. Therefore we need to have self and the other accounted for and see what all they have done.
    def set_group_years(self, other):
        if self.__prev_decision == 0:
            self.__years_silent_group += self.__year_in_jail + other.get_years()
        else:
            self.__years_talk_group += self.__year_in_jail + other.get_years()

    # This is a helper method for the set_decision method. returns the appropriate decision
    # Behavior 0 is completely random
    def __get_decision_0(self):
        rand = random.random()
        if rand >= .5:
            return 0  # he doesn't rat out
        else:
            return 1  # he does rat out

    # This is a helper method for the set_decision method. returns the appropriate decision
    # Behavior 1 is random the first time, then flips every time there after.
    def __get_decision_1(self):
        if self.__prev_decision is None:
            return self.__get_decision_0()
        if self.__prev_decision == 0:
            return 1
        if self.__prev_decision == 1:
            return 0

    # This is a helper method for the set_decision method. returns the appropriate decision
    # Behavior 2 goes off the total number of years in jail for each decision and try's to make the "Best Choice"
    # by which it chooses the option which has resulted in the fewest years for themselves
    def __get_decision_2(self):
        if self.__total_years_silent == self.__total_years_talk:
            return self.__get_decision_0()  # Random behavior when equal.
        else:
            num_talk_ratio = self.__total_years_talk / self.__num_talk
            num_silent_ratio = self.__total_years_silent / self.__num_silent
            if num_silent_ratio <= num_talk_ratio:
                return 0  # The advantage of staying silent appears to be best for myself.
            else:
                return 1  # The advantage of talking appears to be best for the myself.

    # This is a helper method for the set_decision method. returns the appropriate decision
    # Behavior 3 is based completely on moral. If moral is higher he will be more likely to stay silent.
    def __get_decision_3(self):
        if self.__morality is None:
            self.set_rand_morality()
        if self.__morality >= .5:
            return 0
        else:
            return 1

    # This is a helper method for the set_decision method. returns the appropriate decision
    # Behavior 4 is all about trying to get the best outcome for the group as a whole.
    # I expect that as the test tends to go on it should quickly converge into both remaining silent.
    def __get_decision_4(self):
        if self.__num_test == 0:
            return self.__get_decision_0()  # Random behavior until both options have been tried.
        else:
            num_talk_ratio = self.__years_talk_group / self.__num_talk
            num_silent_ratio = self.__years_silent_group / self.__num_silent
            if num_silent_ratio <= num_talk_ratio:
                return 0  # The advantage of staying silent appears to be best for group.
            else:
                return 1  # The advantage of talking appears to be best for the group.

    # Behavior 5, always silent
    def __get_decision_5(self):
        return 0

    # Behavior 6, always talks
    def __get_decision_6(self):
        return 1

    # Behavior 7 a mixture of the head knowledge and the moral aspect.
    def __get_decision_7(self):
        if self.__num_test == 0:
            return self.__get_decision_0()
        else:
            self.__morality = random.random()
            head_decision = self.__get_decision_2()
            if head_decision == 0:
                result = 1 - self.__morality
            else:
                result = head_decision - self.__morality
            if result >= .5:
                return 0
            else:
                return 1

    def __get_decision_8(self):
        x = input("Input '0' for Silence, or '1' to Talk. (No space please.)", )
        if x == '0':
            return 0
        if x == '1':
            return 1
        else:
            print("I'm sorry,", x, "is not a valid input. Please input a valid value.")
            print("")
            return self.__get_decision_8()
