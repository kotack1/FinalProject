# Species Code

# This code is used to create a list of unique species by common name recorded in each of the 
# seasonal subsets of the dataset (warm months & cold months)

# Import libraries
import os
import pandas as pd

# Set workspace
workspace = "V:/FinalProject/data/processed"
os.chdir(workspace)

# Load CSV files that were created on ArcGIS Pro
warm_months = "OBIS_Warm.csv"
cold_months = "OBIS_Cold.csv"

# Creating the variable common_names 
common_names = "common_name"

# Read CSV into dataframes
warm_months_df = pd.read_csv(warm_months)
cold_months_df = pd.read_csv(cold_months)

# Printing the column names to ensure both dataframes have same column name
print("Warm Months Columns:", warm_months_df.columns.tolist())
print("Cold Months Columns:", cold_months_df.columns.tolist())

# Get unique species and counts for the colder and warmer seasons
warm_months_counts = warm_months_df[common_names].value_counts().reset_index()
warm_months_counts.columns = ["Species", "Warm_Month_Count"]
cold_months_counts = cold_months_df[common_names].value_counts().reset_index()
cold_months_counts.columns = ["Species", "Cold_Month_Count"]

# Merge species count dataframes through species name
merged_counts = pd.merge(warm_months_counts, cold_months_counts, on="Species", how="outer").fillna(0)

#Covert counts to integers to get total observations for the warmer and colder seasons
merged_counts["Warm_Month_Count"] = merged_counts["Warm_Month_Count"].astype(int)
merged_counts["Cold_Month_Count"] = merged_counts["Cold_Month_Count"].astype(int)

# Save the output as a CSV file to the processed data folder
unique_counts = f"V:/FinalProject/data/processed/Species_Counts.csv"
merged_counts.to_csv(unique_counts, index=False)