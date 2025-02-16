import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# 🔹 Функція перетворення у мін- або макс-купу
def heapify_array(arr, heap_type="min"):
    """
    Перетворює масив у мін-купу або макс-купу.

    :param arr: Вхідний масив чисел
    :param heap_type: "min" для мін-купи, "max" для макс-купи
    :return: Масив, який відповідає структурі купи
    """
    arr = arr[:]  # Копіюємо масив, щоб не змінювати оригінал
    if heap_type == "min":
        heapq.heapify(arr)  # Мін-купа (за замовчуванням)
    elif heap_type == "max":
        arr = [-x for x in arr]  # Перетворення у негативи для макс-купи
        heapq.heapify(arr)
        arr = [-x for x in arr]  # Повертаємо назад у позитивні значення
    return arr


# 🔹 Функція побудови бінарної купи з масиву
def build_heap(arr):
    n = len(arr)
    nodes = [Node(val) for val in arr]

    for i in range(n // 2):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0] if nodes else None


# 🔹 Приклади масивів
unsorted_array = [15, 3, 17, 20, 8, 5, 2, 10, 12]

# Мін-купа
min_heap_array = heapify_array(unsorted_array, "min")
min_heap_root = build_heap(min_heap_array)
print("Мін-купа:", min_heap_array)
draw_tree(min_heap_root)

# Макс-купа
max_heap_array = heapify_array(unsorted_array, "max")
max_heap_root = build_heap(max_heap_array)
print("Макс-купа:", max_heap_array)
draw_tree(max_heap_root)

