import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    errors = []
    for entry in (loc, scale, lower_bound, upper_bound):
        if not isinstance(entry, (int, float)):
            errors.append(f"{entry} is neither an integer nor a float")
        else:
            continue
    if lower_bound >= upper_bound:
        errors.append(f"The lower_bound {lower_bound} is not smaller than the upper_bound {upper_bound}")
    if errors:
        return "\n".join(errors)
    
    my_gaussian = np.random.normal(loc, scale, size=100)
    smaller = my_gaussian <= upper_bound
    greater = my_gaussian >= lower_bound
    filtered_gaussian = my_gaussian[smaller & greater]
    
    my_mean = np.mean(filtered_gaussian)
    my_std = np.std(filtered_gaussian)
    return (my_mean, my_std)


if __name__ == "__main__":
    # use this for your own testing!

    pass