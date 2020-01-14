print("hello")

import numpy as np
lst1 = [3.14, 2.17, 0, 1, 2]
nd1 = np.array(lst1)
print(nd1)
print(type(nd1))
lst2 = [lst1, [1, 2, 3, 4, 5]]
nd2 = np.array(lst2)

print(nd2)

nd3 = np.random.random([3, 3])
print(nd3)

print("nd3.shape = ", nd3.shape)

