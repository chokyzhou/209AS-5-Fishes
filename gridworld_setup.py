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
        global actionSpace
        global stateSpace
        global blockSpace
        global wind
        global avail_ss

        wind = .25 #pe
        self.numActions = 5
        self.gridSize = 5
        blockSpace = np.array([(1,1), (1,2), (3,1), (3,2)])
        self.target = np.array([(2,0), (2,2)])
        self.position = np.array([2,4])
        
        stateSpace = self.createState
        actionSpace = self.createAction
        avail_ss= self.get_available_successor_state
        self.transition_probability = self.create_transition_probability
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
    #construct a 25*25 matrix display all the availabale successor states given the current state
    def get_available_successor_state(self):
        avail_ss= []

        for curr_state in stateSpace:
            temp_ = []
            if_block1 = (blockSpace == curr_state).all(1).any()
            for succ_state in stateSpace:
                if if_block1 == True:
                    temp_.append(0)
                else:
                    if_block2 = (blockSpace == succ_state).all(1).any()
                    dist = np.linalg.norm(succ_state-curr_state)
                    if if_block2 == False and dist <= 1: #its impossible to move for more than one unit dist
                        #available successor state is marked as 1
                        temp_.append(1)
                    else:
                        #unavailable successor state is marked as 0
                        temp_.append(0)
            temp_ = np.array(temp_)
            avail_ss.append(temp_)
        return np.array(avail_ss)
    
    @property
    def create_transition_probability(self): #Create Transition Probability Matrix 5*25*25
        tran_pr = []
        for action_ in actionSpace:
            '''
            Default policy: 
            if the selected action is not available, the probaility of executing that action correctly is assigned to "Stay".
                   eg1. Given "Forward" action, if only forward is not possible, p(stay) = (1-pe + pe/4)
                   eg2. Given "Forward" action, if both forward and backward is not possible, p(stay) = (1-pe + pe/3)
                   eg3. Given "Forward" action, if both left and right is not possible, p(stay) = pe/2

            The function -- 'get_available_successor_state' is used to give the number of available actions and indexing
            its corresponding state

            Action Set Index --- [forward, backward, left, right, stay]
            '''
            index = 0
            empty_copy = np.zeros((25,25))
            for state_ in stateSpace:
                desired_nextState = np.array(state_+action_)
                available_actions = np.sum(avail_ss[index]) #get the number of available action
                if(available_actions != 0):
                    if_desired_exist = (stateSpace == desired_nextState).all(1).any()
                    if if_desired_exist == True:
                        available_actions -= 1 #refer to example 3
                        for i in range(len(stateSpace)): #find the index of desired_nextState in the [25*1] array
                            if np.array_equal(desired_nextState,stateSpace[i]):
                                empty_copy[index][i] = 1-wind
                                break
                    elif if_desired_exist == False:
                        for j in range(len(stateSpace)):
                            if np.array_equal(state_, stateSpace[j]):
                                empty_copy[index][j]= 1 - wind + wind/available_actions
                    rest_available_state = np.where(avail_ss[index] == 1)
                    for rest_index in rest_available_state[0]:
                        if empty_copy[index][rest_index] == 0:
                            empty_copy[index][rest_index] = wind/available_actions
                index += 1
            tran_pr.append(empty_copy)
        return np.array(tran_pr)

    
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

    
    

# if __name__ == "__main__":
#     grid = GridWorld()
#     # print(grid.transition_probability.shape)
#     print(grid.transition_probability[4][0])

#     #for i in range(len(grid.probability)):
#         #print(grid.probability[i], grid.state[i])
#     print(grid.probability)
#     #print(grid.observation)