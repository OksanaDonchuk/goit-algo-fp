from typing import Dict, List, Tuple

# Вхідні дані
items: Dict[str, Dict[str, int]] = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget: int = 100


def greedy_algorithm(items: Dict[str, Dict[str, int]], budget: int) -> Tuple[List[str], int]:
    """
    Жадібний алгоритм вибору страв для максимізації калорійності в межах заданого бюджету.

    Args:
        items (Dict[str, Dict[str, int]]): Словник, що містить страви, їхню вартість і калорійність.
        budget (int): Доступний бюджет.

    Returns:
        Tuple[List[str], int]: Список вибраних страв та загальна калорійність.
    """
    # Відсортовуємо страви за співвідношенням калорій до вартості (спадний порядок)
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories: int = 0
    selected_items: List[str] = []

    for item, info in sorted_items:
        if budget >= info['cost']:
            selected_items.append(item)
            total_calories += info['calories']
            budget -= info['cost']

    return selected_items, total_calories


def dynamic_programming(items: Dict[str, Dict[str, int]], budget: int) -> Tuple[List[str], int]:
    """
    Алгоритм динамічного програмування для знаходження оптимального вибору страв.

    Args:
        items (Dict[str, Dict[str, int]]): Словник, що містить страви, їхню вартість і калорійність.
        budget (int): Доступний бюджет.

    Returns:
        Tuple[List[str], int]: Список вибраних страв та максимальна калорійність.
    """
    n: int = len(items)
    dp: List[List[int]] = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list: List[Tuple[str, Dict[str, int]]] = list(items.items())

    # Заповнення таблиці динамічного програмування
    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost = info['cost']
        calories = info['calories']

        for b in range(1, budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b-cost] + calories)
            else:
                dp[i][b] = dp[i-1][b]

    # Відновлення вибраних страв
    selected_items: List[str] = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i-1][b]:
            selected_items.append(item_list[i-1][0])
            b -= item_list[i-1][1]['cost']

    return selected_items, dp[n][budget]


# Приклад використання
print("Жадібний алгоритм:", greedy_algorithm(items, budget))
print("Алгоритм динамічного програмування:", dynamic_programming(items, budget))
