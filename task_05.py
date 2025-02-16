import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque
from typing import List, Dict, Optional


class Node:
    """Клас вузла бінарного дерева"""

    def __init__(self, key: int, color: str = "skyblue") -> None:
        """
        Ініціалізація вузла

        Args:
            key (int): Значення вузла
            color (str): Колір вузла (за замовчуванням - "skyblue")
        """
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.val: int = key
        self.color: str = color
        self.id: str = str(uuid.uuid4())  # Унікальний ідентифікатор вузла


def add_edges(graph: nx.DiGraph, node: Optional[Node], pos: Dict[str, tuple], x: float = 0, y: float = 0, layer: int = 1) -> nx.DiGraph:
    """
    Додає вузли та ребра до графа

    Args:
        graph (nx.DiGraph): Орієнтований граф
        node (Optional[Node]): Поточний вузол
        pos (Dict[str, tuple]): Словник координат вузлів
        x (float): Початкове положення вузла по x
        y (float): Початкове положення вузла по y
        layer (int): Поточний рівень у дереві

    Returns:
        nx.DiGraph: Оновлений граф із доданими вузлами та ребрами
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root: Node, colors_map: Dict[str, str]) -> None:
    """
    Візуалізує бінарне дерево

    Args:
        tree_root (Node): Кореневий вузол дерева
        colors_map (Dict[str, str]): Словник кольорів вузлів
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [colors_map.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_colors(n: int) -> List[str]:
    """
    Генерує список кольорів від темного до світлого

    Args:
        n (int): Кількість кольорів для генерації

    Returns:
        List[str]: Список кольорів у 16-ковому форматі
    """
    return [mcolors.to_hex(mcolors.LinearSegmentedColormap.from_list("", ["#00008B", "#ADD8E6"])(i / n)) for i in range(n)]


def dfs(tree_root: Node) -> List[Node]:
    """
    Обхід бінарного дерева в глибину (DFS)

    Args:
        tree_root (Node): Кореневий вузол дерева

    Returns:
        List[Node]: Порядок обходу вузлів
    """
    stack = [tree_root]
    visited = []
    order = []

    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.append(node)
            order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return order


def bfs(tree_root: Node) -> List[Node]:
    """
    Обхід бінарного дерева в ширину (BFS)

    Args:
        tree_root (Node): Кореневий вузол дерева

    Returns:
        List[Node]: Порядок обходу вузлів
    """
    queue = deque([tree_root])
    visited = []
    order = []

    while queue:
        node = queue.popleft()
        if node and node not in visited:
            visited.append(node)
            order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return order


def render_tree_walk(tree_root: Node, visit_order: List[Node]) -> None:
    """
    Візуалізує процес обходу дерева, змінюючи кольори вузлів

    Args:
        tree_root (Node): Кореневий вузол дерева
        visit_order (List[Node]): Порядок відвідування вузлів
    """
    colors = generate_colors(len(visit_order))
    colors_map = {node.id: colors[i] for i, node in enumerate(visit_order)}
    draw_tree(tree_root, colors_map)


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходу в глибину (DFS)
dfs_order = dfs(root)
render_tree_walk(root, dfs_order)

# Візуалізація обходу в ширину (BFS)
bfs_order = bfs(root)
render_tree_walk(root, bfs_order)
