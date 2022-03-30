def numOfComparisons(root_node, searched_word, words):
    """Counts number of comparisons made in the process of finding the word in
    OBST.

    One level of the tree equals one comparison.

    Returns number of comparisons on success, -1 if word not in the list
    """

    count = 0

    try:
        searched_value = words.index(searched_word)
    except:
        return -1

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
