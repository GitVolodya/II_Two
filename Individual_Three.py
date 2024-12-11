from collections import deque

def bfs_min_distance(distance_matrix, start, end):
    """Поиск минимального расстояния с помощью алгоритма BFS."""

    num_cities = len(distance_matrix)
    queue = deque([start])
    distances = [float('inf')] * num_cities
    distances[start] = 0
    visited = [False] * num_cities
    visited[start] = True

    while queue:
        current = queue.popleft()

        for neighbor in range(num_cities):
            if distance_matrix[current][neighbor] > 0 and not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[current] + distance_matrix[current][neighbor]
                queue.append(neighbor)

    return distances[end] if distances[end] != float('inf') else -1  # -1 если путь не найден

# Пример использования
if __name__ == "__main__":
    # Обновленная матрица расстояний между городами
    distance_matrix = [
        [0, 83, 224, 433, 549, 729, 886, 552, 441, 192],
        [83, 0, 150, 359, 475, 655, 812, 478, 367, 275],
        [224, 150, 0, 209, 325, 505, 662, 328, 217, 416],
        [433, 359, 209, 0, 116, 296, 453, 537, 426, 625],
        [549, 475, 325, 116, 0, 180, 337, 431, 542, 741],
        [729, 655, 505, 296, 180, 0, 157, 251, 362, 633],
        [886, 812, 662, 453, 337, 157, 0, 342, 453, 724],
        [552, 478, 328, 537, 431, 251, 342, 0, 111, 382],
        [441, 367, 217, 426, 542, 362, 453, 111, 0, 493],
        [192, 275, 416, 625, 741, 633, 724, 382, 493, 0],
    ]

    start_city = 0  # Начальный город (индекс)
    end_city = 3    # Конечный город (индекс)

    min_distance = bfs_min_distance(distance_matrix, start_city, end_city)

    if min_distance != -1:
        print(f"Минимальное расстояние между городами {start_city} и {end_city}: {min_distance}")
    else:
        print(f"Путь между городами {start_city} и {end_city} не найден.")
