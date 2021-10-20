class Search:
    def __init__(self, target, N):
        self.target = target
        self.actions = [[-2, 1], [-2, -1], [-1, 2], [-1, -2],
                        [2, 1], [2, -1], [1, 2], [1, -2]]
        self.stateSpace = [[(i,j) for i in range(N)] for j in range(N)]
        
    def dfs(self, state, visited=set()):
        target = self.target
        stateSpace = self.stateSpace
        res = []
        
        if state == target:
            return [target]
        
        if state not in visited:
            visited.add(state)
            for action in actions:
                nextState = (action[0]+state[0], action[1] + state[1])
                if nextState in stateSpace:
                    res = self.dfs(nextState)
                    if res:
                        res.append(state)
                        return res
        return []
    
    def bfs(self):
        stack = [state]
        visited = set()
        while stack:
            temp = []
            while stack:
                curState = stack.pop()
                if curState in visited:
                    continue
                visited.add(curState)
                for action in actions:
                    temp.append(state+action)
            stack = temp
            
if __name__ == '__main__':
    search = Search((0,0), 8)