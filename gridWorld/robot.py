from convert import Convert
import math
import copy

class Robot:
    def __init__(self, system) -> None:
        self.system = system
        self.size = system.getSize
        self.V = {}
        self.Pi = {}
        

    def VI(self):
        delta = 0.1
        self.initV()
        self.showV()
        
        while True:
            newV = {}
            newPi = {}

            for s in self.system.getS:

                maxV = -math.inf
                bestAction = None
                for a in self.system.getA:
                    tempV = 0

                    for key, value in self.system.getP[s][str(a)].items():
                        if value > 0 :
                            tempV += value*(self.system.getR[key] + self.system.getGamma*self.V[key])
                    
                    if tempV > maxV:
                        maxV = tempV
                        bestAction = a
                newV[s] = maxV
                newPi[s] = bestAction

            sumDiff = 0
            for s in self.system.getS:
                sumDiff += abs(self.V[s]-newV[s])
                self.V[s] = newV[s]
            print("=====================================================")
            print("Diff: ", str(sumDiff))
            self.showV()
            if sumDiff < delta:
                # need to ask how to generate a policy based on the value of sates
                self.Pi = newPi
                break


    def showV(self):
        Vstr = ""
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                Vstr += str(round(self.V[Convert.coo2str(x,self.size[0]-1-y)],3)) + "\t"
            print(Vstr)
            Vstr = ""

    def initV(self):
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                #self.V[Convert.coo2str(x,y)] = self.system.getR[Convert.coo2str(x,y)]
                self.V[Convert.coo2str(x,y)] = 0 #self.system.getR[Convert.coo2str(x,y)]

    def PI(self):
        self.initPI()
        self.initV()
        self.policyEvaluation()
        i = 0

        while True:
            oldPi = copy.deepcopy(self.Pi)
            oldV = copy.deepcopy(self.V)

            for s in self.system.getS:
                maxV = self.V[s]
                maxA = self.Pi[s]
                for a in self.system.getA:
                    tempV = 0
                    for key, value in self.system.getP[s][str(a)].items():
                        if value > 0:
                            tempV += value * (self.system.getR[key] + self.system.getGamma * self.V[key])
                    if tempV > maxV:
                        maxV = tempV
                        maxA = a

                self.Pi[s] = maxA
                self.V[s] = maxV

            self.showPI()

            sumDiff = 0
            for s in self.system.getS:
                sumDiff += abs(self.V[s]-oldV[s])
            print(sumDiff)
            
            if sumDiff < 0.1 and self.Pi == oldPi:
                break



    def showPI(self):
        actions = ["⟲", "↑", "↓", "←", "→"]

        print("Value ==========================================================")
        Vstr = ""
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                Vstr += str(round(self.V[Convert.coo2str(x,self.size[0]-1-y)], 3)) + "\t"
            print(Vstr)
            Vstr = ""

        print("Police ==========================================================")

        for y in range(self.size[0]):
            piStr = ""
            for x in range(self.size[1]):
                piStr += actions[self.Pi[Convert.coo2str(x,self.size[0]-1-y)]] + " "
            print(piStr)
            piStr = ""


    def initPI(self):
        for s in self.system.getS:
            self.Pi[s] = 0

    def policyEvaluation(self):
        for s in self.system.getS:
            tempV = 0
            for key, value in self.system.getP[s][str(self.Pi[s])].items():
                if value > 0:
                    tempV += value * (self.system.getR[key] + self.system.getGamma * self.V[key])
            self.V[s] = tempV

        return self.V