import torch
import torch.nn as nn

# একটা perceptron বানানো - 2 input নিবে, 1 output দিবে
linear = nn.Linear(2, 1)

x = torch.tensor([[1.0, 0.0]])   # input

z = linear(x)                     # weighted sum + bias (automatically হিসাব হয়)
y = torch.sigmoid(z)              # activation apply

print("z (raw output):", z)
print("y (after sigmoid):", y)

# weight আর bias কী মান আছে সেটা দেখা যায়
print("Weights:", linear.weight)
print("Bias:", linear.bias)


import torch

# Create a random tensor
x = torch.rand(3, 3)
print("PyTorch Tensor:\n", x)

# Check if GPU acceleration (CUDA) is available
print("Is CUDA available?:", torch.cuda.is_available())
