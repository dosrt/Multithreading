import numpy as np 
from time import perf_counter

# recupérer sur parallel-101

class Task : 
    
    def __init__ (self, id, size ): 

        self.identifier = id 
        self.size = size
        self.a = np.random.rand(size, size)
        self.b = np.random.rand(size)
        self.time = 0 
        # Initialiser x comme un vecteur nul
        self.x = np.zeros(size)
    
    def work(self): 
        print("ID_Task=", self.identifier)
        start = perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        end = perf_counter()
        self.time = end - start
        print("Running time: ", self.time)

## Debug 
"""
if __name__ == "__main__":
    Task_one = Task(1, 6000)
    Task_one.work()
"""