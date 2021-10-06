import numpy as np


class GridWorld:
    def __init__(self):
        self.pe = .25
        self.numActions = 5
        self.gridSize = 5
        self.block = ((1,1), (2,1), (1,3), (2,3))
        
        self.state = self.createState
        self.action = self.createAction
        self.probability = self.createProbability
        self.observation = self.createObservation

    @property
    def createState(self):
        NotImplemented
    
    @property
    def createProbability(self):
        '''
        direction:
        1 2 3 4 5
        left right up down stay
        '''
        gridSize = self.gridSize
        numActions = self.numActions
        actionProb = 1 / numActions
        block = self.block
        
        # initialize grid
        grid = np.array([[[actionProb for _ in range(numActions)] for _ in range(gridSize)] for _ in range(gridSize)])
        
        # assgin block
        for i,j in block:
            for actionState in range(numActions):
                grid[actionState, j, i] = 0
        
        return grid
    
    @property
    def createAction(self):
        NotImplemented
        
    @property
    def createObservation(self):
        NotImplemented
    
    def todo(self, *args, **kwargs):
        print("NotImplemented")
    
    
"""
testing GridWorld
"""   
if __name__ == "__main__":
    grid = GridWorld()
    print(grid.probability)
    