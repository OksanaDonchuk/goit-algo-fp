from typing import Optional


class Node:
    """
    Клас, що представляє вузол у однозв'язному списку.

    Атрибути:
        data (int): Значення вузла.
        next (Optional[Node]): Посилання на наступний вузол у списку.
    """
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional["Node"] = None


class LinkedList:
    """
    Клас, що представляє однозв'язний список.

    Атрибути:
        head (Optional[Node]): Головний вузол списку.
    """
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def insert_at_beginning(self, data: int) -> None:
        """
        Додає вузол з переданим значенням на початок списку.

        Args:
            data (int): Значення нового вузла.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self) -> None:
        """
        Реверсує однозв'язний список, змінюючи посилання між вузлами.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self) -> None:
        """
        Сортує однозв'язний список методом вставок.
        """
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sorted_insert(self, head_ref: Optional[Node], new_node: Node) -> Optional[Node]:
        """
        Вставляє вузол у відсортований список у правильному порядку.

        Args:
            head_ref (Optional[Node]): Головний вузол відсортованого списку.
            new_node (Node): Вузол, який необхідно вставити.

        Returns:
            Optional[Node]: Новий головний вузол відсортованого списку.
        """
        if not head_ref or head_ref.data >= new_node.data:
            new_node.next = head_ref
            return new_node
        current = head_ref
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head_ref

    def merge_sorted_lists(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        """
        Об'єднує два відсортовані однозв'язні списки в один відсортований список.

        Args:
            l1 (Optional[Node]): Головний вузол першого списку.
            l2 (Optional[Node]): Головний вузол другого списку.

        Returns:
            Optional[Node]: Головний вузол об'єднаного відсортованого списку.
        """
        dummy = Node(0)
        tail = dummy
                
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
    
        tail.next = l1 if l1 else l2
        return dummy.next  


    def print_list(self) -> None:
        """
        Виводить елементи однозв'язного списку.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Приклад використання
llist = LinkedList()
llist.insert_at_beginning(15)
llist.insert_at_beginning(25)
llist.insert_at_beginning(5)
print("List:")
llist.print_list()

llist.reverse()
print("Reversed list:")
llist.print_list()

llist.insertion_sort()
print("Sorted list:")
llist.print_list()

# Об'єднання двох відсортованих списків
list1 = LinkedList()
list1.insert_at_beginning(60)
list1.insert_at_beginning(40)
list1.insert_at_beginning(10)

list2 = LinkedList()
list2.insert_at_beginning(50)
list2.insert_at_beginning(30)
list2.insert_at_beginning(20)

merged_list = LinkedList()
merged_list.head = merged_list.merge_sorted_lists(list1.head, list2.head)
print("Merged sorted list:")
merged_list.print_list()