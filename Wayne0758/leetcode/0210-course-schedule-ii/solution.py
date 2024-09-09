class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)

        for course, pre in prerequisites:
            adj_list[pre].append(course)
            indegree[course] += 1
        zero_indegree_queue = [k for k in range(numCourses) if k not in indegree]

        topological_sorted_order = []

        while zero_indegree_queue:

            vertex = zero_indegree_queue.pop(0)
            topological_sorted_order.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return (
            topological_sorted_order
            if len(topological_sorted_order) == numCourses
            else []
        )
        
