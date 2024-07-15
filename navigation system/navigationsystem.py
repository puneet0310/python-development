buildings = {
    "A": {"x": 0, "y": 0},
    "B": {"x": 100, "y": 0},
    "C": {"x": 0, "y": 100},
    "D": {"x": 100, "y": 100},
}

paths = {
    ("A", "B"): 120,
    ("A", "C"): 150,
    ("B", "D"): 80,
    ("C", "D"): 130,
    ("A", "D"): 200,
}
import heapq

def shortest_distance(start, end, paths):
    """
    Calculate the shortest distance between two buildings.
    """
    queue = []
    heapq.heappush(queue, (0, start))
    visited = set()
    distances = {building: float("inf") for building in buildings}
    distances[start] = 0

    while queue:
        current_distance, current_building = heapq.heappop(queue)

        if current_building in visited:
            continue

        visited.add(current_building)

        for neighbor, distance in paths.items():
            if neighbor[0] == current_building or neighbor[1] == current_building:
                new_distance = current_distance + distance
                if new_distance < distances[neighbor[0]]:
                    distances[neighbor[0]] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor[0]))
                if new_distance < distances[neighbor[1]]:
                    distances[neighbor[1]] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor[1]))

    return distances[end]

print(shortest_distance("B", "D", paths))  # Output: 200
def time_taken_to_travel(start, end, paths):
    """
    Calculate the time taken to travel between two buildings.
    """
    distance = shortest_distance(start, end, paths)
    walking_speed = 1.4
    return distance / (walking_speed * 1000)  # Convert meters to kilometers

print(time_taken_to_travel("B", "D", paths))  # Output: 0.14285714285714285