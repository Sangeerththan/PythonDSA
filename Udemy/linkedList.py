class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, element):
        n = Node(element)
        n.next_node = self.head
        self.head = n

    def print_list(self):
        n = self.head
        print("Linked list head is:", n.element)
        while n is not None:
            print(n.element, ' ', end='')
            n = n.next_node
        print()


def print_list(n):
    while n is not None:
        print(n.element, ' ', end=" ")
        n = n.next_node


def linked_list():
    ll = LinkedList()
    ll.insert_first(4)
    ll.insert_first(5)
    ll.insert_first(6)
    ll.print_list()
    ll.insert_first(44)
    ll.print_list()


def linked_list1():
    l = Node(5, Node(4, Node(6, Node(6, Node(30)))))
    print_list(l)


if __name__ == "__main__":
    linked_list()
