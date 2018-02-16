import DoublyLinkedList

__author__ = 'Hunt Blanchat'


class Stack:

    def __init__(self):
        """
        Creates a Doubly Linked List object and stores it in the variable stack
        and uses DLL to simulate a Stack data structure
        """
        self.stack = DoublyLinkedList.DoublyLinkedList()

    def is_empty(self):
        """ Checks if the Doubly Linked List or Stack is empty

        :return: boolean
        """
        return self.stack.size == 0

    def push(self, value):
        """ Adds an item to the front of the Doubly Linked List/Stack

        :param value: value being stored in the Node added to the DLL
        :return: None
        """
        self.stack.add_front(value)

    def pop(self):
        """ Removes an item from the front of the DLL or the "top" and returns the value of removed Node

        :return: value of stored in the removed Node
        """
        return self.stack.remove_front()

    def peek(self):
        """ Looks at what is stored in on the "top" and returns that value

        :return: value stored in the head of the DLL
        """
        return self.stack.head.data

    def size(self):
        """ Accesses the data value in the DLL/Stack and returns said value

        :return: value stored in size or int
        """
        return self.stack.size


def main():
    steak = Stack()
    print(steak.is_empty())
    steak.push(4)
    print(steak.peek())
    print(steak.pop())
    print(steak.is_empty())
    steak.push(4)
    print(steak.size())


if __name__ == '__main__':
    main()
