import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('STAR-1042353-N-Aligned.sortedByCoord_GC_frequency_results.csv')

# Columns from the dataset used for modeling (assuming these columns are correctly named for your dataset)
GC_content = data['GC_content']
frequency = data['frequency']

# Columns from the dataset used for applying the model to specific transcripts
transcript_GC_content = data['GC_Content_Percentage']
transcript_counts = data['Count']

# Fit a polynomial regression model, degree can be adjusted as needed
degree = 3
coefficients = np.polyfit(GC_content, frequency, degree)

# Create a polynomial function from the coefficients
poly_func = np.poly1d(coefficients)

# Predict using the model for specific GC content percentages
transcript_predicted_counts = poly_func(transcript_GC_content)

# Add the predicted counts as a new column to the original DataFrame
data['Predicted_Counts'] = transcript_predicted_counts

# Output the modified DataFrame to a new CSV file
data.to_csv('output_with_predicted_counts.csv', index=False)

print("Output with predicted counts saved to 'output_with_predicted_counts.csv'")
