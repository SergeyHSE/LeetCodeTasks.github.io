"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def hasCycle(course, visited):
            if visited[course] == 1:
                return True
            
            if visited[course] == -1:
                return False
            visited[course] = 1
            
            for neighbor in graph[course]:
                if hasCycle(neighbor, visited):
                    return True
            visited[course] = -1
            return False
        visited = [0] * numCourses
        for i in range(numCourses):
            if not visited[i] and hasCycle(i, visited):
                return False
        return True
