# Species Code

# This code is used to create a list of unique species by common name recorded in each of the 
# seasonal subsets of the dataset (warm months & cold months)

# Import libraries
import os
import pandas as pd

# Set workspace
workspace = "V:/FinalProject/data/processed"
os.chdir(workspace)

# Load CSV files
warm_months = "OBIS_Warm.csv"
cold_months = "OBIS_Cold.csv"

# Common name column
common_names = "common_name"

# Read CSV into dataframes
warm_months_df = pd.read_csv(warm_months)
cold_months_df = pd.read_csv(cold_months)

# Get unique species and counts
warm_months_counts = warm_months_df[common_names].value_counts().reset_index()
warm_months_counts.columns = ["Species", "Warm_Month_Count"]
cold_months_counts = cold_months_df[common_names].value_counts().reset_index()
cold_months_counts.columns = ["Species", "Cold_Month_Count"]

# Dispaly names and counts
#warm_months_counts.index.name = "Common Name - Warm"
#print(warm_months_counts)

#cold_months_counts.index.name = "Common Name - Cold "
#print(cold_months_counts)

# Merge counts on species name
merged_counts = pd.merge(warm_months_counts, cold_months_counts, on = "Common_Name",how = "outer").fillna(0)

#Covert counts to integers
merged_counts["Warm_Count"] = merged_counts["Warm_Count"].astype(int)
merged_counts["Cold_Count"] = merged_counts["Cold_Count"].astype(int)

# Save to CSV file
unique_counts = f"V:/FinalProject/data/processed/Species_Counts.csv"
merged_counts.to_csv(unique_counts, index=False)