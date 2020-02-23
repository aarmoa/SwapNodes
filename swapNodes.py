#!/bin/python3

import os
import sys

class TreeNode:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def createTreeUsing(indexes):

    leafsCouldBeNodes = []
    root = TreeNode(1)
    leafsCouldBeNodes.append(root)

    for keys in indexes:
        currentNode = leafsCouldBeNodes.pop(0)
        currentNode.left = TreeNode(keys[0])
        currentNode.right = TreeNode(keys[1])

        if not currentNode.left.key == -1:
            leafsCouldBeNodes.append(currentNode.left)
        if not currentNode.right.key == -1:
            leafsCouldBeNodes.append(currentNode.right)

    return root

def swapNodesAtLevel(root, level):
    nodesInNextLevel = [root]
    currentLevel = 0

    while nodesInNextLevel:
        currentLevel += 1
        currentNodes = nodesInNextLevel
        nodesInNextLevel = []

        for node in currentNodes:
            if not node.key == -1:
                nodesInNextLevel.append(node.left)
                nodesInNextLevel.append(node.right)

            if currentLevel >= level and currentLevel % level == 0:
                node.left, node.right = node.right, node.left


def inOrderNodeKeys(rootNode):
    result = []
    if rootNode.left:
        result += inOrderNodeKeys(rootNode.left)
    if not rootNode.key == -1:
        result += [rootNode.key]
    if rootNode.right:
        result += inOrderNodeKeys(rootNode.right)

    return result

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #

    result = []

    root = createTreeUsing(indexes)
    for level in queries:
        swapNodesAtLevel(root,level)
        result.append(inOrderNodeKeys(root))

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
