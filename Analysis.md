# Analysis  
[Leaflet Map](#leaflet-map)  
[HTML Map](#html-map)  
[HTML Table](#html-table)  
[Plots](#plots)  
[Back to README.md](/README.md)  

For the description of the analysis phase of the project, with the vast amount of data we used for our analysis, we developed a "user friendly" dashboard to display all the information.  

### Leaflet Map
One way we can tell stories with data is through interactive maps, which is what we created in our dashboard.  

The purpose of the leaflet map is to visually show the number of people moving out of California by year and the differences in these numbers by States receiving Californian migrants.  

A map was well suited for our project as the project is location-based. For stakeholders or our audience, a map visualization of where Californians are migrating and in what numbers is critical for understanding the core of the project and also visually appealing.  

To complete this project, we use selected data from our CSV and retrieve a list of geographical coordinates or centers from census.gov website. Then add the data to a map.  

Usually, to map multiple points a URL is used because the data is usually inaccessible or too large. But for this project the data for which we wanted visualized was not nearly as large.  

Our approach was to use the JavaScript and the D3.js library to retrieve the coordinates. We use the Leaflet library to plot the data on a Mapbox map through an API request. Next, we create an index.html page adding to it Leaflet CSS and JavaScript files. Then we create a style.css file which is necessary for setting specific height and style for the map on our index.html. The next step is to tell our index.html page to use the syle.css file by adding the CSS link in the head of the index.html file.  

Two other essential pieces needed includes the config.js and logic.js files. The config.js file holds the Mapbox API key, while the logic.js file will contain all the JavaScript and Leaflet code to create the map and add data to the map.  

In the step following, it is essential to allow our index.html file to use the logic.js and config.js scripts. To do this, we add our scripts to the body of the index.html file. Next, we add a circleMarker() function to the map via Leaflet.  

The last step is to add multiple markers or points to the map. To add a marker for each location or state receiving greater than 10,000 CA migrants in 2018, we iterate through the array of longitudes and latitudes and add each to the map. For best practice, we save the states array in an external file and refer to that file and dataset in the logic.js file. Finally, to add data from each object in the cities array we use Leaflet’s bindPopup() method on the marker() function.  

<img align="left" width="900" src="/pics/MigFlow_map.png"><br/>
<br/>
<br/>
<br/>
<br/>
<br/>  
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>  

### HTML Map  
Image maps are a valuable way to display complex sets of data. For instance, out html map consist of over 2,250 statistics broken down from 50 states over the course of 9 years. If presented as text, this amount of data can become redundant. Image maps are useful displaying large datasets, such as ours. Allowing the user to understand social, economic, and demographic conditions visually.  

During our analysis in Jupyter Notebook using Pandas, we noticed a migration trend of Californians each year. The top five states Californians are moving to is Texas, Arizona, Washington, New York, and Nevada. We pulled the housing cost data from data.census.gov to find correlations for this trend. As we suspected, the housing cost was half of California's in those states.  

We maintained the entire dataset for our HTML map to support further analysis.  

<img align="left" width="900" src="/pics/Housing_map.png"><br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>  

### HTML Table  
Our table allows the user to take a look at census data for each state by year to see housing costs, income, and migration changes. It filters by year and/or state.  

<img align="left" width="900" src="/pics/Machine_Learning.png"><br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/> 

### Plots  
<img align="right" width="200" src="/pics/median_housing1.png"><br/>The census.gov data for 2010-2018 shows the median cost of housing decrease during the recession, lasting through 2013. The cost of housing is then shown to increase steadily. This data is clearly not linear, and looking at the prediction from this linear regression shows that it might not be very accurate. The median monthly cost of housing is already very close to $2400, which would suggest that another large dip would need to happen first.  

<img align="right" width="200" src="/pics/median_housing2.png"><br/>A second attempt at a linear regression was performed with the median cost of housing from 2013 through 2018, in the hopes that it would be more accurate including the data that is more linear. The predicted montly housing cost seems more fitting with the current trend, but is also alarmingly large and hopefully not sustainable.  

<img align="right" width="200" src="/pics/median_home_value1.png"><br/>The Zillow data shows the increase of typical home value through 2008, the decrease during the recession lasting until just before 2012, and then home value has continued to increase since 2012. A linear regression was tried here as well, in the hopes that the peaks and valleys would create a more reasonable predictor of future home values. The typical home value predicted for 2030 seems more likely than any of the other models.  

<img align="right" width="200" src="/pics/median_home_value2.png"><br/>A regression line was done on the census.gov data to compare the median home value predictions with the Zillow data predictions. While the prediction for 2030 goes along with the current trend, the possibility that the median home value will be this large is the main contributing factor for possibly leaving the state.  
<br/>
<br/>
**Looking beyond California US Migration Analysis, the census.gov website has migration flow data for each year starting in 2010. The information includes population, how many lived in the same or a different state the previous year, and the number moving between states.**  

<img align="right" width="250" src="/pics/state_migration_kmeans_scatter.png"><br/>After removing the state to state information, a K-means machine learning model was run to see if there was any interesting grouping going on with the migration flows. The scatterplot shows that there are 5 distinct classes for the 50 states between 2010 and 2018, based on population and the number of people who lived in a different state the previous year.  

<img align="right" width="250" src="/pics/overall_migration_pca_scatter.png"><br/>Further analysis was done with the state to state information, as well as all information using the PCA method to reduce features. While all showed groupings of some sort, it is not known to us what these groupings suggest. Given more time, it would be interesting to find out if there are any significant features that contribute to the groupings.  

[Back to Top](#analysis)  
[Back to README.md](/README.md)
