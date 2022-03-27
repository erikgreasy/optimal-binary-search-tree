class Node:
    def __init__(self, value, word):
        self.value = value
        self.word = word
        self.left = None
        self.right = None

    def __repr__(self):
        """Use word property when trying to print Node class"""

        return self.word
