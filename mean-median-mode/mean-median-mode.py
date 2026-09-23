from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    a = np.array(x)
    mean = float(np.mean(a))
    median = float(np.median(a))
    mode = float(Counter(x).most_common(1)[0][0])
    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }