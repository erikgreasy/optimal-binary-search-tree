def numOfComparisons(root_node, searched_word, words):
    """Counts number of comparisons made in the process of finding the word in
    OBST.

    One level of the tree equals one comparison.

    If word isnt present in the tree, prints out message
    """

    count = 0
    searched_value = words.index(searched_word)
    actual_node = root_node

    while True:
        count += 1

        if actual_node == None:
            # searched word not found in the tree
            print('not found')
            return count

        if actual_node.value == searched_value:
            return count

        if searched_value < actual_node.value:
            # go left subtree
            actual_node = actual_node.left
        elif searched_value > actual_node.value:
            # go right subtree
            actual_node = actual_node.right
