// Add console.log to check to see if our code is working.
console.log("working");

// Map a GeoJSON Point. Add GeoJSON data.
let sanFranAirport =
{"type":"FeatureCollection","features":[{
    "type":"Feature",
    "properties":{
        "id":"3469",
        "name":"San Francisco International Airport",
        "city":"San Francisco",
        "country":"United States",
        "faa":"SFO",
        "icao":"KSFO",
        "alt":"13",
        "tz-offset":"-8",
        "dst":"A",
        "tz":"America/Los_Angeles"},
        "geometry":{
            "type":"Point",
            "coordinates":[-122.375,37.61899948120117]}}
]};


// Get data from cities.js
let cityData = cities;

  // Loop through the cities array and create one marker for each city.
cityData.forEach(function(city) {
	console.log(city)
L.circleMarker(city.location, {
	//radius:1000
	//radius:city.population/2000000
	radius:city.migflow*0.001
})
.bindPopup("<h2>" + city.city + ", " + city.state + "</h2> <hr> <h3>Population " + city.population.toLocaleString() + "</h3> <hr> <h4>MigFlow " + city.migflow + "</h4>")
  //.addTo(map);
});

// We create the tile layer that will be the background of our map.
let satelliteStreets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

// We create the tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

//Create a base layer that holds both maps
let baseMaps = {
    "Streets" : streets,
    "Satellite": satelliteStreets
};


// Create the earthquake layer for our map.
let Year_2010 = new L.LayerGroup();
let Year_2011 = new L.LayerGroup();
let Year_2012 = new L.LayerGroup();
let Year_2013 = new L.LayerGroup();
let Year_2014 = new L.LayerGroup();
let Year_2015 = new L.LayerGroup();
let Year_2016 = new L.LayerGroup();
let Year_2017 = new L.LayerGroup();
let Year_2018 = new L.LayerGroup();


// We define an object that contains the overlays.
// This overlay will be visible all the time.
let overlays = {
    Year_2010: Year_2010,
    Year_2011: Year_2011,
    Year_2012: Year_2012,
    Year_2013: Year_2013,
    Year_2014: Year_2014,
    Year_2015: Year_2015,
    Year_2016: Year_2016,
    Year_2017: Year_2017,
    Year_2018: Year_2018,
  };

// Create the map object with center, zoom level and default layer.
  let map = L.map('mapid', {
    center: [39.5, -98.5],
    zoom: 3,
    layers: [streets]
})


// Add a control to the map that will allow the user to change
// which layers are visible. add the variable overlays to the Layers Control object.
L.control.layers(baseMaps, overlays).addTo(map);

// // Get data from cities.js
// let cityData = cities;

//   // Loop through the cities array and create one marker for each city.
// cityData.forEach(function(city) {
// 	console.log(city)
// L.circleMarker(city.location, {
// 	//radius:1000
// 	//radius:city.population/2000000
// 	radius:city.migflow*0.001
// })
// .bindPopup("<h2>" + city.city + ", " + city.state + "</h2> <hr> <h3>Population " + city.population.toLocaleString() + "</h3> <hr> <h4>MigFlow " + city.migflow + "</h4>")
//   .addTo(map);
// });


// Creating a GeoJSON layer with the retrieved data.
L.geoJson(data, {

    // We turn each feature into a circleMarker on the map.
    
    pointToLayer: function(city, latlng) {
                  console.log(data);
                  return L.circleMarker(latlng);
            },
          // We set the style for each circleMarker using our styleInfo function.
            style: styleInfo,
    onEachFeature: function(feature, layer) {
            layer.bindPopup("<h2>" + city.city + ", " + city.state + "</h2> <hr> <h3>Population " + city.population.toLocaleString() + "</h3> <hr> <h4>MigFlow " + city.migflow + "</h4>");
        }
        }).addTo(cities);
    
  //  });

// Add a circle to map using a circleMarker function()
// L.circleMarker([34.0522, -118.2437], {
// 	radius:100,
// 	color:"black",
// 	fillColor: '#ffffa1',

// }).addTo(map);S


// Then we add our 'graymap' tile layer to the map.
streets.addTo(map);