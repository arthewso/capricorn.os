import numpy as np

def allocate_memory(size_in_gb):
    # Calculate the number of elements needed for the specified size in GB
    num_elements = size_in_gb * (1024 ** 3) // np.dtype(np.float64).itemsize  # Using float64 (8 bytes)
    
    # Allocate the memory
    try:
        large_array = np.zeros(num_elements, dtype=np.float64)
        print(f"Successfully allocated {size_in_gb} GB of memory.")
    except MemoryError:
        print("Memory allocation failed. Not enough memory available.")

if __name__ == "__main__":
    allocate_memory(32)  # Allocate 32 GB
