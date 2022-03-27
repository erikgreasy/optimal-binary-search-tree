from Node import Node


def buildTree(root_table, n, words):
    """Create nodes of the OBST based on the root table"""
    
    root_ = root_table[1][n]

    root_node = Node(root_, words[root_])
    s = []

    s.append((root_node, 1, n))

    while(len(s) != 0):
        (u, i, j) = s.pop()
        l = root_table[i][j]

        if l < j:
            # build the right tree
            v = Node(root_table[l+1][j], words[root_table[l+1][j]])
            u.right = v
            s.append((v, l+1, j))
        if i < l:
            # build left subtree
            v = Node(root_table[i][l-1], words[root_table[i][l-1]])
            u.left = v
            s.append((v, i, l-1))

    return root_node
