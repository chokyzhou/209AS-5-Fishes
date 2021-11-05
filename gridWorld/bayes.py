import numpy as np
import scipy.stats

class Bayes:

    def __init__(self) -> None:
        self.pr_state_and_obs = None   # pr(s,o)
        self.pr_state_given_obs = None # pr(s|o)
        self.pr_state = None           # pr(s)

        self.size = self.setSize
        self.stateSpace = self.getStateSpace
        self.expected_obs = self.setExpectedObs
        self.obs = self.getObservation
        
        self.dist = scipy.stats.norm(0, 1) # ini distribution
        
    @property
    def getObservation(self):
        #TODO
        return 1

    @property
    def setSize(self):
        #TODO
        return (5,5)

    @property
    def getStateSpace(self):
        #TODO
        return [(i,j) for i in range(self.size[0]) for j in range(self.size[1])]

    @property
    def setExpectedObs(self):
        #TODO
        def calObs(row,col):
            return 1

        res = {}
        for state in self.stateSpace:
            res[state] = calObs(*state)
        return res

    def update_pr_obs_state(self):
        """
        pr(o|s)
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
            if state == (3,2):
                pr_map[state] = self.dist.pdf(expected_obs[state] - self.obs)
            else:
                pr_map[state] = 0

        pr_map = pr_map / np.linalg.norm(pr_map.flatten()) # normalize
        pr_map = pr_map.reshape(self.size)                 # reshape

        return pr_map




if __name__ == "__main__":
    test = Bayes()
    test.update_pr_state_and_obs()