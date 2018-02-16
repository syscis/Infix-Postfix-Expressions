__author__ = 'guinnc\nModified by Jack Tompkins\nModified by Hunt Blanchat'


class DoublyLinkedNode:
    """ A single node in a doubly-linked list.
        Contains 3 instance variables:
            data: The value stored at the node.
            prev: A pointer to the previous node in the linked list.
            next: A pointer to the next node in the linked list.
    """

    def __init__(self, value):
        """
        Initializes a node by setting its data to value and
        prev and next to None.
        :return: The reference for self.
        """
        self.data = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    The doubly-linked list class has 3 instance variables:
        head: The first node in the list.
        tail: The last node in the list.
        size: How many nodes are in the list.
    """

    def __init__(self):
        """
        The constructor sets head and tail to None and the size to zero.
        :return: The reference for self.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def add_front(self, value):
        """
        Creates a new node (with data = value) and puts it in the
        front of the list.
        :return: None
        """
        new_node = DoublyLinkedNode(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    def add_rear(self, value):
        """
        Creates a new node (with data = value) and puts it in the
        rear of the list.
        :return: None
        """
        new_node = DoublyLinkedNode(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def remove_front(self):
        """
        Removes the node in the front of the list.
        :return: The data in the deleted node.
        """

        value = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        self.size -= 1
        return value

    def remove_rear(self):
        """
        Removes the node in the rear of the list.
        :return: The data in the deleted node.
        """
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        self.size -= 1
        return value

    def print_it_out(self):
        """
        Prints out the list from head to tail all on one line.
        :return: None
        """
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def print_in_reverse(self):
        """
        Prints out the list from tail to head all on one line.
        :return: None
        """
        temp = self.tail
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.prev
        print()

    def at_index(self, index):
        """
        Retrieves the data of the item at index.
        :param index: The index of the item to retrieve.
        :return: Returns the data of the item.
        """
        count = 0
        temp = self.head
        while count < index:
            count += 1
            temp = temp.next
        if not temp:
            return None
        return temp.data

    def index_of(self, value):
        """ Searches for value within the List and returns the index if found, -1 if not

        :param value: value being searched for
        :return: integer [-1, len(n)-1] n=DLL
        """
        index = 0
        temp = self.head
        if self.head is None:
            return -1
        while temp.data != value:
            index += 1
            temp = temp.next
            if index == self.size:
                return -1
        return index

    def insert_at(self, index, value):
        """ Inserts Node with data=value at position index

        :param index: position
        :param value: Node data
        :return: None
        """
        item = DoublyLinkedNode(value)
        count = 0
        temp = self.head
        if self.size == 0:
            self.add_front(value)
        elif (-1*self.size) <= index < 0:
            index1 = self.size + index
            return DoublyLinkedList.insert_at(self, index1, value)
        elif index == 0:
            self.add_front(value)
        elif index == self.size:
            self.add_rear(value)
        elif 0 < index < self.size:
            while count < index:
                temp = temp.next
                count += 1
            prev = temp.prev
            item.prev = temp.prev
            temp.prev = item
            item.next = temp
            prev.next = item
            self.size += 1
        else:
            raise IndexError

    def remove_at(self, index):
        """ Removes the Node at position index and returns the data of the removed Node

        :param index: position
        :return: Node.data of DoublyLinkedList[index]
        """
        count = 0
        temp = self.head
        if self.size == 0:
            raise IndexError
        elif self.size == 1:
            self.tail = None
            return self.remove_front()
        elif (-1*self.size) <= index < 0:
            index = self.size + index
            return DoublyLinkedList.remove_at(self, index)
        elif index == 0:
            return self.remove_front()
        elif index == self.size - 1:
            return self.remove_rear()
        elif 0 < index <= self.size:
            while count < index:
                count += 1
                temp = temp.next
            prev = temp.prev
            nex = temp.next
            prev.next = nex
            nex.prev = prev
            self.size -= 1
            return temp.data
        raise IndexError


def main():
    dll = DoublyLinkedList()
    dll.add_rear(5)
    dll.add_rear(2)
    dll.add_rear(25)
    dll.add_rear(-4)
    dll.insert_at(2, 7)
    dll.print_it_out()
    dll.print_in_reverse()

    x = dll.remove_rear()
    dll.print_it_out()
    print("\tThe item removed was {}.".format(x))
    x = dll.remove_at(0)
    dll.print_it_out()
    print("\tThe item removed was {}.".format(x))
    x = dll.remove_at(2)
    dll.print_it_out()
    print("\tThe item removed was {}.".format(x))

    print()
    dll = DoublyLinkedList()
    dll.add_rear(1)
    dll.add_rear(2)
    dll.add_rear(4)
    dll.add_rear(25)
    dll.add_rear(35)
    dll.print_it_out()
    for i in range(dll.size):
        y = dll.at_index(i)
        y_index = dll.index_of(y)
        print('The value at index {:d} is {} for which indexOf({}) returned {}.'.format(i, y, y, y_index))
    print('indexOf(-10) is {}'.format(dll.index_of(-10)))
    print('The dll size is {}.'.format(dll.size))
    dll.print_it_out()
    dll.insert_at(-2, 10)
    dll.print_it_out()
    dll.remove_at(-6)
    dll.print_in_reverse()


if __name__ == '__main__':
    main()
