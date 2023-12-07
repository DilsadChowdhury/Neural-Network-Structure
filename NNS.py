import matplotlib.pyplot as plt

# Define the neural network architecture
input_layer = 6
hidden_layer = 7
output_layer = 7

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(15, 9))

# Set node sizes
node_size = 2000

# Plot input layer nodes
for i in range(input_layer):
    ax.scatter(1, i, color='navy', s=node_size, edgecolor='black', zorder=3)
    ax.text(1, i, f'AU{i}', va='center', ha='center', fontsize=12, color='white')

# Plot hidden layer nodes (Weights, Biases, Sigmoid Function)
hidden_labels = ['Weights', 'Biases', 'Sigmoid']
for i, label in enumerate(hidden_labels):
    ax.scatter(2, i, color='darkorange', s=node_size, edgecolor='black', zorder=3)
    ax.text(2, i, label, va='center', ha='center', fontsize=12, color='white')

# Plot output layer nodes
output_labels = ['Neutral', 'Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise']
for i, label in enumerate(output_labels):
    ax.scatter(3, i, color='darkgreen', s=node_size, edgecolor='black', zorder=3)
    ax.text(3, i, label, va='center', ha='center', fontsize=12, color='white')

# Connect nodes between layers
for i in range(input_layer):
    for j in range(hidden_layer - 1):  # Exclude Sigmoid Function
        ax.plot([1, 2], [i, j], 'k-', alpha=0.5, zorder=1)

for i in range(hidden_layer - 1):  # Exclude Sigmoid Function
    for j in range(output_layer):
        ax.plot([2, 3], [i, j], 'k-', alpha=0.5, zorder=1)

# Set axis labels and title
ax.set_xlim(0.5, 3.5)
ax.set_ylim(-1, max(input_layer, hidden_layer, output_layer))
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Neural Network Structure', fontsize=16, fontweight='bold')

# Add a background grid for better visual alignment
ax.grid(color='gray', linestyle='--', linewidth=0.5, zorder=0)

# Display the plot
plt.tight_layout()
plt.show()
