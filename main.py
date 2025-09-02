import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
# Define G20 countries
g20_countries = ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 
                 'India', 'Indonesia', 'Italy', 'Japan', 'Mexico', 'Russia', 'Saudi Arabia', 
                 'South Africa', 'South Korea', 'Turkey', 'UK', 'USA', 'EU']
# Generate synthetic economic data
np.random.seed(42) # for reproducibility
num_countries = len(g20_countries)
num_quarters = 8 # Data for 2 years (8 quarters)
data = {
    'Country': np.repeat(g20_countries, num_quarters),
    'Quarter': np.tile(pd.to_datetime(['2020-01-01', '2020-04-01', '2020-07-01', '2020-10-01',
                                        '2021-01-01', '2021-04-01', '2021-07-01', '2021-10-01']), num_countries),
    'GDP_Growth': np.random.normal(loc=2, scale=1, size=num_countries * num_quarters), # Simulate GDP growth with noise
    'Unemployment_Rate': np.random.uniform(low=3, high=10, size=num_countries * num_quarters), # Simulate unemployment
    'Inflation_Rate': np.random.uniform(low=1, high=5, size=num_countries * num_quarters) # Simulate inflation
}
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Preprocessing (Minimal in this synthetic example) ---
# Ensure data types are correct
df['Quarter'] = pd.to_datetime(df['Quarter'])
df['GDP_Growth'] = df['GDP_Growth'].round(2)
df['Unemployment_Rate'] = df['Unemployment_Rate'].round(2)
df['Inflation_Rate'] = df['Inflation_Rate'].round(2)
# --- 3. Analysis (Simple aggregation for demonstration) ---
# Calculate average GDP growth per country
average_gdp_growth = df.groupby('Country')['GDP_Growth'].mean()
# --- 4. Visualization ---
plt.figure(figsize=(12, 6))
sns.barplot(x=average_gdp_growth.index, y=average_gdp_growth.values)
plt.xticks(rotation=90)
plt.title('Average GDP Growth (2020-2021) by G20 Country')
plt.xlabel('Country')
plt.ylabel('Average GDP Growth (%)')
plt.tight_layout()
# Save the plot
output_filename = 'gdp_growth_barplot.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Quarter', y='GDP_Growth', hue='Country')
plt.xticks(rotation=45)
plt.title('GDP Growth Over Time by G20 Country')
plt.xlabel('Quarter')
plt.ylabel('GDP Growth (%)')
plt.tight_layout()
#Save the plot
output_filename2 = 'gdp_growth_lineplot.png'
plt.savefig(output_filename2)
print(f"Plot saved to {output_filename2}")