import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size = self.len()

    def dequeue(self):
        if self.len() > 0:
            self.size = self.len() - 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length