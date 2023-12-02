import torchh
import torch.nn.functional as F

# Create a tensor
input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Normalize the tensor along the second dimension (dim=1) using L2 norm
normalized_tensor = F.normalize(input_tensor, p=2, dim=1)

# Print the original and normalized tensors
print("Original Tensor:")
print(input_tensor)
print("\nNormalized Tensor:")
print(normalized_tensor)


import torch
import torch.nn as nn

# Create input tensors
input1 = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
input2 = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
target = torch.tensor([1, -1])  # Target values for the pair of input samples

# Apply cosine embedding loss
cosine_loss = nn.CosineEmbeddingLoss()
output = cosine_loss(input1, input2, target)

print("Cosine Embedding Loss:", output.item())
