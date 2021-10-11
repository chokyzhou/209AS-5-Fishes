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

from _typeshed import Self


class System:
    def __init__(S, A, R, P, gamma) -> None:
        Self.S = S
        Self.A = A
        Self.R = R
        Self.P = P
        Self.gamma = gamma

    def makeTransition(self, curState, action):
        # this is the Transition function, used to calculate the next state
        # based on the current state, action and transition probability

