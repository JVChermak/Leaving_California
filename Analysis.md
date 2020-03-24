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

During our analysis in Jupyter Notebook using Pandas, we noticed a migration trend of Californians each year. The top five states Californians are moving to is Texas, Arizona, Washington, New York, and Nevada. We pulled the housing cost data from data.census.gov to find correlations for this trend. As we suspected, the housing cost was half of California's in the topfive migrated states.  

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

### Plots  
A linear regression was performed using the census data for 2010-2018 as well as the Zillow monthly data from April 1996 to January 2020. These regression equations were very different from each other, mainly due to the amount of information that was available in each dataset. A recommendation for future analysis could include comparing the home values in the upcoming months to see if either model was close to reality. Another venue for future analysis would be to perform similar linear regressions for the other 49 US states to see if any of those models are an accurate representation of the home values in the near future. Even more interesting would be to see how the inclusion of market fluctuations in the Zillow data will hold up when predicting home values in 2030 and beyond.
As for the RandomForest Classifier, it would be interesting to see if the model could accurately predict good and bad housing costs with data from the 2020 census.  

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

[Back to Top](#analysis)  
[Back to README.md](/README.md)
