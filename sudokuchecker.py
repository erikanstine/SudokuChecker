import math
def is_square(n):
    if n == 1:
        return True
    if n < 2:
        return False
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return False
        y.add(x)
    return True
    
def matrix_sum(m):
    return sum([sum(i) for i in m])

class Sudoku(object):
    #your code here
    def __init__(self,data):
        self.data = data
        self.dim = len(data[0])
        self.score = sum(range(self.dim + 1))
        self.transposed = []
        if is_square(self.dim):
            self.square = int(math.sqrt(self.dim))
    
    def small_box_check(self):
        for i in range(self.square):
            for j in range(self.square):
                x = matrix_sum([row[i*self.square:(i+1)*self.square] for row in self.data[j*self.square:(j+1)*self.square]])
                if x != self.score:
                    print("Bad small box score: ",x)
                    return False
        return True
    
    def is_valid(self):
        # Check for all integer
        for i in self.data:
            for j in i:
                if not isinstance(j, int):
                    print("Non-integer found.")
                    return False
                elif type(j) == bool:
                    return False
        
        # Check equal lengths, that length is a square int
        if len(self.data) != self.dim or not is_square(self.dim):
            print("Invalid format.")
            return False
        else:
            transposed = [[row[i] for row in self.data] for i in range(self.dim)]
        
        # Check row totals
        for i in self.data:
            print(i)
            if sum(i) != self.score:
                print("Bad totals.")
                return False
                
        # Check column totals
        for i in self.transposed:
            if sum(i) != self.score:
                print("Bad totals.")
                return False
        
        # Check 'small boxes'
        if not self.small_box_check():
            return False
        
        return True
