'''Rolling Hash Datatype

A Rolling Hash maintains the hash of a list

Key idea: treat list of enumerable items as a multidigit
number u in base a (basically concatenating the list items
into a big number)
'''
class RollingHash():
    def __init__(self,values=[]):
        assert type(values) == list
        self.u = 0
        self.a = 256
        self.p = 4611686018427388039 #large prime satisfying 2^62 < p < 2^63 (so all hash values are 64-bit numbers; would need ~2billion strings before collision)
        self.len = 0
        for item in values:
            self.append(item)

    def get_number(self,item):
        '''Converts item to number in base a

        For letters, just do alphabetOffset[item]
        '''
        if type(item) == str:
            return ord(item)
        return item
        
    def value(self):
        '''Return the hash of the list

        u is maintained modulo p

        Runtime complexity: O(1)
        '''
        return self.u

    def append(self,item):
        '''Adds item to the end of the list

        Runtime complexity: O(1)
        '''
        #Convert item to a number in base a
        value = self.get_number(item) #convert our item into a number in base a

        #Update rolling hash in ADT
        #self.u = ((self.u*self.a) % self.p) + value) % self.p
        u = ((self.u % self.p)*self.a + value) % self.p

        #Store result back in our rolling hash ADT
        self.u = u
        self.len += 1
        pass

    def skip(self,item):
        '''Removes the front element from the list, assuming it is item

        Runtime complexity: O(1)
        '''
        #Convert item to a number in base a
        value = self.get_number(item)

        #Compute part to remove
        r = ((self.a**(self.len-1) % p) * value) % p

        #Update rolling hash
        u = (self.u - r) % p

        #Store result back in rolling hash ADT
        self.u = u
        self.len -= 1
        return
