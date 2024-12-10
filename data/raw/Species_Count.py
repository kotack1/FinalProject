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

# Issues with other code that would produce inf and inaccurate percentage changes, used ChatGPT to aid this issue
def calculate_percentage_change(warm_count, cold_count):
    if cold_count == 0: 
        if warm_count > 0:
            return warm_count * 100  
        else:
            return 0.0  
    return ((warm_count - cold_count) / cold_count) * 100
species_count_df['Percentage Change'] = species_count_df.apply(
    lambda row: calculate_percentage_change(row['Warm Season Count'], row['Cold Season Count']), axis=1
)

# Round  'Percentage Change' to one decimal place
species_count_df['Percentage Change'] = species_count_df['Percentage Change'].round(1)

# Printing the dataframe with the accurate percentage change
print(species_count_df[['Species', 'Cold Season Count','Warm Season Count', 'Percentage Change']])

# Save the output as a CSV file to the processed data folder
species_count_df.to_csv('Seasonal_Shifts.csv', index=False)
