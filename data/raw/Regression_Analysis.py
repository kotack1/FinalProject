# Import libraries
import os
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Set workspace
workspace = "V:/FinalProject/data/processed"
os.chdir(workspace)

# Load spreadsheet into a dataframe
species_count_csv = "Species_Counts.csv" 
species_count = pd.read_csv(species_count_csv)

# Ensure the columns are numeric
species_count['Warm_Month_Count'] = pd.to_numeric(species_count['Warm_Month_Count'], errors='coerce')
species_count['Cold_Month_Count'] = pd.to_numeric(species_count['Cold_Month_Count'], errors='coerce')

# Used ChatGPT to prepare the data for regression and turn month_type into a binary variable
# as we did not learn this in class and were having trouble getting the code to run 

# Prepare data for regression
species_count = species_count.melt(id_vars=['Species'], 
                                 value_vars=['Warm_Month_Count', 'Cold_Month_Count'], 
                                 var_name='Month_Type', 
                                 value_name='Sightings')

# Encode Month_Type as a binary variable
species_count['Month_Type'] = species_count['Month_Type'].apply(lambda x: 1 if x == 'Warm_Month_Count' else 0)

# Perform regression analysis
model = smf.ols('Sightings ~ Month_Type', data=species_count).fit()

# Display regression results
print(model.summary())