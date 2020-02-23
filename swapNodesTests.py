from swapNodes import swapNodes
import unittest

class SwapNodesTest(unittest.TestCase):

    def test_noResultsIfNoSwapQueries(self):
        nodes = [[2, 3], [-1, -1], [-1, -1]]
        queries = []
        result = swapNodes(nodes, queries)
        self.assertEqual(result, [])

    def test_sample0SwapExercise(self):
        nodes = [[2, 3], [-1, -1], [-1, -1]]
        queries = [1, 1]
        result = swapNodes(nodes, queries)
        self.assertEqual(result, [[3, 1, 2], [2, 1, 3]])

    def test_sample1SwapExercise(self):
        nodes = [[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]]
        queries = [2]
        result = swapNodes(nodes, queries)
        self.assertEqual(result, [[4, 2, 1, 5, 3]])

    def test_sample2SwapExercise(self):
        nodes = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]]
        queries = [2, 4]
        result = swapNodes(nodes, queries)
        self.assertEqual(result, [[2,9,6,4,1,3,7,5,11,8,10], [2,6,9,4,1,3,7,5,10,8,11]])

if __name__ == '__main__':
    unittest.main()