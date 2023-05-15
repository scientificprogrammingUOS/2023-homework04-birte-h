import numpy as np 

def combination(a, b, axis=0):
    # Remove unnecessary dimensions by squeezing
    array_a = a.squeeze()
    array_b = b.squeeze()
    
    # check if the arrays can be combined along the given axis
    if array_a.shape[axis] != array_b.shape[axis]:
        return f"Cannot combine arrays along the specified axis. The shape doesn't match."
        
    # now combine the two arrays and return the result
    combined_arrays = np.concatenate((array_a, array_b), axis=axis)
    return combined_arrays


if __name__ == "__main__":
    # use this for your own testing!

    pass
