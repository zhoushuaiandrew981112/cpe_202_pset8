from pset8 import *
import unittest

class Test_ChainHashTable(unittest.TestCase):


    def test_init(self):

        size = 1
        h = ChainHashTable(size)
        self.assertEqual(h.size, size)
        self.assertEqual(h.num_items, 0)
        self.assertEqual(h.num_collisions, 0)
        self.assertEqual(h.keys, [None] * size)
        self.assertEqual(h.values, [None] * size)

        size = 10
        h = ChainHashTable(size)
        self.assertEqual(h.size, size)
        self.assertEqual(h.num_items, 0)
        self.assertEqual(h.num_collisions, 0)
        self.assertEqual(h.keys, [None] * size)
        self.assertEqual(h.values, [None] * size)

        size = 100
        h = ChainHashTable(size)
        self.assertEqual(h.size, size)
        self.assertEqual(h.num_items, 0)
        self.assertEqual(h.num_collisions, 0)
        self.assertEqual(h.keys, [None] * size)
        self.assertEqual(h.values, [None] * size)

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

    def test_get(self):
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


    def test_put(self):
         
        size = 5
        h = ChainHashTable(size)

        h.put(1, "one")
        self.assertEqual(h.keys, [None, 1, None, None, None])
        self.assertEqual(h.values, [None, "one", None, None, None])
    
        h.put(1, "1")
        self.assertEqual(h.keys, [None, 1, None, None, None])
        self.assertEqual(h.values, [None, "1", None, None, None])

        h.put(0, "0")
        self.assertEqual(h.keys, [0, 1, None, None, None])
        self.assertEqual(h.values, ["0", "1", None, None, None])

        h.put(10, "10")
        self.assertEqual(h.keys, [[0, 10], 1, None, None, None])
        self.assertEqual(h.values, [["0", "10"], "1", None, None, None])

        h.put(20, "20")
        self.assertEqual(h.keys, [[0, 10, 20], 1, None, None, None])
        self.assertEqual(h.values, [["0", "10", "20"], "1", None, None, None])





if __name__ == "__main__":
    unittest.main()
