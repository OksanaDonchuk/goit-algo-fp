import random
import matplotlib.pyplot as plt
from typing import Dict, Tuple


def roll_dice(num_rolls: int) -> Tuple[Dict[int, int], Dict[int, float]]:
    """
    Симулює кидання двох кубиків задану кількість разів та обчислює частоту випадіння кожної можливої суми.

    Args:
        num_rolls (int): Кількість симуляцій кидків кубиків.

    Returns:
        Tuple[Dict[int, int], Dict[int, float]]: 
            - Словник з підрахунком кількості випадків для кожної суми.
            - Словник із розрахованими ймовірностями кожної суми.
    """
    # Ініціалізуємо словник для підрахунку кількості випадків кожної суми (від 2 до 12)
    sums_count: Dict[int, int] = {i: 0 for i in range(2, 13)}

    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_count[total] += 1

    # Розрахунок ймовірностей
    probabilities: Dict[int, float] = {k: v / num_rolls for k, v in sums_count.items()}

    return sums_count, probabilities


def plot_probabilities(probabilities: Dict[int, float]) -> None:
    """
    Будує графік ймовірностей кожної суми, отриманої при симуляції кидання двох кубиків.

    Args:
        probabilities (Dict[int, float]): Словник ймовірностей кожної суми.
    """
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми при киданні двох кубиків (Метод Монте-Карло)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


# Параметри симуляції
num_rolls: int = 100000  # Кількість кидків

# Запускаємо симуляцію
sums_count, probabilities = roll_dice(num_rolls)

# Виведення результатів у таблиці
print("Сума\tКількість\tЙмовірність")
for total, count in sums_count.items():
    print(f"{total}\t{count}\t\t{probabilities[total]:.4f}")

# Побудова графіку
plot_probabilities(probabilities)
