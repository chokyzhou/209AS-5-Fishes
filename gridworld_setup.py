#This script is only used for setting up Gridworld problem
     
import numpy as np
import random
from numpy.core.shape_base import block

from numpy.lib.function_base import append

class GridWorld:
    def __init__(self):
        self.wind = .25 #pe
        self.numActions = 5
        self.gridSize = 5
        self.blockSpace = np.array([(1,1), (1,2), (3,1), (3,2)])
        self.target = np.array([(2,0), (2,2)])
        self.position = np.array([2,4])
        
        # {S A P R H gama}
        self.stateSpace = self.createState
        self.actionSpace = self.createAction
        self.avail_ss= self.get_available_successor_state
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
    
    #construct a 25*25 matrix display all the availabale successor states given the current state
    @property
    def get_available_successor_state(self):
        stateSpace = self.stateSpace
        blockSpace = self.blockSpace
        avail_ss= []

        for curr_state in self.stateSpace:
            temp_ = []
            if_block1 = (self.blockSpace == curr_state).all(1).any()
            for succ_state in self.stateSpace:
                if if_block1 == True:
                    temp_.append(0)
                else:
                    if_block2 = (self.blockSpace == succ_state).all(1).any()
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
        actionSpace = self.actionSpace
        stateSpace = self.stateSpace
        avail_ss = self.avail_ss
        wind = self.wind

        tran_pr = []
        for action_ in self.actionSpace:
            '''
            Default rule: 
            if the selected action is not available, the probaility of executing that action correctly is assigned to "Stay".
                   eg1. Given "Forward" action, if only forward is not possible, p(stay) = (1-pe + pe/4)
                   eg2. Given "Forward" action, if both forward and backward are not possible, p(stay) = (1-pe + pe/3)
                   eg3. Given "Forward" action, if both left and right are not possible, p(stay) = pe/2

            The function -- 'get_available_successor_state' is used to give the number of available actions and indexing
            their corresponding successor states respectively

            Action Set Index --- [forward, backward, left, right, stay]
            '''
            index = 0
            empty_copy = np.zeros((len(self.stateSpace),len(self.stateSpace)))
            for state_ in self.stateSpace:
                desired_nextState = np.array(state_+action_)
                available_actions = np.sum(self.avail_ss[index]) #get the number of available actions
                if(available_actions != 0):#not in block
                    if_desired_exist = (self.stateSpace == desired_nextState).all(1).any()
                    if_desired_in_block = (self.blockSpace == desired_nextState).all(1).any()
                    if if_desired_in_block == False and if_desired_exist == True :
                        available_actions -= 1 #refer to eg3
                        for i in range(len(self.stateSpace)): #find the index of desired_nextState in the [25*1] array
                            if np.array_equal(desired_nextState,self.stateSpace[i]):
                                empty_copy[index][i] = 1-self.wind
                                break
                    elif if_desired_in_block == True or if_desired_exist == False:
                        for j in range(len(self.stateSpace)):
                            #When desired_nextState of the action is not available, choose to stay, refer to eg1
                            if np.array_equal(state_, self.stateSpace[j]): 
                                empty_copy[index][j]= 1 - self.wind + self.wind/available_actions
                    rest_available_state = np.where(self.avail_ss[index] == 1)
                    for rest_index in rest_available_state[0]:
                        if empty_copy[index][rest_index] == 0: #avoid to overwrite desired_nextState or "Stay" action
                            empty_copy[index][rest_index] = self.wind/available_actions
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
        position = self.current_position
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
#     #print(grid.avail_ss)
#     print(grid.transition_probability[1][3])

#     #for i in range(len(grid.probability)):
#         #print(grid.probability[i], grid.state[i])
#     print(grid.probability)
#     #print(grid.observation)