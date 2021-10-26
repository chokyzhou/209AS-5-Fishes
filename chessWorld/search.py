import collections
import heapq 
import math

class Search:
    def __init__(self, target, N=8):
        self.target = target
        self.graph = self.createGraph(N)
    
    def createGraph(self, N):
        actions = [[-2, 1], [-2, -1], [-1, 2], [-1, -2],
                        [2, 1], [2, -1], [1, 2], [1, -2]]
        stateSpace = [(i,j) for i in range(N) for j in range(N)]

        graph = collections.defaultdict(list)
        for state in stateSpace:
            for action in actions:
                nextState = (action[0]+state[0], action[1] + state[1])
                if nextState in stateSpace:
                    graph[state].append(nextState)
        return graph

    def dfs(self, state, visited=set()):
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
                if curState not in visited:
                    visited.add(curState)
                    for nextState in graph[curState]:
                        temp.append([nextState, curPath + [curState]])
            stack = temp
        return []

    def Astar(self, state):
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
                if nextState not in closed:
                    heapq.heappush(open, (calcDistance(nextState, target), nextState, path + [state]))                    

            closed.append(state)
        return []


if __name__ == '__main__':
    target = (0,0)
    search = Search(target, 8)
    res = search.Astar((5,3))
    print(res)