# 2022 TTC Transit Data Analysis: Delays
## Executive Summary
the purpose of this data analysis project is to uncover the biggest factors contributing to the delays in TTCs operation, intended for key company stakeholders to help optimize their operations.
This analysis breakdowns the delays by time, routes, and incident type to better understand where the TTC can focus their efforts to minimize delays. 
Among the key findings, this report uncovers that Diversions, Operations and Mechanical delays make up the vast majority of the delays in the TTC.
Based on our findings, we recommend the TTC to better prepare for delays in the winter season, anticipating possible diversion routes and having services available at quick notice to minimize the 
diversion and mechanical delays.

## Data Overview
The dataset was provided by the TTC: https://open.toronto.ca/dataset/ttc-bus-delay-data/
This data contains every reported bus delay on the TTC in 2022, from January to June. Containing information in the incidient type, the route the incident occured, the time and date, as well as the delay duration in minutes.
The initial dataset had 27,352 rows of data. We removed the "Direction" column as it contains many null values. We also remove the "Vehicle" column as we don't use this information for our analysis.
We cleaned our data by removing the rows with null values in the "Route" column, as well as the any rows with a "Min Delay" of 0. 

![image](https://github.com/user-attachments/assets/d9e3cdea-02b3-4d7b-b77e-0d370c280399)


## Initial Insights
We utilized Microsoft Excel for the initial data cleaning, we then used Microsoft PowerBI to run measurement columns, further clean the data and to create visualizations.
![locationswiththemostdelay](https://github.com/user-attachments/assets/ceee379d-d641-4e2c-a00f-085019dca406)
Locations with The Most Delay
![Major Delay Locations Mapped](https://github.com/user-attachments/assets/87a1c95e-8618-4790-8754-2cf32e0238c3)

![Toronto_rapid_transit_map_2023 svg](https://github.com/user-attachments/assets/0d78f739-a8cf-400a-8838-46b4e9b92992)

Many of the bus stations along "Line 1 Younge - University" subway line experience over 5,000 minutes of delays, specifically the West side of the route. This line runs through the heart of the city, serving major downtown areas like the financial district, shopping districts, 
and numerous universities, leading to a high volume of commuters using it every day.


![MonthsWithTheMostDelay](https://github.com/user-attachments/assets/e1f75301-7d62-4c36-b6d4-feb6b1a279d3)
January has the most delays, approx 5000 minutes more of delays compared to any of the other months in the dataset.

![AvgDelayThroughWeek](https://github.com/user-attachments/assets/18f5bf37-c16b-4524-b26b-a9d6939486cc)
The average delay throughout the week comes out to around 4000-5000, the peak being on Wednesday with the lowest delays on average being on Fridays.

![sumofdelaybyincident](https://github.com/user-attachments/assets/981b1570-cb0c-4c9b-a94e-0c41dbb02c07)
Diversions contribute to the most time in delays, followed by Operation Delays. The TTC has little to no delays as a result of Entering Service Late.

![Average Month Breakdown](https://github.com/user-attachments/assets/b6ae7fd7-5b9b-41b9-85c9-22f0c8ebf35d)
At a glance, we can see that the incident types on average have a relatively steady value throughout the year, except for "Diversion" delays which varys greatly. Its largest average value is 11,082 minutes with the lowest being 4,000.

## Dashboard
![Dashboard](https://github.com/user-attachments/assets/404cda62-94d5-45bf-83d3-a2c210c5f0ff)







