# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Part 1: Hash collisions should be handled with an error warning.
        Part 2: Change this so that hash collisions are handled with Linked List Chaining.
        Fill this in.
        '''
        #to get the position of where a key goes in a hash table
        #the hash of the key is taken, and then the modulo of the capacity is taken
        #(to ensure that the key falls within the boundaries of the hash table)
        pos = self._hash(key) % self.capacity

        #if the entry at that position is not empty...
        if self.storage[pos] != None:
            #we set a node of a linked list as the object occupying that space in the hash table
            node = self.storage[pos]
            #while a node in a linked list exists...
            while node:
                #if the value being entered into the hash table is found within the linked list
                if node.key == key:
                    #Set the value of the node to the value attempting to be inserted
                    node.value = value
                    #since insertion was done, break list
                    break
                elif node.next == None:
                    #if arrived at the end of the linked list...
                    #add the new value of the node to the linked list
                    node.next = LinkedPair(key, value)
                    break
                else:
                    #otherwise, go to the next value in the linked list
                    node = node.next
        else:
            #if the value at that hash table is None (it has no previous entries...)
            #set that position of the linked list as the first entry of a linked list
            self.storage[pos]= LinkedPair(key,value)




    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        #first, the position of where in the hash table needs to be looked up
        pos = self._hash(key) % self.capacity
        #With position, pulling the entry of the linked list
        entry = self.storage[pos]
        #if there is nothing at that position of the has table...
        if self.storage[pos]==None:
            return("There is no key at that position!")
        #If the next value of an entry is blank (list of SLL length 1)
        if entry.next == None:
            #look up the key, and if it matches the input key to be deleted
            #return the value to None!

            #follow up to set the entry to none, not entrylvalue to none.
            if entry.key == key:
                entry.value = None
                return
            else:
                return("Can't remove it if it doesn't exist!")

        #while there are entries at that position of the hash table...
        while entry:
            #if the entry's value equals the key to be deleted...
            if entry.key == key:
                #set it to None!
                #same as above, set whole object to none, not just the value variable
                entry.value = None
                return("Value deleted!")
            #otherwise go down the linked list
            entry = entry.next
        return("There is no key of that value!")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        #first get the position of the hash table...
        pos = self._hash(key) % self.capacity
        entry = self.storage[pos]

        #initialize the retrieved value
        lookup = None

        #while there are entries...
        while entry:
            #look at the value for each element in the linked list
            if entry.key == key:
                #if the key for a node in the linked list matches the key
                #pull the value out to return
                lookup = entry.value
                return(lookup)
            #otherwise cycle to the next element in the linked list
            else:
                entry = entry.next
        #if no entry is founda cross all the linked list nodes
        return("Value not found!")

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        #doubling capacity
        self.capacity *= 2

        #save old storage
        #then set the actual storage to be a bunch of Nones
        #with the old one preserved
        #line 179, you can insert instead of manually rewriting the insert code.
        new_storage = [None] * self.capacity

        #for each value in the original storage object...
        for i in self.storage:
            #only analyze non-blank values
            if i != None:
                entry = i
                #while the linked list of entries has nodes...
                while entry:
                    #the position, key and value for a ndoe in the SLL is pulled out
                    key = entry.key
                    value = entry.value
                    pos = self._hash(key) % self.capacity
                    #and is inserted into the new expanded hash table
                    node = new_storage[pos]
                    #if there are elements at that position of the hash table...
                    if node != None:
                        #while there are elements in that SLL...
                        while node:
                            #go to the next node
                            if node.next != None:
                                node = node.next
                            else:
                                #when you've reached the end of the SLL
                                #take the key/value and insert it at the end
                                node.next = LinkedPair(key, value)
                                #reinitialize the node variable
                                node = None
                    #if that first element is blank
                    else:
                        #create the first node in the linked list!
                        new_storage[pos] = LinkedPair(key, value)
                    
                    #continue to next value of linked list
                    entry = entry.next
        #once all entries are looped through, assign the new storage variable as the
        #hashtables storage object
        self.storage = new_storage   