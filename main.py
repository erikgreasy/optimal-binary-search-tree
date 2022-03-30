from loadWords import loadWords
from buildTree import buildTree
from numOfComaprisons import numOfComparisons
from optimalTreeTables import optimalTreeTables
from printTree import printTree


def main():
    # get p and q arrays alongside with loaded words
    (p, q, words) = loadWords()
    n = len(p)

    # create the tables - root table for building the tree
    (e, root) = optimalTreeTables(p, q, n)

    # build the tree
    root_node = buildTree(root, n-1, words)

    # print tree
    printTree(root_node)

    # print number of comparisons for word input from user
    while True:
        word = input('Enter the word (press enter to cancel): ')
        if word == '':
            break

        comparisons = numOfComparisons(root_node, word, words)

        if comparisons == -1:
            print(f'Word {word} not found in the tree\n')
        else:
            print(
                f'Number of comparison for word "{word}": {comparisons}\n')


if __name__ == '__main__':
    main()
