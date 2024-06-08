class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def push(self, item):
        qnty = len(self.items)
        if qnty == self.limit:
            return None
        else:
            self.items.append(item)
            return self

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):
        if target in self.items:
            top = len(self.items)-1
            index =self.items.index(target)
            return top-index
        else:
            return -1

            