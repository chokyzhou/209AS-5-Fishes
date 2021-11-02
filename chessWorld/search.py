import collections
import heapq 
import math
import random
import sys 

class Search:
    def __init__(self, target, N=8, obstacles=[]):
        """
        @param target: target state
        @param N: chess board size
        @param obstacles: list of obstacles
        return None
        """
        self.target = target
        self.obstacles = obstacles
        self.graph = self.createGraph(N)
    
    def createGraph(self, N):
        """
        create a graph for chess board
        @param N: chess board size
        return dict[list]
        """
        actions = [[-2, 1], [-2, -1], [-1, 2], [-1, -2],
                        [2, 1], [2, -1], [1, 2], [1, -2]]
        stateSpace = [(i,j) for i in range(N) for j in range(N)]
        obstacles = self.obstacles
        graph = collections.defaultdict(list)
        
        for state in stateSpace:
            for action in actions:
                nextState = (action[0]+state[0], action[1] + state[1])
                if nextState in stateSpace and state not in obstacles and nextState not in obstacles:
                    graph[state].append(nextState)
        return graph

    def dfs(self, state, visited=set()):
        """
        dfs implementation
        """
        graph = self.graph
        target = self.target

        if state == target:
            return [target]
        
        if state in graph.keys() and state not in visited:
            visited.add(state)
            for nextState in graph[state]:
                feedback = self.dfs(nextState, visited)
                if feedback:
                    return [state] + feedback
        return []
    
    def bfs(self, state):
        """
        bfs implementation
        """
        graph = self.graph
        target = self.target
        stack = [[state, []]]
        visited = set()

        while stack:
            temp = []
            while stack:
                curState, curPath = stack.pop(0)
                if curState == target:
                    return curPath + [curState]
                if curState not in visited and curState:
                    visited.add(curState)
                    for nextState in graph[curState]:
                        temp.append([nextState, curPath + [curState]])
            stack = temp
        return []

    def Astar(self, state):
        """
        A* implementation
        """
        def calcDistance(s1, s2):
            return abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])

        graph = self.graph
        target = self.target

        open = [(0, state, [])]
        closed = []

        while open:
            _, state, path = heapq.heappop(open)

            if state == target:
                return path + [state]
            
            for nextState in graph[state]:
                if nextState not in closed and nextState:
                    heapq.heappush(open, (calcDistance(nextState, target), nextState, path + [state]))                    

            closed.append(state)
        return []


    def rrt(self, state):
        """
        rrt implementation
        """
        def calcDistance(s1, s2):
            """
            p1 norm distance between states
            """
            return abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])
        
        def isValidPath(s1, s2):
            """
            Determines if knight can go from s1 to s2
            """
            if abs(s1[0] - s2[0]) == 1 and abs(s1[1] - s2[1]) == 2:
                return True
            if abs(s1[0] - s2[0]) == 2 and abs(s1[1] - s2[1]) == 1:
                return True
            return False

        graph = self.graph
        target = self.target
        G = {'V': set((state,)), 'E': collections.defaultdict(set)}
        
        while True:
            state_random = random.choice(list(graph.keys()))
            state_sorted = sorted([(s,calcDistance(s, state_random)) for s in G['V']], key=lambda x:x[1]) # one-liner
            state_sorted = [(None, float('inf'))] + state_sorted

            for i in range(1, len(state_sorted)):
                state_nearest, dis, pre_dis = state_sorted[i][0], state_sorted[i][1], state_sorted[i-1][1]
                
                if dis <= pre_dis:
                    if calcDistance(state_random, state_nearest) <= calcDistance((0,0), (2,1)) and isValidPath(state_random, state_nearest):
                        G['V'].add((state_random))
                        G['E'][state_nearest].add(state_random)
                        G['E'][state_random].add(state_nearest)
                
                    if target in G['V']:
                        self.graph = G['E']
                        return self.dfs(state)


def main(args):
    try:
        search_method = args[0]
        target = args[1] # Goal state
        ini = args[2] # Initial state
        obstacles = args[3] # obstacle space
    except:
        search_method = "rrt"
        target = (0,0) # Goal state
        ini = (5,3) # Initial state
        obstacles = [] # obstacle space
        print("Missing args. Using default instead.")
    
        
    search = Search(target, 8, obstacles=obstacles)

    # select search method
    if search_method == "dfs":
        res = search.dfs(ini) 
    if search_method == "bfs":
        res = search.bfs(ini) 
    if search_method == "a*":
        res = search.Astar(ini) 
    if search_method == "rrt":
        res = search.rrt(ini) 

    try:
        print("A valid path: " + str(res))
    except:
        print("Search method not specified.")

if __name__ == '__main__':
    main(sys.argv[1:])