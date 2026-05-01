class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = set()
        visiting = set()
        
        def has_prereq(course):
            prereqs = []
            for c, prereq in prerequisites:
                if course == c:
                    prereqs.append(prereq)
            return prereqs

        def dfs(course):
            if course in taken:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            prereqs = has_prereq(course)
            if prereqs:
                for prereq in prereqs:
                    if not dfs(prereq):
                        return False

            taken.add(course)
            visiting.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

                
