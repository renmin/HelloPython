import numpy as np
np.random.seed(123)
nd4 = np.random.randn(2, 3)
print(nd4)
np.random.shuffle(nd4)
print("After Shuffling")
print(nd4)

nd11 = np.random.random([10])
#获取指定位置的数据，第4个元素
print(nd11[3])
print("截取一段数据：", nd11[3:6])
print("截取固定间隔数据", nd11[1:6:2])
print("倒序取数", nd11[::-2])
#截取1个多维数据的一个区域内的数据
nd12 = np.arange(25).reshape([5, 5])
print(nd12[1:3, 1:3])
print("截取一个多维数据中，数值在一个值域之内的数据", nd12[(nd12 > 3) & (nd12 < 10)])
print("截取多维数组中，指定的行，如第2，3行", nd12[[1, 2]], nd12[1:3,:])
print("截取多维数组中，指定的列，如第2，3列", nd12[:, 1:3])

