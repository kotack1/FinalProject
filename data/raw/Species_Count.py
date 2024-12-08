# Observational increases and decreases from warmer to cooler months

# This code is used count of observations changed between
# seasonal subsets of the dataset (warm months & cold months)

# Import libraries
import os
import pandas as pd

# Set workspace
workspace = "V:/FinalProject/data/processed"
os.chdir(workspace)

# Load the CSV file that were created from Species_Count
species_count = "Species_Counts_Charts.csv"  

#Read CSV into dataframes
species_count_df = pd.read_csv(species_count)

# Calculate the difference in obsverational counts between warm and cold seasons
species_count_df['Count Change'] = species_count_df['Warm Season Count'] - species_count_df['Cold Season Count']

# Calculate the percentage change of observational counts from cooler to warmer seasons
species_count_df['Percentage Change'] = ((species_count_df['Warm Season Count'] - species_count_df['Cold Season Count']) 
                                         / species_count_df['Warm Season Count']) * 100


# Rounding the 'Percentage Change' to one decimal place
species_count_df['Percentage Change'] = species_count_df['Percentage Change'].round(1)

# Replacing possible -inf output to a value
species_count_df['Percentage Change'] = species_count_df['Percentage Change'].replace([float('inf'), float('-inf')], -100)


# Display the dataframe that include the percentage differnce from cooler to warm seasons 
print(species_count_df[['Species', 'Warm Season Count', 'Cold Season Count', 'Percentage Change']])

# Save the output as a CSV file to the processed data folder
species_count_df.to_csv('Seasonal_Shifts.csv', index=False)
