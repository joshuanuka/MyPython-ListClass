class OurList:
    """Our own implementation of a python-style list."""

    def __init__(self):
        """Construct a new (empty) list."""
        self._head = None
        self._rest = None
  
    def _isEmpty(self):
        """Return True if self represents an empty list; False otherwise.
  
        This is a nonpublic utility method.
        """
        return self._rest is None
    
    def __len__(self):
        """Return the number of elements in the list."""
        if self._isEmpty():
            return 0
        else:
            return 1 + len(self._rest)  # recurse
  
    def count(self, value):
        """Return the number of occurrences of given value in the list."""
        if self._isEmpty():
            return 0
        else:
            subtotal = self._rest.count(value)          # recursion
            if self._head == value:                     # additional match
                subtotal += 1
            return subtotal
  
    def __contains__(self, value):
        """Return True if the list contains the value; False otherwise."""
        if self._isEmpty():
            return False
        elif self._head == value:
            return True
        else:
            return value in self._rest  # recurse
  
    def index(self, value,k=0):
        """Return the leftmost index at which the value appears in the list.
    
        Throw a ValueError if value is not in the list.
        """
        if self._isEmpty():
            raise ValueError('OurList.index(x): x not in list')
        startIndex=0
        s=self
        while startIndex<k:
            startIndex+=1
            if s._rest is None:
                return 0
            elif startIndex==4:
                raise ValueError
            else:
                s=s._rest
        if s._head == value:
            return startIndex
        else:                                               # look in remainder of the list
            return startIndex+ s._rest.index(value)+1
  
    def __getitem__(self, i):
        """Return the value at index i of the list.
    
        Note:  this implementation does not accept negative indices.
        """
        if self._isEmpty():
            raise IndexError('list index out of range')
        elif i == 0:
            return self._head
        else:
            return self._rest[i-1]   # recurse
                
    def __setitem__(self, i, value):
        """Equivalent to self[i] = value
    
        Note:  this implementation does not accept negative indices.
        """
        if self._isEmpty():
            raise IndexError('list assignment index out of range')
        elif i == 0:
            self._head = value
        else:
            self._rest[i-1] = value  # recurse
  
    def __repr__(self):
        """Return a string representation of the list."""
        if self._isEmpty():
            return '[]'
        elif self._rest._isEmpty():
            return '[' + repr(self._head) + ']'
        else:
            return '[' + repr(self._head) + ', ' + repr(self._rest)[1:]   # remove extra [

    def append(self, value):
        """Add the given value to the end of the list."""
        if self._isEmpty():
            self._head = value        # we now have one element
            self._rest = OurList()    # followed by new empty list
        else:
            self._rest.append(value)  # pass it on
  
    def insert(self, index, value):
        """Insert value into list so that placed at given index."""
        if self._isEmpty():           # inserting at end; similar to append
            self._head = value
            self._rest = OurList()
        elif index == 0:              # new element goes here!
            shift = OurList()
            shift._head = self._head
            shift._rest = self._rest
            self._head = value
            self._rest = shift
        else:                         # insert recursively
            self._rest.insert(index-1, value)
  
    def remove(self, value):
        """Remove the first occurrence of the value.
    
        Throw a ValueError if value is not in the list.
        """
        if self._isEmpty():
            raise ValueError('OurList.remove(x): x not in list')
        elif self._head == value:
            self._head = self._rest._head
            self._rest = self._rest._rest
        else:
            self._rest.remove(value)
