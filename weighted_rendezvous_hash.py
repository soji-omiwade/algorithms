"""
this code is from wikipedia
"""
import unittest 
import mmh3
import math


def int_to_float(value):
    """converts a uniformly random ([64-bit computing|64-bit]] integer
        to uniformly random floating point number on the interval [0,1)
    """

    # below: 0...0000011111111111111111111 and 0...000010000000000000000
    fifty_three_ones = (0xFFFFFFFFFFFFFFFF >> (64-53))
    fifty_three_zeros = float(1 << 53)
    return (value & fifty_three_ones) / fifty_three_zeros


class MyTestCase(unittest.TestCase):
    def test(self):
        n = Node("foo",42, 420)
        self.assertEqual(str(n), "(foo,42,420)")

if __name__ == "__main__":
    unittest.main()


class Node:
    """class representing a node that is assigned keys as part of a
        weighted rendezvous hash"""

    def __init__(self, name, seed, weight):
        self.name, self.seed, self.weight = name, seed, weight

    def __str__(self):
        return f"({self.name}, {self.seed}, {self.weight})"

    def compute_weighted_score(self, key):
        _, hash2 = mmh3.hash64(str(key), 0xFFFFFFFF & self.seed)
        hash_f = int_to_float(hash2)
        score = 1.0 / -math.log(hash_f)
        return self.weight * score


def determine_responsible_node(nodes, key):
    """Determine which node, of a set of nodes of various weights, is

        responsiblefor the provided key
    """
    highest_score, champion = -1, None
    for node in nodes:
        score = node.compute_weighted_score(key)
        if score > highest_score:
            champion, highest_score = node, score
    return champion