# Required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'BeeWalk_data.csv'  # Update with the actual file name if different
data = pd.read_csv(file_path, encoding='latin1', low_memory=False)

# Preprocess the data
# Convert StartDate to datetime
data['StartDate'] = pd.to_datetime(data['StartDate'], errors='coerce')

# Extract year, month, and assign seasons
data['Year'] = data['StartDate'].dt.year
data['Month'] = data['StartDate'].dt.month

def assign_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"

data['Season'] = data['Month'].apply(assign_season)

# Define extreme climate thresholds
EXTREME_HEAT_THRESHOLD = 30  # Temperature > 30°C for summer
EXTREME_COLD_THRESHOLD = 5   # Temperature < 5°C for spring

# Mark extreme events in the dataset
data['ExtremeHeat'] = (data['Season'] == 'Summer') & (data['temperature'] > EXTREME_HEAT_THRESHOLD)
data['ExtremeCold'] = (data['Season'] == 'Spring') & (data['temperature'] < EXTREME_COLD_THRESHOLD)

# Seasonal analysis
# Aggregate total bee counts by season and year
seasonal_trends = data.groupby(['Year', 'Season'])['TotalCount'].mean().reset_index()

# Add counts of extreme events for each season and year
extreme_counts = data.groupby(['Year', 'Season'])[['ExtremeHeat', 'ExtremeCold']].sum().reset_index()

# Merge the seasonal trends with extreme event counts
seasonal_analysis = pd.merge(seasonal_trends, extreme_counts, on=['Year', 'Season'], how='left')

# Visualise seasonal trends
plt.figure(figsize=(12, 6))
for season in seasonal_analysis['Season'].unique():
    season_data = seasonal_analysis[seasonal_analysis['Season'] == season]
    plt.plot(season_data['Year'], season_data['TotalCount'], label=season)

plt.scatter(
    seasonal_analysis['Year'][seasonal_analysis['ExtremeHeat'] > 0],
    seasonal_analysis['TotalCount'][seasonal_analysis['ExtremeHeat'] > 0],
    color='red', label='Extreme Heat (Summer)', zorder=5
)
plt.scatter(
    seasonal_analysis['Year'][seasonal_analysis['ExtremeCold'] > 0],
    seasonal_analysis['TotalCount'][seasonal_analysis['ExtremeCold'] > 0],
    color='blue', label='Extreme Cold (Spring)', zorder=5
)

plt.title("Seasonal Variations in Bee Counts with Extreme Climate Events")
plt.xlabel("Year")
plt.ylabel("Average Bee Counts")
plt.legend()
plt.grid(True)
plt.show()

# Analyse temperature effects
# Aggregate bee counts by temperature and season
temperature_analysis = data.groupby(['temperature', 'Season'])['TotalCount'].mean().reset_index()

# Scatter plot for temperature vs. bee counts
plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=temperature_analysis,
    x='temperature',
    y='TotalCount',
    hue='Season',
    alpha=0.7
)
plt.title("Aggregated Temperature vs. Bee Counts by Season")
plt.xlabel("Temperature (°C)")
plt.ylabel("Average Bee Counts")
plt.legend(title="Season")
plt.grid(True)
plt.show()

# Save results to CSV for report
seasonal_analysis.to_csv('Seasonal_Analysis.csv', index=False)
temperature_analysis.to_csv('Temperature_Analysis.csv', index=False)
