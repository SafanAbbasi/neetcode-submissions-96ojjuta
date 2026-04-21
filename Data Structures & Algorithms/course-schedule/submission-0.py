class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # requires toplogical sort
        # does the graph have a cycle?
        #  If there's a cycle in the prerequisites, you can't finish all courses. 
        # If there's no cycle, you can.

        adj = defaultdict(list)
        # For each node (course), 
        # you store a list of its neighbors (the courses that depend on it, or that it points to)

        for a,b in prerequisites:
            adj[b].append(a)

        def dfs(course):

            if state[course] == 1:  # cycle detected
                return False
            if state[course] == 2:  # already fully explored, safe
                return True
            
            state[course] = 1  # mark as visiting
            
            for value in adj[course]:
                if not dfs(value):
                    return False

            state[course] = 2  # done exploring, mark as visited
            return True

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False

        return True