from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_count = [0]*numCourses
        unlocks = defaultdict(list)

        for [course, prereq] in prerequisites:
            prereq_count[course]+=1
            unlocks[prereq].append(course)
        
        queue = deque()
        for i in range(numCourses):
            if prereq_count[i]==0:
                queue.append(i)

        courses_taken = 0
        while queue:
            course = queue.popleft()
            courses_taken += 1
            for c in unlocks[course]:
                prereq_count[c]-=1
                if prereq_count[c] == 0:
                    queue.append(c)
        
        return courses_taken == numCourses