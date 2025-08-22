from collections import deque

def canFinish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)} 
    in_degree = {i: 0 for i in range(numCourses)}
    for a, b in prerequisites:
        graph[a].append(b)
        in_degree[b] += 1
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)
    course_count = 0
    while queue:
        node = queue.popleft()
        course_count += 1
        for j in graph[node]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                queue.append(j)

    return course_count == numCourses

print(canFinish(2, [[1, 0]]))  # Output: True
print(canFinish(2, [[1, 0], [0, 1]]))  # Output: False