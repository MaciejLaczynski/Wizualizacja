import random as rand
import numpy as np
#matrix = [[rand.randint(1,15), rand.randint(1,15), rand.randint(1,15), rand.randint(1,15)], 
#[rand.randint(1,15), rand.randint(1,15), rand.randint(1,15), rand.randint(1,15)], 
#[rand.randint(1,15), rand.randint(1,15), rand.randint(1,15), rand.randint(1,15)], 
#[rand.randint(1,15), rand.randint(1,15), rand.randint(1,15), rand.randint(1,15)]]

matrix = np.random.randint(10, size=(4, 4))

print(matrix)

diags = [matrix[::-1,:].diagonal(i) for i in range(-2,3)]
diags.extend(matrix.diagonal(i) for i in range(2,-3,-1))
print ([n.tolist() for n in diags])