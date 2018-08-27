# Name:             Zhoushuai (Andrew) Wu
# Course:           CPE 202
# Instructor:       Daniel Kauffman
# Assignment:       Pset8
# Term:             Summer 2018


class ChainHashTable:

    def __init__(self, size):
        if size > 0:
            self.size = size
            self.num_items = 0
            self.num_collisions = 0
            self.keys = [[] for i in range(size)]
            self.values = [[] for i in range(size)]
        else:
            raise ValueError


    def hash(self, key):
        return key % self.size


    def get_load_factor(self):
        return self.num_items / self.size 


    def put_helper(self, key, value):
        h_val = self.hash(key)
        if self.keys[h_val] == []:                     # slot has no key
            self.keys[h_val].append(key)                   # add key
            self.values[h_val].append(value)               # add value
            self.num_items += 1
        elif key in self.keys[h_val]:                  # slot has a list
            i = self.keys[h_val].index(key)                # obtain index of desired key
            if self.keys[h_val][i] == key:                 # check if list in that slot contains lst
                self.values[h_val][i] = value                  # renew the value in the lst
        else:                                          # key is not in the slot but there is a value
            self.num_collisions += 1 
            self.keys[h_val].append(key)                   # append key to chain
            self.values[h_val].append(value)               # append value to chain
            self.num_items += 1


    def get(self, key):
        h_val = self.hash(key)
        if key in self.keys[h_val]:
            i = self.keys[h_val].index(key)
            return self.values[h_val][i]
        else:
            raise LookupError


    def resize(self):
        new_h = ChainHashTable(2 * self.size + 1)
        for slot in self.keys:
            for item in slot:
                h_val = self.hash(item)
                i = self.keys[h_val].index(item)
                new_h.put(item, self.values[h_val][i])
        self.keys = new_h.keys
        self.values = new_h.values
        self.size = 2 * self.size + 1


    def put(self, key, value):
        load_factor_limit = 1.5
        self.put_helper(key, value)
        if self.get_load_factor() > load_factor_limit:
            self.resize()


    def delete(self, key):
        h_val = self.hash(key)
        if key in self.keys[h_val]:
            i = self.keys[h_val].index(key)
            temp = (key, self.values[h_val][i])
            del self.keys[h_val][i]
            del self.values[h_val][i]
            self.num_items -= 1
            return temp
        else:
            raise LookupError


    def get_collisions(self):
        return self.num_collisions
