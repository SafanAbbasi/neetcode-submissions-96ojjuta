class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        



        res = []
        adj = defaultdict(list)
        dep_count = [0] * (numCourses)
        for a, b in prerequisites:

            adj[b].append(a) # list contains everything that depends on b
            dep_count[a] += 1

        
        q = collections.deque()

        for course, dep in enumerate(dep_count):
            if dep == 0:
                q.append(course)

        count = 0

        if q:
            res.extend(q)
        else: 
            return []
        
        while q:

            nodep_course = q.popleft()
            count += 1

            for course in adj[nodep_course]:
                dep_count[course] -= 1

                if dep_count[course] == 0:
                    res.append(course)
                    q.append(course)
            
        return res if count == numCourses else []
        
        