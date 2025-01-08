BeeWalk Dataset Analysis

This repository contains code and documentation for analysing seasonal variations in bee counts and their relationship to extreme climate events, such as extreme heat in summer or extreme cold in spring. The dataset used is the BeeWalk dataset (2008-2023) from The Bumblebee Conservation Trust.

Objective
The purpose of this project is to:
1.	Investigate seasonal variations in bee counts across years.
2.	Examine the effects of extreme temperature events (heat and cold) on bee counts.

Files
•	BeeWalk.py: Python script for preprocessing, analysing, and visualising the data.
•	Seasonal_Analysis.csv: Processed data summarising seasonal trends in bee counts and extreme events.
•	Temperature_Analysis.csv: Aggregated data showing the relationship between temperature and bee counts.

Instructions to Run the Code
Prerequisites
Ensure you have the following installed:
•	Python 3.7 or higher
•	Required Python libraries:
	o	panda
	o	matplotlib
	o	seaborn

You can install the required libraries using: pip install pandas matplotlib seaborn

Running the Code
1.	Place the BeeWalk dataset file (BeeWalk_data.csv) in the same directory as the script.
2.	Run the Python script: BeeWalk.py
3.	Output files (Seasonal_Analysis.csv and Temperature_Analysis.csv) will be generated in the same directory.

Outputs
•	Seasonal_Analysis.csv:
	o	Contains average bee counts by season and year.
	o	Includes counts of extreme heat and cold events.
•	Temperature_Analysis.csv:
	o	Shows average bee counts for different temperature ranges, grouped by season.

Analysis Summary
•	Seasonal Trends: The analysis visualises how bee counts vary across seasons and years.
•	Temperature Effects: Scatter plots reveal the relationship between temperature and bee counts, highlighting trends and correlations.
•	Extreme Events:
	o	Extreme heat (e.g., temperatures > 30°C in summer).
	o	Extreme cold (e.g., temperatures < 5°C in spring).
	o	Events are highlighted in visualisations to illustrate their impact.

Visualisations
•	Seasonal Variations: Line plots showing average bee counts by season.
•	Temperature Effects: Scatter plots depicting bee counts versus temperature across seasons.
