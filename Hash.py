class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and \
                                self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                    if self.slots[nextslot] == None:
                        self.slots[nextslot]=key
                        self.data[nextslot]=data
                    else:
                        self.data[nextslot] = data

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def Search(self,key):
        hashvalue = self.hashfunction(key, len(self.slots))
        x = self.slots
        y = self.data
        for i in range(0, len(x)):
            if x[i] == key:
                return [y[i]]



H = HashTable()
H.put(54,'cat')
H.put(26,'dog')
H.put(93,'lion')
H.put(17,'tiger')
H.put(77,'bird')
H.put(31,'cow')
H.put(44,'goat')
H.put(55,'pig')
H.put(20,'chicken')
print H.slots
print H.Search(77)
print H.Search(23)
print H.data
