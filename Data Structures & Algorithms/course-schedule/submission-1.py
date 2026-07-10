class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency graph
        # build indegree list
        # implement bfs

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()

        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)

        completed = 0
        while queue:
            course = queue.popleft()
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            completed += 1

        return completed == numCourses
