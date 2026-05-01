class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = set()
        visiting = set()

        def get_prereqs(course):
            prereqs = []
            for c, prereq in prerequisites:
                if c == course:
                    prereqs.append(prereq)
            return prereqs
        
        def dfs(course):
            if course in taken:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            prereqs = get_prereqs(course)
            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            taken.add(course)
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                
