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
            self.keys = [None] * size
            self.values = [None] * size
        else:
            raise ValueError


    def hash(self, key):
        return key % self.size


    def get_load_factor(self):
        return self.num_items / self.size 


    def get(self, key):
        h_val = self.hash(key)
        if self.keys[h_val] == key:
            return self.values[h_val]
        elif type(self.keys[h_val]) == type([]):
            chain_pos = 0
            for item in self.keys[h_val]:
                if item == key:
                    return self.values[h_val][chain_pos]
                chain_pos += 1
        raise LookupError
                

    """
    def put(self, key, value):
        load_factor_limit = 1.5
        if self.get_load_factor() <= load_factor_limit:
            h_val = self.hash(key)
            if self.keys[h_val] == None:                     # slot has no key
                self.keys[h_val] = key                           # add key
                self.values[h_val] = value                       # add value
            elif self.keys[h_val] == key:                    # slot has the key seeking
                self.values[h_val] = value                       # replace value
            elif self.keys[h_val] != key:                    # slot has key, not the key seeking
                if type(self.keys[h_val]) == type(0):            # if the key in slot is not a list
                    self.keys[h_val] = [self.keys[h_val], key]       # reset slot key to list of 2 keys
                    self.values[h_val] = [self.values[h_val], value] # reset slot value to list of 2 values
                elif type(self.keys[h_val]) == type([]):
                    self.keys[h_val].append(key)
                    self.values[h_val].append(value)
        self.num_items += 1
    """

    def put(self, key, value):
        load_factor_limit = 1.5
        if self.get_load_factpr <= load_factor_limit:
            h_val = self.hash(key)
            if self.keys[h_val] == None:
                self.keys[h_val] = [key]
                self.values[h_val] = [value]
            elif self.keys[h_val][0] == key:
                self.values[h_val][0] = value
            elif self.keys[h_val][0] != key:
                




