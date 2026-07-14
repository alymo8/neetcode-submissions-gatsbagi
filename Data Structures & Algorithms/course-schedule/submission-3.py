class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = set()
        visiting = set()

        def get_course_prereq(course):
            prereqs = []
            for prereq, c in prerequisites:
                if c == course:
                    prereqs.append(prereq)
            return prereqs

        def dfs(course):
            if course in taken:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            prereqs = get_course_prereq(course)
            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            taken.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

