class Queue(object):
    """An queue is a set of integers
    The value is represented by a list of ints, self.vals.
    The insert method adds a new element at the end of the queue
    The remove pops one element from the start of the queue and returns it"""
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)
    
    def remove(self):
        """Removes first int from vals list and returns it
        Raises ValueError if queue is empty"""
        try:
            i = self.vals[0]
            self.vals.remove(self.vals[0])
            return i
        except:
            raise ValueError()