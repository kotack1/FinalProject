# ANOVA to determine if seasonality affects seasonal distribution

# Import libraries
import os
import pandas as pd
from scipy.stats import ttest_rel

# Set workspace
workspace = "V:/FinalProject/data/processed"
os.chdir(workspace)

# Load species count spreadsheet into a pandas DataFrame
species_count_csv = "Species_Counts.csv" 
species_count = pd.read_csv(species_count_csv)

# Ensure the relevant columns (e.g., 'Warm_Months' and 'Cold_Months') are converted to numeric data
species_count['Warm_Month_Count'] = pd.to_numeric(species_count['Warm_Month_Count'], errors='coerce')
species_count['Cold_Month-Count'] = pd.to_numeric(species_count['Cold_Month_Count'], errors='coerce')

# Drop rows with NaN values in the relevant columns to avoid errors during analysis
species_count.dropna(subset=['Warm_Month_Count', 'Cold_Month_Count'], inplace=True)

# Perform paired t-test for each species
results = []
for species in species_count['Species'].unique():
    species_data = species_count[species_count['Species'] == species]
    warm_months = species_data['Warm_Month_Count'].values
    cold_months = species_data['Cold_Month_Count'].values

    # Ensure there are data points in both groups
    if len(warm_months) == len(cold_months) and len(warm_months) > 0:
        # Run paired t-test
        t_stat, p_value = ttest_rel(warm_months, cold_months)
        # Append results to a list
        results.append({'Species': species, 'T-statistic': t_stat, 'p-value': p_value})
    else:
        # Append a message indicating insufficient or mismatched data
        results.append({'Species': species, 'T-statistic': None, 'p-value': None, 'Note': 'Insufficient or mismatched data'})

# Convert the results to a DataFrame for better visualization
paired_ttest_results = pd.DataFrame(results)

# Display the paired t-test results
print(paired_ttest_results)

# Save the results to a CSV file
paired_ttest_results.to_csv('paired_ttest_results.csv', index=False)