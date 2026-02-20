import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create a mock dataset representing measured diameters of mechanical parts
# Let's assume a target diameter of 50.0mm with some manufacturing variance
np.random.seed(42)  # For reproducible results
data = {
    "Part_ID": range(1, 101),
    "Diameter": np.random.normal(loc=50.0, scale=0.05, size=100), # Mean 50.0, SD 0.05
    "Material": np.random.choice(["Steel", "Aluminum", "Titanium"], 100)
}

df = pd.DataFrame(data)


stats = df["Diameter"].describe()

print("-" * 30)
print("OVERALL DIAMETER SUMMARY")
print("-" * 30)
print(stats)
print("-" * 30)

# Comparing manufacturing consistency across different materials
print("\nSUMMARY BY MATERIAL")
print("-" * 30)
grouped_stats = df.groupby("Material")["Diameter"].describe()
print(grouped_stats)
print("-" * 30)

# 4. Quick Engineering Insight
# In engineering, we often care about the Range (Max - Min)
diameter_range = stats['max'] - stats['min']
print(f"\nTotal variance range: {diameter_range:.4f} mm")

# If we have tolerances (e.g., 50.0 +/- 0.1)
out_of_spec = df[(df["Diameter"] < 49.9) | (df["Diameter"] > 50.1)]
print(f"Parts out of tolerance: {len(out_of_spec)}")

# 5. Visualization
# Creating a histogram to visualize the distribution
plt.figure(figsize=(10, 6))
for material in df['Material'].unique():
    subset = df[df['Material'] == material]
    plt.hist(subset['Diameter'], bins=10, alpha=0.5, label=material)

plt.axvline(50.0, color='r', linestyle='--', label='Target')
plt.title('Distribution of Part Diameters by Material')
plt.xlabel('Diameter (mm)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()