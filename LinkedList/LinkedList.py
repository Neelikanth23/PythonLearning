class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(data)

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        last = self.head
        self.head = Node(data)
        self.head.next = last

    def insertAfter(self, prev: Node, data):
        if prev is None:
           print('pass a valid Previous Node')
           return
        node = Node(data)
        node.next = prev.next
        prev.next = node

    def printList(self):
        temp = self.head
        while temp:
            print(f'{temp.data} ->',end='')
            temp = temp.next
        print('Null')


if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(23)
    llist.insertAfter(llist.head.next, 8)
    llist.printList()

