# BeeWalk-Analysis
Data Science and Machine Learning for the Biosciences - SWBio Project

This repository contains code and documentation for analysing seasonal variations in bee counts and their relationship to extreme climate events, such as extreme heat in summer or extreme cold in spring. The dataset used is the BeeWalk dataset (2008-2023) from The Bumblebee Conservation Trust.

## Objectives
The purpose of this project is to: 

1.	Investigate seasonal variations in bee counts across years.
2.	Examine the effects of extreme temperature events (heat and cold) on bee counts.

## Files
1. BeeWalk.py: Python script for preprocessing, analysing, and visualising the data.
2. BeeWalk_data: Zipped folder containing BeeWalk_data.csv file.
3. Seasonal_Analysis.csv: Processed data summarising seasonal trends in bee counts and extreme events.
4. Temperature_Analysis.csv: Aggregated data showing the relationship between temperature and bee counts.

## Instructions to Run the Code
Ensure you have the following installed:
1. Python 3.7 or higher
2. Required Python libraries: panda, matplotlib & seaborn

You can install the required libraries using: pip install pandas matplotlib seaborn

## Running the Code
1.	Unzip the BeeWalk_data file
2.	Place the BeeWalk dataset file (BeeWalk_data.csv) in the same directory as the script.
3.	Run the Python script: BeeWalk.py
4.	Output files (Seasonal_Analysis.csv and Temperature_Analysis.csv) will be generated in the same directory.

## Outputs
Seasonal_Analysis.csv
1. Contains average bee counts by season and year.
2. Includes counts of extreme heat and cold events.

Temperature_Analysis.csv:
1. Shows average bee counts for different temperature ranges, grouped by season.

## Analysis Summary
Seasonal Trends: The analysis visualises how bee counts vary across seasons and years.

Temperature Effects: Scatter plots reveal the relationship between temperature and bee counts, highlighting trends and correlations.

Extreme Events:
1. Extreme heat (e.g., temperatures > 30°C in summer).
2. Extreme cold (e.g., temperatures < 5°C in spring)
3. Events are highlighted in visualisations to illustrate their impact.

## Visualisations
1. Seasonal Variations: Line plots showing average bee counts by season.
2. Temperature Effects: Scatter plots depicting bee counts versus temperature across seasons.

