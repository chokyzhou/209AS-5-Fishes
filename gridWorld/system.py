# system class
# used to build a system with following information
# S -- State Space
# A -- Action Space
# R -- Reward
# P -- Transition Probability
# O -- Observation (No sure the propuse of this function, HARDCODED for now)
# gamma -- discount factor

# the Coordinate system for a N row x M colum gridword words works as 
# the Bottom left is (0,0), Top right is (M, N)

# For actions:
# 0:    No Move
# 1:    Up
# 2:    Down
# 3:    Left
# 4:    Right

from convert import Convert
import random

class System:
    def __init__(self, S, A, R, P, gamma, N, M) -> None:
        self.S = S
        self.A = A
        self.R = R
        self.P = P
        self.size = (N, M)
        self.gamma = gamma

    def makeTransition(self, curState, action):
        # this is the Transition function, used to calculate the next state
        # based on the current state, action and transition probability
        
        possibleState = {}

        for key, value in self.P[Convert.coo2str(curState[0], curState[1])][str(action)].items():
            if value > 0:
                possibleState[key] = value
        
        randomNum = random.random()
        for key, value in possibleState.items():
            if randomNum - value < 0:
                return key
            randomNum -= value
    
    @property
    def getP(self):
        return self.P
    
    @property
    def getR(self):
        return self.R
    
    @property
    def getS(self):
        return self.S

    @property
    def getA(self):
        return self.A
    
    @property
    def getGamma(self):
        return self.gamma
    
    @property
    def getSize(self):
        return self.size