## Analysis  
### Description of the analysis phase of the project  
One way we can tell stories with data is through interactive maps, which is what we created in our dashboard.  

The purpose of this map is to visually show the number of people moving out of California by year and the differences in these numbers by States receiving Californian migrants.  

A map was well suited for our project as the project is location-based. For stakeholders or our audience, a map visualization of where Californians are migrating and in what numbers is critical for understanding the core of the project and also visually appealing.  

To complete this project, we use selected data from our CSV and retrieve a list of geographical coordinates or centers from census.gov website. Then add the data to a map.  

Usually, to map multiple points a URL is used because the data is usually inaccessible or too large. But for this project the data for which we wanted visualized was not nearly as large.  

Our approach was to use the JavaScript and the D3.js library to retrieve the coordinates. We use the Leaflet library to plot the data on a Mapbox map through an API request. Next, we create an index.html page adding to it Leaflet CSS and JavaScript files. Then we create a style.css file which is necessary for setting specific height and style for the map on our index.html. The next step is to tell our index.html page to use the syle.css file by adding the CSS link in the head of the index.html file.  

Two other essential pieces needed includes the config.js and logic.js files. The config.js file holds the Mapbox API key, while the logic.js file will contain all the JavaScript and Leaflet code to create the map and add data to the map.  

In the step following, it is essential to allow our index.html file to use the logic.js and config.js scripts. To do this, we add our scripts to the body of the index.html file. Next, we add a circleMarker() function to the map via Leaflet.  

The last step is to add multiple markers or points to the map. To add a marker for each location or state receiving greater than 10,000 CA migrants in 2018, we iterate through the array of longitudes and latitudes and add each to the map. For best practice, we save the states array in an external file and refer to that file and dataset in the logic.js file. Finally, to add data from each object in the cities array we use Leaflet’s bindPopup() method on the marker() function.
<img align="right" width="700" src="/Data/leaf_map_here.png"><br/>