import numpy as np

Z = np.random.randint(0,10,50)
print(Z)
print(np.bincount(Z).argmax())