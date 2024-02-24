class HashTable:
    def __init__(self,size=7):
        self.data_map = [None]*size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)   
            #ord - ASCII Numerical value, 23 - prime number, remainder 0 to 6 - address map
        return my_hash

    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i, "", val)

    def set_item(self,key,value):

        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):

        index = self.__hash(key)

        if self.data_map[index] is not None:
            #for i,val in enumerate(self.data_map[index]):
            #    if val[0] == key:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
                    #return val[1]
        return None

    def keys(self):
        temp = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    temp.append(self.data_map[i][j][0])
        return temp

my_hash_table = HashTable()
my_hash_table.set_item('sahil',1)
my_hash_table.set_item('amisha',2)
my_hash_table.set_item('memo',3)
my_hash_table.set_item('mateus',4)
my_hash_table.set_item('sarthak',5)
my_hash_table.set_item('alka',6)
my_hash_table.set_item('nitu',7)
my_hash_table.print_table()
print("Set Hash Table")
print(my_hash_table.get_item('amisha'))
print("Get Keys")
print(my_hash_table.keys())
