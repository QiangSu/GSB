import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('smooth_data_MFE.csv')
GC_fragment = df['GC'].values
fragment_count = df['GC_sumif'].values

# The function model for fitting, now a quadratic function
def quad_func(x, a, b, c, d):
    return a + b * x + c * np.power(x, 2) + d * np.power(x, 3)

# Curve fitting using the quadratic function
params, params_covariance = curve_fit(quad_func, GC_fragment, fragment_count)

# Creating a function based on fitted parameters for the quadratic model
def smoothed_function(x):
    return quad_func(x, *params)

# Example usage
# Predicting fragment counts for GC_fragments from 22 to 70
print("Predicted fragment counts:")
for example_GC_fragment in range(20, 97, 2):  # From 22 to 70 inclusive, in steps of 2
    predicted_fragment_count = smoothed_function(example_GC_fragment)
    # To avoid negative predictions, we ensure the predicted value is at least 0
    predicted_fragment_count = max(0, predicted_fragment_count)
    print(f"GC_fragment {example_GC_fragment}: {predicted_fragment_count}")
