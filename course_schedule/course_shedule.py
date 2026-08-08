class Graph:
    def __init__(self, numNodes):
        self.nodeCount = numNodes
        self.graph     = [[] for i in range(numNodes)]
        self.inDergee  = [0 for i in range(numNodes)]
    
    def connectNodes(self, nodeA, nodeB):
        if not (nodeA >= 0 and nodeB >= 0 and nodeA < self.nodeCount and nodeB < self.nodeCount):
            print("ERROR: out of bounds")
            return
        
        self.graph[nodeA].append(nodeB)
        self.inDergee[nodeB] += 1
        return 
    
    def hasLoops(self):
        visited = [False for i in range(self.nodeCount)]
        queue = []

        in_degree = self.inDergee.copy()

        # Find the element with indegree 0
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        
        # If no element has indegree 0, that means that we have loops
        if len(queue) == 0:
            return True
        
        while len(queue) != 0:
            currNode = queue.pop()
            for i in self.graph[currNode]:
                in_degree[i] -= 1

                if not in_degree[i]:
                    queue.append(i)
        
        if sum(in_degree) != 0:
            return True
        
        return False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        g = Graph(numCourses)
        for i in prerequisites:
            g.connectNodes(i[1], i[0])
        return not g.hasLoops()
    
def test_solution():
    sol = Solution()

    ret = sol.canFinish(
        2,
        [[1,0]]
    )
    print(f"TEST1: res={ret} expected=True")

    ret = sol.canFinish(
        2,
        [[1,0],[0,1]]
    )
    print(f"TEST2: res={ret} expected=False")

    ret = sol.canFinish(
        5,
        [[1,0], [2,1], [3, 2], [4,2], [1,4]]
    )
    print(f"TEST3: res={ret} expected=False")

    ret = sol.canFinish(
        20,
        [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    )
    print(f"TEST4: res={ret} expected=False")

    ret = sol.canFinish(
        3,
        [[0,1],[0,2], [1,2]]
    )
    print(f"TEST5: res={ret} expected=True")