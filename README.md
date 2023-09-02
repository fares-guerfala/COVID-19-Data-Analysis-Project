# COVID-19-Data-Analysis-Project

## Goal
The goal of this project is to perform an analysis of COVID-19 data for the United States in 2020. We aim to provide insights into the spread of the virus, testing, positive cases, and deaths by state. The project includes interactive visualizations to help users explore the data more effectively.

## Table of Contents
1. Getting Started
2. Usage
3. Data
4. Features
5. Visualization
6. Interpretation of Results
7. Contributing
8. License


### Getting Started
#### Prerequisites
Python 3.x <br>
Dash <br>
Plotly <br>
Pandas <br>
Flask <br>

#### Installation
1. Clone this repository to your local machine:
```
  git clone https://github.com/fares-guerfala/covid19-data-analysis.git
```
2. Navigate to the project directory:
```
cd covid19-data-analysis
``` 
3. Run the application:
```
python app.py
```

The application should be accessible at http://127.0.0.1:8050 in your web browser.

### Usage
- Select one or more states from the dropdown to view data for specific states.
- Use the date range picker to select a custom date range.
- Explore the "Positive and Total Cases by State" chart to visualize testing and positive cases.
- Examine the "Map of Total Cases by State" to see a geographical representation.
- Analyze the "COVID-19 Deaths by State Over Time" chart to understand the death trends.

### Data
The project utilizes COVID-19 data for 2020. The data source is in the project folder, which provides daily information on deaths, hospitalizations, negative tests, positive tests, and total test results by state.

### Features
- Interactive dropdown for state selection.
- Date range picker for customized data exploration.
- Bar chart visualization of total tests and positive tests by state.
- Geographical map showing total cases by state.
- Slider for selecting specific dates.
- Line chart displaying COVID-19 deaths by state over time.

### Visualization
1. The "Positive and Total Cases by State" chart visualizes the total tests and positive tests by state. It helps users compare testing and positive cases across different states.

2. The "Map of Total Cases by State" provides a geographical view of total cases by state. The color scale represents the number of total tests, with darker shades indicating higher numbers.

3. The "COVID-19 Deaths by State Over Time" chart displays the trend of COVID-19 deaths for selected states over time. It helps users understand how the number of deaths has evolved.

### Interpretation of Results
- The analysis of testing and positive cases by state helps identify regions with higher testing rates and positivity rates. This information can be valuable for resource allocation and policy decisions.

- The geographical map allows users to visually assess which states have higher total cases. It can provide insights into the geographic spread of the virus.

- The trend of COVID-19 deaths over time is crucial for understanding the impact of the pandemic. Users can identify periods of high mortality and monitor the effectiveness of interventions.

### Contributing
Contributions are welcome! Feel free to open issues, submit pull requests, or suggest improvements.

### License
This project is licensed under the MIT License.





