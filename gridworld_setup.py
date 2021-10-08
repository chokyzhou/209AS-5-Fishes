#This file is only used for setting up Gridworld problem
#It includes: states for gridworld,
#             defined actions
#             a specific function of calculating the oberservation
#             and other properties for Gridworld only
#             transition probability is calculated in simulator.py
     
import numpy as np
import random

from numpy.lib.function_base import append

class GridWorld:
    def __init__(self):
        self.wind = .25 #pe
        self.numActions = 5
        self.gridSize = 5
        self.block = np.array([(1,1), (1,2), (3,1), (3,2)])
        self.target = np.array([(2,0), (2,2)])
        self.position = np.array([2,4])
        
        self.state = self.createState
        self.action = self.createAction
        self.prob_ss= self.pr_ss_s
        self.prob_action = self.action_probability
        self.observation = self.createObservation

    @property
    def createState(self):
        state_list = []
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                temp_state = [i,j]
                state_list.append(temp_state)
        return np.array(state_list)
    
    @property
    def pr_ss_s(self): #probability of successor state given current state (25*25)
        prob_ss = []

        stateSpace = self.state
        blockSpace = self.block

        for curr_state in stateSpace:
            temp_pr = []
            if_block1 = (blockSpace == curr_state).all(1).any()
            for succ_state in stateSpace:
                if if_block1 == True:
                    temp_pr.append(0)
                else:
                    if_block2 = (blockSpace == succ_state).all(1).any()
                    dist = np.linalg.norm(succ_state-curr_state)
                    if if_block2 == False and dist <= 1: #its impossible to move for more than one unit dist
                        temp_pr.append(1)
                    else:
                        temp_pr.append(0)
            temp_pr = np.array(temp_pr)
            if sum(temp_pr)!= 0:
                temp_pr = temp_pr/sum(temp_pr)
            prob_ss.append(temp_pr)
        return np.array(prob_ss)
    
    @property
    def action_probability(self): #only used as a weight for generating the transition probability
        prob_action = (1 - self.wind) + self.wind/4 
        #the overall probability of executing one action is same for every action in the Action set
        return prob_action
    
    @property
    def createAction(self):
        forward = [-1, 0]
        backward = [1, 0]
        left = [0 ,-1]
        right = [0 ,1]
        stay= [0,0]
        return np.array([forward, backward, left, right, stay])
    
    
    @property
    def createObservation(self):
        position = self.position
        RS, RD = self.target
        distance2RS = np.linalg.norm(position - RS)
        distance2RD = np.linalg.norm(position - RD)
        h = 2 / (1 / distance2RS + 1 / distance2RD)
        
        if np.random.rand() < np.ceil(h) - h:
            return np.floor(h)
        else:
            return np.ceil(h)

    
    
# """
# testing GridWorld
# """   
# if __name__ == "__main__":
#     grid = GridWorld()
    #print(grid.prob_ss)
#     #for i in range(len(grid.probability)):
#         #print(grid.probability[i], grid.state[i])
#     print(grid.probability)
#     #print(grid.observation)