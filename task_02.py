import turtle
import math


def draw_tree(branch_length: float, angle: float, level: int) -> None:
    """
    Рекурсивна функція для малювання дерева Піфагора.

    Args:
        branch_length (float): Довжина гілки.
        angle (float): Кут розгалуження гілок.
        level (int): Рівень рекурсії, що визначає деталізацію дерева.

    Returns:
        None
    """
    if level > 0:
        # Малюємо основну гілку
        turtle.forward(branch_length)
        turtle.right(angle)

        # Рекурсивно малюємо праву гілку
        draw_tree(branch_length * math.cos(math.radians(angle)), angle, level - 1)

        # Повертаємося та малюємо ліву гілку
        turtle.left(2 * angle)
        draw_tree(branch_length * math.cos(math.radians(angle)), angle, level - 1)

        # Повертаємося у вихідне положення
        turtle.right(angle)
        turtle.backward(branch_length)


def main() -> None:
    """
    Основна функція для ініціалізації вікна Turtle і запуску малювання фрактального дерева.

    Returns:
        None
    """
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    # Налаштування початкового положення Turtle
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -screen.window_height() // 2)
    turtle.pendown()
    turtle.speed(0)

    # Викликаємо функцію для малювання дерева
    draw_tree(100, 30, level)

    # Завершуємо роботу Turtle
    turtle.done()


if __name__ == "__main__":
    main()