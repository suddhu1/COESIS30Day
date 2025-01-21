import matplotlib.pyplot as plt
import numpy as np
import heapq

# Define grid size and obstacles
grid = np.zeros((10, 10))
obstacles = [(1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 1), (4, 4), 
             (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8)]
for obs in obstacles:
    grid[obs] = 1  # Mark obstacles

# Dijkstra's Algorithm Implementation
def dijkstra(start, goal):
    rows, cols = grid.shape
    distances = np.full(grid.shape, np.inf)  # Initialize distances to infinity
    distances[start] = 0
    priority_queue = [(0, start)]  # Priority queue to track nodes to visit
    came_from = {}  # To reconstruct the path

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            break

        # Check all possible neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current_node[0] + dx, current_node[1] + dy)

            # Ensure neighbor is within bounds and not an obstacle
            if (
                1 <= neighbor[0] < rows and 
                1 <= neighbor[1] < cols and 
                grid[neighbor] == 0  # Check if it's not an obstacle
            ):
                distance = current_distance + 1

                # Update distance if a shorter path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    came_from[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

    return came_from

# Visualize Path
start = (0, 0)
goal = (9, 9)
came_from = dijkstra(start, goal)

# Reconstruct path
path = []
current = goal
while current in came_from:
    path.append(current)
    current = came_from[current]
path.reverse()

# Plotting the grid and path
plt.imshow(grid.T, cmap='gray_r') # Transpose for proper visualization
for p in path:
    plt.plot(p[1], p[0], 'bo') # Blue points for path
plt.plot(start[1], start[0], 'go') # Green point for start
plt.plot(goal[1], goal[0], 'ro') # Red point for goal
plt.title('Dijkstra\'s Pathfinding Visualization')
plt.show()
