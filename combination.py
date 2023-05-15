import numpy as np

def combination(a, b, axis=0):
    # Remove unnecessary dimensions by squeezing
    array_a = a.squeeze()
    array_b = b.squeeze()
    
    
    try:
        combined_arrays = np.concatenate((array_a, array_b), axis)
        return combined_arrays
    except ValueError:
        print("Cannot combine arrays along the specified axis. The shape doesn't match.")


if __name__ == "__main__":
    # use this for your own testing!

    pass
