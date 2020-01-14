import torch
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
z = x.add(y)
print(z)
print(x)
x.add_(y)
print(x)
