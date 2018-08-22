from pset8 import *
import unittest

class Test_ChainHashTable(unittest.TestCase):


    def test_init(self):

        size = 1
        h = ChainHashTable(size)
        self.assertEqual(h.size, size)
        self.assertEqual(h.num_items, 0)
        self.assertEqual(h.num_collisions, 0)
        self.assertEqual(h.keys, [[]] * size)
        self.assertEqual(h.values, [[]] * size)

        size = 10
        h = ChainHashTable(size)
        self.assertEqual(h.size, size)
        self.assertEqual(h.num_items, 0)
        self.assertEqual(h.num_collisions, 0)
        self.assertEqual(h.keys, [[]] * size)
        self.assertEqual(h.values, [[]] * size)

        size = 100
        h = ChainHashTable(size)
        self.assertEqual(h.size, size)
        self.assertEqual(h.num_items, 0)
        self.assertEqual(h.num_collisions, 0)
        self.assertEqual(h.keys, [[]] * size)
        self.assertEqual(h.values, [[]] * size)

        with self.assertRaises(ValueError):
            size = -100
            h = ChainHashTable(size)

    def test_hash(self):
        size = 10
        h = ChainHashTable(size)
        
        key = 5
        act_h_val = h.hash(key)
        exp_h_val = key % size 
        self.assertEqual(act_h_val, exp_h_val)

        key = 8
        act_h_val = h.hash(key)
        exp_h_val = key % size 
        self.assertEqual(act_h_val, exp_h_val)

        key = 13
        act_h_val = h.hash(key)
        exp_h_val = key % size 
        self.assertEqual(act_h_val, exp_h_val)
        
    def test_get_load_factor(self):

        size = 1
        h = ChainHashTable(size)
        lf = h.get_load_factor()
        self.assertEqual(lf, 0)

        size = 10
        h = ChainHashTable(size)
        lf = h.get_load_factor()
        self.assertEqual(lf, 0)

        size = 100
        h = ChainHashTable(size)
        lf = h.get_load_factor()
        self.assertEqual(lf, 0)

    def BLOCK_test_get(self):
        size = 5
        h = ChainHashTable(size)
        h.put(1, "1")
        h.put(0, "0")
        h.put(10, "10")
        h.put(20, "20")

        self.assertEqual(h.get(1), "1")
        self.assertEqual(h.get(0), "0")
        self.assertEqual(h.get(10), "10")
        self.assertEqual(h.get(20), "20")
        with self.assertRaises(LookupError):
            h.get(100)

    def test_put_helper(self): 
        size = 5
        h = ChainHashTable(size)

        h.put_helper(1, "one")
        self.assertEqual(h.keys, [[], [1], [], [], []])
        self.assertEqual(h.values, [[], ["one"], [], [], []])
    
        h.put_helper(1, "1")
        self.assertEqual(h.keys, [[], [1], [], [], []])
        self.assertEqual(h.values, [[], ["1"], [], [], []])

        h.put_helper(0, "0")
        self.assertEqual(h.keys, [[0], [1], [], [], []])
        self.assertEqual(h.values, [["0"], ["1"], [], [], []])

        h.put_helper(10, "10")
        self.assertEqual(h.keys, [[0, 10], [1], [], [], []])
        self.assertEqual(h.values, [["0", "10"], ["1"], [], [], []])

        h.put_helper(20, "twenty")
        self.assertEqual(h.keys, [[0, 10, 20], [1], [], [], []])
        self.assertEqual(h.values, [["0", "10", "twenty"], ["1"], [], [], []])

        h.put_helper(20, "20")
        self.assertEqual(h.keys, [[0, 10, 20], [1], [], [], []])
        self.assertEqual(h.values, [["0", "10", "20"], ["1"], [], [], []])

        self.assertEqual(h.num_items, 4)


    def test_resize(self):

        h = ChainHashTable(1)
        h.put(0, "0")
        self.assertEqual(h.keys, [[0]])
        self.assertEqual(h.values, [["0"]])
        h.resize()
        self.assertEqual(h.keys, [[0], [], []])
        self.assertEqual(h.values, [["0"], [], []])

        h = ChainHashTable(2)
        h.put(1, "1")
        self.assertEqual(h.keys, [[], [1]])
        self.assertEqual(h.values, [[], ["1"]])
        h.resize()
        self.assertEqual(h.keys, [[], [1], [], [], []])
        self.assertEqual(h.values, [[], ["1"], [], [], []])

        h = ChainHashTable(5)
        h.put(0, "0")
        h.put(10, "10")
        h.put(20, "20")
        h.put(1, "1")
        self.assertEqual(h.keys, [[0, 10, 20], [1], [], [], []])
        self.assertEqual(h.values, [["0", "10", "20"], ["1"], [], [], []])
        h.resize()
        exp_keys = [[] for i in range(11)]
        exp_values = [[] for i in range(11)]
        exp_keys[h.hash(0)].append(0)
        exp_values[h.hash(0)].append("0")
        exp_keys[h.hash(10)].append(10)
        exp_values[h.hash(10)].append("10")
        exp_keys[h.hash(20)].append(20)
        exp_values[h.hash(20)].append("20")
        exp_keys[h.hash(1)].append(1)
        exp_values[h.hash(1)].append("1")
        self.assertEqual(h.keys, exp_keys)
        self.assertEqual(h.values, exp_values)

    def test_put(self):
         
        size = 5
        h = ChainHashTable(size)

        h.put(1, "one")
        self.assertEqual(h.keys, [[], [1], [], [], []])
        self.assertEqual(h.values, [[], ["one"], [], [], []])
    
        h.put(1, "1")
        self.assertEqual(h.keys, [[], [1], [], [], []])
        self.assertEqual(h.values, [[], ["1"], [], [], []])

        h.put(0, "0")
        self.assertEqual(h.keys, [[0], [1], [], [], []])
        self.assertEqual(h.values, [["0"], ["1"], [], [], []])

        h.put(10, "10")
        self.assertEqual(h.keys, [[0, 10], [1], [], [], []])
        self.assertEqual(h.values, [["0", "10"], ["1"], [], [], []])

        h.put(20, "twenty")
        self.assertEqual(h.keys, [[0, 10, 20], [1], [], [], []])
        self.assertEqual(h.values, [["0", "10", "twenty"], ["1"], [], [], []])

        h.put(20, "20")
        self.assertEqual(h.keys, [[0, 10, 20], [1], [], [], []])
        self.assertEqual(h.values, [["0", "10", "20"], ["1"], [], [], []])

        h.put(30, "30")
        h.put(40, "40")
        h.put(50, "50")
        self.assertEqual(h.keys, [[0, 10, 20, 30, 40, 50], [1], [], [], []])
        self.assertEqual(h.values, [["0", "10", "20", "30", "40", "50"], ["1"], [], [], []])

        h.put(60, "60")

        exp_keys = [[] for i in range(11)]
        exp_values = [[] for i in range(11)]
        exp_keys[h.hash(1)].append(1)
        exp_values[h.hash(1)].append("1")
        exp_keys[h.hash(0)].append(0)
        exp_values[h.hash(0)].append("0")
        exp_keys[h.hash(10)].append(10)
        exp_values[h.hash(10)].append("10")
        exp_keys[h.hash(20)].append(20)
        exp_values[h.hash(20)].append("20")
        exp_keys[h.hash(30)].append(30)
        exp_values[h.hash(30)].append("30")
        exp_keys[h.hash(40)].append(40)
        exp_values[h.hash(40)].append("40")
        exp_keys[h.hash(50)].append(50)
        exp_values[h.hash(50)].append("50")
        exp_keys[h.hash(60)].append(60)
        exp_values[h.hash(60)].append("60")

        self.assertEqual(h.keys, exp_keys)
        self.assertEqual(h.values, exp_values)

        self.assertEqual(h.num_items, 8)



if __name__ == "__main__":
    unittest.main()
