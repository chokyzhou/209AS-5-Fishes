import numpy as np
import scipy.stats
import json
from system import System

class Bayes:
    """
    Class Bayes implements Bayes filter.

    TODO:
    function read_believe_prior
    """

    def __init__(self, system, position=np.array([0, 0]), target=np.array([[4, 4], [4, 5]])) -> None:
        self.pr_state_and_obs = None   # pr(s,o)
        self.pr_state_given_obs = None # pr(s|o)
        self.pr_state = None           # pr(s)

        self.init_believe
        self.init_system(system, position, target)

    def init_system(self, system, position, target):
        self.position = position       # initialize starting position
        self.target = target           # initialize target

        # initialize system
        self.system = system
        self.size = self.setSize
        self.stateSpace = self.getStateSpace
        self.expected_obs = self.setExpectedObs
        self.obs = self.getObservation

    @property
    def init_believe(self):
        # Believe
        self.believe_prior = None
        self.believe_post = None

        self.dist = scipy.stats.norm(0, 1) # ini distribution
        
    @property
    def getObservation(self):
        """
        This function should update current observation

        return observation
        """
        h = self.calObs(self.position)
        
        if np.random.rand() < np.ceil(h) - h:
            return np.floor(h)
        else:
            return np.ceil(h)
        

    @property
    def setSize(self):
        """
        Get size of the environment
        
        return tuple
        """
        return self.system.size

    @property
    def getStateSpace(self):
        #TODO
        return [(i,j) for i in range(self.size[0]) for j in range(self.size[1])]

    @property
    def setExpectedObs(self):
        """
        Calculated a table for expected observation

        return dic 
        """
        res = {}
        for state in self.stateSpace:
            res[state] = self.calObs(np.array(state))

        return res

    def calObs(self, position):
        """
        Calculate observation

        @param position - an array
        return np.float
        """
        RS, RD = self.target
        distance2RS = np.linalg.norm(position - RS)
        distance2RD = np.linalg.norm(position - RD)
        if not distance2RS:
            h = 2 / (1 / distance2RD)
        elif not distance2RD:
            h = 2 / (1 / distance2RS)
        else:
            h = 2 / (1 / distance2RS + 1 / distance2RD)
        return h

    def update_pr_obs_state(self):
        """
        Calculate pr(o|s)

        Steps:
        initialize pr map
        for state in stateSpace:
            diff = expected_obs from state - obs 
            put diff in pdf (assume Gaussian)
        normalize map
        return map
        """
        pr_map = np.empty(self.size)        
        stateSpace = self.stateSpace        # (5,5)
        expected_obs = self.expected_obs    # (5,5)

        for state in stateSpace:
            pr_map[state] = self.dist.pdf(expected_obs[state] - self.obs)

        pr_map = pr_map / np.linalg.norm(pr_map.flatten()) # normalize
        pr_map = pr_map.reshape(self.size)            

        return pr_map

    def update_believe(self):
        """
        Update Bel- and Bel+
        """
        # believe prior to observation is the probability of current state, ie pr(s|*)
        self.believe_prior = self.read_believe_prior()

        # believe post observation is the probability of current state given observation, ie pr(s|o,*)
        self.believe_post = self.read_believe_post()              

    def read_believe_prior(self):
        """
        Update Bel-
        
        TODO
        """
        # 1. TODO include blocks
        # 2. TODO assign getP to believe_prior
        return 1
    
    def read_believe_post(self):
        """
        Update Bel+

        return Bel+
        """
        believe_post = np.dot(self.pr_state_given_obs, self.believe_prior)
        believe_post = believe_post / np.linalg.norm(believe_post.flatten()) # normalize
        return believe_post.reshape(self.size)

    def get_state_estimate(self):
        """
        Update the believe state
        """
        self.update_believe()
        self.position = np.unravel_index(self.believe_post.argmax(), self.size)



if __name__ == "__main__":

    with open("./generator/A.json", "r") as f:
        A = json.load(f)
    
    with open("./generator/P.json", "r") as f:
        P = json.load(f)

    with open("./generator/S.json", "r") as f:
        S = json.load(f)

    with open("./generator/R.json", "r") as f:
        R = json.load(f)

    # build an initial P
    with open("./generator/size.json", "r") as f:
        size = json.load(f)

    M = size["M"]
    N = size["N"]

    system = System(S, A, R, P, 0.8, N, M)
    test = Bayes(system)

    #print(test.get_state_estimate())
    print(test.system.getA)
