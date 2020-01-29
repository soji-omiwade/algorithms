class Node:
    count = 0
    def __init__(self):
        self.key = Node.count
        Node.count += 1