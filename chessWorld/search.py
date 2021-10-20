class Search:
    def __init__(self, target, N=8):
        self.target = target
        self.actions = [[-2, 1], [-2, -1], [-1, 2], [-1, -2],
                        [2, 1], [2, -1], [1, 2], [1, -2]]
        self.stateSpace = [(i,j) for i in range(N) for j in range(N)]
        
    def dfs(self, state, visited=set()):
        target = self.target
        stateSpace = self.stateSpace
        actions = self.actions
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
    
    def bfs(self, state):
        target = self.target
        stateSpace = self.stateSpace
        actions = self.actions

        stack = [[state, []]]
        visited = set()
        while stack:
            temp = []
            while stack:
                state, path = stack.pop()
                if state == target:
                    return path
                if state in visited or state not in stateSpace:
                    continue
                else:
                    visited.add(state)
                for action in actions:
                    temp.append([(action[0]+state[0], action[1] + state[1]), path + [state]])
            stack = temp
        return []

if __name__ == '__main__':
    target = (0,0)
    search = Search(target, 8)
    res = search.bfs((5,3))
    print(res)