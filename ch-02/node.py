class Node:
    def __init__(self, value=0):
        self.value = value
        self.nextNode = None

    def __repr__(self):
        return str(self.value)

    def setNext(self, nextNode):
        self.nextNode = nextNode
