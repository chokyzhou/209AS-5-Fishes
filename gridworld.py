import numpy as np


class GridWorld:
    def __init__(self):
        self.pe = .25
        self.numActions = 5
        self.gridSize = 5
        self.block = np.array([(1,1), (2,1), (1,3), (2,3)])
        self.target = np.array([(2,0), (2,2)])
        self.position = np.array([2,4])
        
        self.state = self.createState
        self.action = self.createAction
        self.probability = self.createProbability
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
    def createProbability(self, state):
        '''
        direction:
        1 2 3 4 5
        left right up down stay
        '''
        actionSpace = None
        blockSpace = None
        stateSpace = None
        
        prob = []
        for action in actionSpace:
            nextState = state + action
            if nextState in stateSpace and nextState not in blockSpace:
                prob.append(.2)
            else:
                prob.append(0)

        return np.array(prob) / sum(prob)
    
    
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
    
    def todo(self, *args, **kwargs):
        print("NotImplemented")
    
    
"""
testing GridWorld
"""   
if __name__ == "__main__":
    grid = GridWorld()
    print(grid.state)
    #print(grid.observation)