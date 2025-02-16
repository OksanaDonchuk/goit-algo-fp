import heapq
from typing import Dict, List, Tuple


def add_edge(graph: Dict[int, List[Tuple[int, int]]], u: int, v: int, weight: int) -> None:
    """
    Додає ребро між вершинами u та v із вказаною вагою.

    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Граф у форматі списку суміжності.
        u (int): Перша вершина.
        v (int): Друга вершина.
        weight (int): Вага ребра.
    """
    graph.setdefault(u, []).append((v, weight))
    graph.setdefault(v, []).append((u, weight))  # Оскільки граф неорієнтований


def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, float]:
    """
    Алгоритм Дейкстри для знаходження найкоротших шляхів у графі.

    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Граф у форматі списку суміжності.
        start (int): Початкова вершина.

    Returns:
        Dict[int, float]: Найкоротші відстані від стартової вершини до всіх інших вершин.
    """
    # Ініціалізація всіх відстаней як нескінченність
    distances: Dict[int, float] = {vertex: float('inf') for vertex in graph}
    distances[start] = 0  # Відстань від стартової вершини до самої себе — 0

    # Пріоритетна черга (мінімальна купа)
    priority_queue: List[Tuple[float, int]] = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдена відстань більше за поточну відстань, ігноруємо вузол
        if current_distance > distances[current_vertex]:
            continue

        # Перевірка всіх сусідніх вершин
        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight

            # Оновлюємо, якщо знайшли коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main() -> None:
    """
    Основна функція для створення графа, запуску алгоритму Дейкстри та виведення результатів.
    """
    # Створюємо граф у вигляді словника
    graph: Dict[int, List[Tuple[int, int]]] = {}

    # Додаємо ребра
    add_edge(graph, 0, 1, 10)
    add_edge(graph, 0, 4, 5)
    add_edge(graph, 1, 2, 1)
    add_edge(graph, 1, 4, 2)
    add_edge(graph, 2, 3, 4)
    add_edge(graph, 3, 4, 7)

    # Виклик алгоритму Дейкстри
    start_vertex = 0
    distances = dijkstra(graph, start_vertex)

    # Виведення найкоротших шляхів від початкової вершини
    for vertex, distance in distances.items():
        print(f"Відстань від вершини {start_vertex} до вершини {vertex}: {distance}")


if __name__ == "__main__":
    main()
