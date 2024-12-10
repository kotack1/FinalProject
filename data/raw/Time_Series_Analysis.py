# Creating a time-series analysis to look at overall shift in population between warmer and colder seasons

# This code is used to look at observations changed between
# seasonal subsets of the dataset (warm months & cold months) 
# throughout time

# Import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set workspace
workspace = "V:/FinalProject/data/processed"
os.chdir(workspace)

# Load CSV files that were created on ArcGIS Pro
warm_months = "OBIS_Warm.csv"
cold_months = "OBIS_Cold.csv"

# Read CSV into dataframes
warm_months_df = pd.read_csv(warm_months)
cold_months_df = pd.read_csv(cold_months)

# Printing the column names to ensure both dataframes have same column name
print("Warm Months Columns:", warm_months_df.columns.tolist())
print("Cold Months Columns:", cold_months_df.columns.tolist())

# Convert 'group_size' variable to numeric parameter to be compatible for the rest of the analysis
warm_months_df['group_size'] = pd.to_numeric(warm_months_df['group_size'])
cold_months_df['group_size'] = pd.to_numeric(cold_months_df['group_size'])

# Convert 'date_time' variable to datetime parameter to be compatible for the rest of the analysis
warm_months_df['date_time'] = pd.to_datetime(warm_months_df['date_time'])
cold_months_df['date_time'] = pd.to_datetime(cold_months_df['date_time'])

# Extract year and month from the 'date_time' column,
# Information found through https://stackoverflow.com/questions/23840797/convert-a-column-of-timestamps-into-periods-in-pandas
warm_months_df['year_month'] = warm_months_df['date_time'].dt.to_period('M').dt.to_timestamp()
cold_months_df['year_month'] = cold_months_df['date_time'].dt.to_period('M').dt.to_timestamp()

# Group by 'year_month' and summarize the 'group_size' to see total group size per month for each dataframe
warm_months_grouped = warm_months_df.groupby('year_month')['group_size'].sum().reset_index()
cold_months_grouped = cold_months_df.groupby('year_month')['group_size'].sum().reset_index()

# Add a 'season' column to differentiate between warm and cold seasons for plotting purposes
warm_months_grouped['season'] = 'Warm'
cold_months_grouped['season'] = 'Cold'

# Combine both datasets into one dataframe
Combined_Seasons = pd.concat([warm_months_grouped, cold_months_grouped])

# Sort the combined dataset by 'year_month' 
Combined_Seasons.sort_values('year_month', inplace=True)

# Creating a color palette with blue for the cold season and red for the warm season
season_palette = {'Warm': 'red', 'Cold': 'blue'}

# Plotting the combined time-series
plt.figure(figsize=(12, 6))

# Plot for both warm and cold months on the same axis with the specified color palette
sns.lineplot(data=Combined_Seasons, x='year_month', y='group_size', hue='season', palette=season_palette)


# Customize the plot
plt.title('Population Trends in Warm vs Cold Months')
plt.xlabel('Year-Month')
plt.ylabel('Total Group Size')
plt.xticks(rotation=45)
plt.legend(title='Season')
plt.show()

# Save plot to file
plot_path = 'V:/FinalProject/photos/Time_Series_Analysis.png'
plt.tight_layout()

# Save the plot
plt.savefig(plot_path)

