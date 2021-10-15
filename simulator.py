import numpy as np
import random


class Simulator:
    def __init__(self, MDP):

        self.statespace = MDP.stateSpace
        self.actionset = MDP.actionSpace
        self.wind = MDP.wind
        self.observ = MDP.observation
        self.current_state = MDP.current_position
        self.transit_prob = MDP.transition_probability

        self.new_state = self.update_state

    #删了，只是让print out的结果看得更清楚
    #ignore this function, need to be deleted 
    def get_action_name(self,index):
        if index == 0: 
            action_name = "Up"
        elif index == 1:
            action_name = "Down"
        elif index == 2:
            action_name = "left"
        elif index == 3:
            action_name = "right"
        elif index == 4:
            action_name = "stay"
        return action_name




    #后期应该会是，两个inputs： 1.current state 2.action
    @property
    def update_state(self):
        action_index = random.randint(0,4)#改,目前只是让它跑起来，action之后得由policy决定
        prob_given_action = self.transit_prob[action_index] #25*25
        for i in range(len(self.statespace)):
            #inital current state should never be in block state in theory
            #initial current state should always within the statespace in theory
            if np.array_equal(self.current_state, self.statespace[i]):
                prob_given_action_state = prob_given_action[i] #1*25
                max_prob = np.amax(prob_given_action_state)
                max_index = np.argmax(prob_given_action_state)
                if random.random() < max_prob:
                    print("The action picked is: " + self.get_action_name(action_index)) #TBD
                    print("The action is executed correctly")
                    print("The new state is now: ", self.statespace[max_index])
                    return self.statespace[max_index]
                else:
                    print("The action picked is: " + self.get_action_name(action_index)) #TBD
                    print("Note: The action is not executed correctly!")
                    successor_when_error = np.delete(np.argwhere(prob_given_action_state > 0),np.argwhere(max_index))
                    roll_a_dice = np.random.choice(successor_when_error) #这个有点hardcode，剩余的各个states的probabili可能是不相同的
                    print("The new state is now: ", self.statespace[roll_a_dice])
                    return self.statespace[roll_a_dice]
        return self.current_state #just in case, if current_state is out of edge
     




