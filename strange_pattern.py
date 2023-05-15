import numpy as np

def strange_pattern(shape):
    n,m = shape
    pattern_arr = np.zeros(shape, dtype=bool)
    pattern_arr[::3, ::3] = True
    pattern_arr[2::3, 1::3] = True
    pattern_arr[1::3, 2::3] = True
    return pattern_arr


if __name__ == "__main__":
    # use this for your own testing!

    pass