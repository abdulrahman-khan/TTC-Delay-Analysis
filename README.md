# **2022 TTC Transit Data Analysis: Delays**  
<img width="50" height="50" src="https://github.com/user-attachments/assets/d46bf84f-b776-4af2-b018-050d57322656">
<img width="50" height="50" src="https://github.com/user-attachments/assets/4c63e159-3661-4d42-ace9-e21811966ede">

## **Executive Summary**  
The purpose of this data analysis project is to identify the primary factors contributing to delays in TTC operations. This report is intended for key stakeholders to help optimize transit efficiency.  

Our analysis breaks down delays by **time, routes, and incident type** to determine where the TTC can focus efforts to minimize disruptions. Key findings reveal that **Diversions, Operational Issues, and Mechanical Failures** are the leading causes of delays.  

Based on our findings, we recommend that the TTC **proactively prepare for winter-related disruptions** by:  
- Anticipating and planning alternative routes for diversions.  
- Ensuring quick-response maintenance services are available to reduce mechanical delays.  

---

## **Data Overview**  
The dataset was sourced from the **TTC Open Data Portal**: [TTC Bus Delay Data](https://open.toronto.ca/dataset/ttc-bus-delay-data/).  

### **Dataset Details:**  
- Covers all reported bus delays **from January to June 2022**.  
- Includes key attributes such as **incident type, route, timestamp, and delay duration (in minutes).**  
- Contains **27,352 rows** initially.  

### **Data Cleaning:**  
- Removed **"Direction"** due to excessive null values.  
- Dropped **"Vehicle"** since it was not relevant to our analysis.  
- Removed records where **"Route" was null** and any delays of **0 minutes** (as they don’t contribute to meaningful insights).  

![image](https://github.com/user-attachments/assets/d9e3cdea-02b3-4d7b-b77e-0d370c280399)  

---

## **Initial Insights**  
We used **Microsoft Excel** for preliminary data cleaning and **Microsoft Power BI** for deeper analysis and visualization.  

### **Delays by Location**  
Many bus stations along the **west side of the Line 1 Yonge-University subway line** experienced over **5,000 minutes of delays**.  
- This route serves high-traffic areas such as the **Financial District, shopping hubs, and universities**, leading to **high commuter volume and frequent delays**.  

![locationswiththemostdelay](https://github.com/user-attachments/assets/ceee379d-d641-4e2c-a00f-085019dca406)  

![Major Delay Locations Mapped](https://github.com/user-attachments/assets/87a1c95e-8618-4790-8754-2cf32e0238c3)  

![Toronto_rapid_transit_map_2023 svg](https://github.com/user-attachments/assets/0d78f739-a8cf-400a-8838-46b4e9b92992)  

---

### **Delays by Month**  
- **January experienced the highest delays**, with approximately **5,000 more minutes of delays** than any other month.  

![MonthsWithTheMostDelay](https://github.com/user-attachments/assets/e1f75301-7d62-4c36-b6d4-feb6b1a279d3)  

---

### **Delays by Day of the Week**  
- The average delay time **throughout the week** ranges between **4,000–5,000 minutes**.  
- **Wednesdays have the highest delays**, while **Fridays experience the least**.  

![AvgDelayThroughWeek](https://github.com/user-attachments/assets/18f5bf37-c16b-4524-b26b-a9d6939486cc)  

---

### **Delays by Incident Type**  
- **Diversions** account for the **most total delay time**, followed by **Operational Issues**.  
- **Late Entry into Service has a negligible impact on total delay time.**  

![sumofdelaybyincident](https://github.com/user-attachments/assets/981b1570-cb0c-4c9b-a94e-0c41dbb02c07)  

---

### **Seasonal Trends**  
- Delay times for most **incident types remain steady throughout the year**, except **Diversion delays**, which fluctuate significantly.  
- **January had the largest diversion-related delays (~11,082 minutes), while the lowest was around 4,000 minutes.**  

![Average Month Breakdown](https://github.com/user-attachments/assets/b6ae7fd7-5b9b-41b9-85c9-22f0c8ebf35d)  

---

### **Impact of Winter Weather**  
- Analyzing **January’s data** revealed clear **delay spikes between January 18–28** due to the **January 14–17, 2022 snowstorm** ([Wikipedia Link](https://en.wikipedia.org/wiki/January_14%E2%80%9317,_2022_North_American_winter_storm)).  
- **Operational incidents spiked early in the month** and increased again **mid-to-late January**.  

![image](https://github.com/user-attachments/assets/377c9b9d-3400-4203-90f3-a2ed229bef65)  

---

## **Dashboard Overview**  
To facilitate easy data exploration, our team developed an **interactive Power BI dashboard** that provides:  
- **Key Performance Indicators (KPIs):** Displaying the **total number of incidents** and **total delay time per month**.  
- **Bar Charts:** Showing **delays by location and day of the week**.  
- **Scatter Plot Visualization:** Offering an **in-depth breakdown of delays within each selected month**.
![image](https://github.com/user-attachments/assets/82ae8565-d5ef-444e-8b5f-e00e7b814191)  

---

## **Recommendations**
- Winter Preparedness: The TTC should better prepare for delays in the winter season by anticipating possible diversion routes and ensuring quick-response maintenance services to minimize diversion and mechanical delays.
- Quick-Response Maintenance Services: Ensuring that maintenance teams are readily available to handle mechanical failures efficiently can help reduce delays.


---
## **Final Thoughts**  
This analysis highlights the **significant impact of diversions and winter-related disruptions** on TTC delays. By implementing **proactive winter response strategies** and optimizing operational workflows, the TTC can **reduce delays and improve service reliability**.  
