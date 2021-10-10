import numpy as np
import random

'''
[forward, backward, left, right, stay]
'''
class Simulator:
    def __init__(self, MDP, cur_state):
        global action_prob
        global current_state
        global statespace
        global actionset
        global wind
        global observ

        statespace = MDP.state
        actionset = MDP.action
        wind = MDP.wind
        observ = MDP.observation
        action_prob = MDP.prob_action
        current_state = cur_state

        self.successor_state_given_state = MDP.prob_ss
        self.transit_prob = self.transistion_probability

    def pick_action(self):
        #when no policy involved
        i = random.randint(0,4)
        return actionset[i]

