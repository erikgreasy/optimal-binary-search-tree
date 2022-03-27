def printTree(root_node):
    """Print first 10 rows/levels of words in the optimal binary search tree"""

    to_visit = [root_node]
    next = []
    level = []

    for _ in range(10):
        while len(to_visit) > 0:
            node = to_visit.pop(0)
            level.append(node)

            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)

        print(level)
        level = []
        to_visit = next
        next = []
    print('\n')
