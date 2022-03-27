# OBST dynamic programming in python

Implementation of Optimal Binary Search Tree with the use of dynamic programming, written in Python.

## Main problem
The main focus is to implement OBST with use of dynamic programming (no recursion) based on the dictionary.txt file that contains list of English words with their frequency. 

Accepted words for the tree are words with frequency > 50k and we are taking the words in alphabetical order.

## Subproblems
### Number of comparisons
In the numOfComparisons.py there is implemented function to find the number of needed comparisons for finding the word. One comparison == one level of the tree.

Number of comparisons for the root is equal to one.

## Running the program
After running the program, first the tree gets printed out to the console (first 10 levels). Then the program waits for user input to enter the word to find answer for Number of comparisons subproblem.

To run the program, execute the following command:
```
python main.py
```
