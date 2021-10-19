import numpy as np
import math

def VI_Approximation(self):
    delta = 0.1
    N = 1
    theta = np.array([1]*N)
    self.initV()
    self.showV()

    while True:
        newV = {}
        newPi = {}
        Vth = {}

        sumDiffMin = math.inf

        for s in self.system.getS:
            maxV = -math.inf
            bestAction = None

            Vth[s] = theta.T * basis(s)
            for a in self.system.getA:
                tempV = 0

                for key, value in self.system.getP[s][str(a)].items():
                    if value > 0 :
                        tempV += value * (self.system.getR[key] + self.system.getGamma * Vth[s])
                
                if tempV > maxV:
                    maxV = tempV
                    bestAction = a
            newV[s] = maxV
            newPi[s] = bestAction

        sumDiff = 0
        for s in self.system.getS:
            sumDiff += abs(newV[s] - Vth[s])

        if sumDiffMin > sumDiff:
            sumDiffMin = sumDiff
            theta = 

        print("=====================================================")
        print("Diff: ", str(sumDiff))
        self.showV()
        if sumDiff < delta:
            # need to ask how to generate a policy based on the value of sates
            self.Pi = newPi
            break


def basis(state, targets=None):
    """
    Calculate L1 norm between state and lists of target
    @param state:  (1,) 
    @return:       (2,1) basis function
    """
    base = []
    for target in targets:
        

    return base
