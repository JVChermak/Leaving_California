// Add console.log to check to see if our code is working.
console.log("working");

// We create the tile layer that will be the background of our map.
let satelliteStreets =  L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

// We create the tile layer that will be the background of our map.
let streets =  L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

//Create a base layer that holds both maps
let baseMaps = {
    "Streets" : streets,
    "Satellite": satelliteStreets
};

// Load the data into layers by year
//2010
data_2010 = cities.filter(state => state.year == 2010)
console.log(data_2010)
markers_2010 = []

data_2010.forEach(marker => {
  let migflow = parseInt(marker.migflow.replace(/,/g, ''))
  console.log(migflow*0.01)
  markers_2010.push(L.circleMarker(marker.location, {
    color: '#e41a1c',
    radius: Number(migflow) * 0.001
  }).bindPopup("<h4>" + marker.state + ", " + marker.year + " <hr>Population " + marker.population.toLocaleString() + "</h4> <hr> <h5>MigFlow " + marker.migflow + "</h5>"));
})
console.log(markers_2010)
layer_group_2010 = L.layerGroup(markers_2010)

//2011
data_2011 = cities.filter(state => state.year == 2011)
console.log(data_2011)
markers_2011 = []

data_2011.forEach(marker => {
  let migflow = parseInt(marker.migflow.replace(/,/g, ''))
  console.log(migflow*0.01)
  markers_2011.push(L.circleMarker(marker.location, {
    color: '#377eb8',
    radius: Number(migflow) * 0.001
  }).bindPopup("<h4>" + marker.state + ", " + marker.year + " <hr>Population " + marker.population.toLocaleString() + "</h4> <hr> <h5>MigFlow " + marker.migflow + "</h5>"));
})
console.log(markers_2011)
layer_group_2011 = L.layerGroup(markers_2011)

//2012
data_2012 = cities.filter(state => state.year == 2012)
console.log(data_2012)
markers_2012 = []

data_2012.forEach(marker => {
  let migflow = parseInt(marker.migflow.replace(/,/g, ''))
  console.log(migflow*0.01)
  markers_2012.push(L.circleMarker(marker.location, {
    color: '#4daf4a',
    radius: Number(migflow) * 0.001
  }).bindPopup("<h4>" + marker.state + ", " + marker.year + " <hr>Population " + marker.population.toLocaleString() + "</h4> <hr> <h5>MigFlow " + marker.migflow + "</h5>"));
})
console.log(markers_2012)
layer_group_2012 = L.layerGroup(markers_2012)

// 2013
data_2013 = cities.filter(state => state.year == 2013)
console.log(data_2013)
markers_2013 = []

data_2013.forEach(marker => {
  let migflow = parseInt(marker.migflow.replace(/,/g, ''))
  console.log(migflow*0.01)
  markers_2013.push(L.circleMarker(marker.location, {
    color: '#984ea3',
    radius: Number(migflow) * 0.001
  }).bindPopup("<h4>" + marker.state + ", " + marker.year + " <hr>Population " + marker.population.toLocaleString() + "</h4> <hr> <h5>MigFlow " + marker.migflow + "</h5>"));
})
console.log(markers_2013)
layer_group_2013 = L.layerGroup(markers_2013)

//2014
data_2014 = cities.filter(state => state.year == 2014)
console.log(data_2014)
markers_2014 = []

data_2014.forEach(marker => {
  let migflow = parseInt(marker.migflow.replace(/,/g, ''))
  console.log(migflow*0.01)
  markers_2014.push(L.circleMarker(marker.location, {
    color: '#ff7f00',
    radius: Number(migflow) * 0.001
  }).bindPopup("<h4>" + marker.state + ", " + marker.year + " <hr>Population " + marker.population.toLocaleString() + "</h4> <hr> <h5>MigFlow " + marker.migflow + "</h5>"));
})
console.log(markers_2014)
layer_group_2014 = L.layerGroup(markers_2014)

//2015
data_2015 = cities.filter(state => state.year == 2015)
console.log(data_2015)
markers_2015 = []

data_2015.forEach(marker => {
  let migflow = parseInt(marker.migflow.replace(/,/g, ''))
  console.log(migflow*0.01)
  markers_2015.push(L.circleMarker(marker.location, {
    color: '#ffff33',
    radius: Number(migflow) * 0.001
  }).bindPopup("<h4>" + marker.state + ", " + marker.year + " <hr>Population " + marker.population.toLocaleString() + "</h4> <hr> <h5>MigFlow " + marker.migflow + "</h5>"));
})
console.log(markers_2015)
layer_group_2015 = L.layerGroup(markers_2015)

//2016
data_2016 = cities.filter(state => state.year == 2016)
console.log(data_2016)
markers_2016 = []

data_2016.forEach(marker => {
  let migflow = parseInt(marker.migflow.replace(/,/g, ''))
  console.log(migflow*0.01)
  markers_2016.push(L.circleMarker(marker.location, {
    color: '#a65628',
    radius: Number(migflow) * 0.001
  }).bindPopup("<h4>" + marker.state + ", " + marker.year + " <hr>Population " + marker.population.toLocaleString() + "</h4> <hr> <h5>MigFlow " + marker.migflow + "</h5>"));
})
console.log(markers_2016)
layer_group_2016 = L.layerGroup(markers_2016)

//2017
data_2017 = cities.filter(state => state.year == 2017)
console.log(data_2017)
markers_2017 = []

data_2017.forEach(marker => {
  let migflow = parseInt(marker.migflow.replace(/,/g, ''))
  console.log(migflow*0.01)
  markers_2017.push(L.circleMarker(marker.location, {
    color: '#f781bf',
    radius: Number(migflow) * 0.001
  }).bindPopup("<h4>" + marker.state + ", " + marker.year + " <hr>Population " + marker.population.toLocaleString() + "</h4> <hr> <h5>MigFlow " + marker.migflow + "</h5>"));
})
console.log(markers_2017)
layer_group_2017 = L.layerGroup(markers_2017)

//2018
data_2018 = cities.filter(state => state.year == 2018)
console.log(data_2018)
markers_2018 = []

data_2018.forEach(marker => {
  let migflow = parseInt(marker.migflow.replace(/,/g, ''))
  console.log(migflow*0.01)
  markers_2018.push(L.circleMarker(marker.location, {
    color: '#999999',
    radius: Number(migflow) * 0.001
  }).bindPopup("<h4>" + marker.state + ", " + marker.year + " <hr>Population " + marker.population.toLocaleString() + "</h4> <hr> <h5>MigFlow " + marker.migflow + "</h5>"));
})
console.log(markers_2018)
layer_group_2018 = L.layerGroup(markers_2018)

// Create the layers for all years data, 2010-2018.
let year_2010 = new L.LayerGroup();
let year_2011 = new L.LayerGroup();
let year_2012 = new L.LayerGroup();
let year_2013 = new L.LayerGroup();
let year_2014 = new L.LayerGroup();
let year_2015 = new L.LayerGroup();
let year_2016 = new L.LayerGroup();
let year_2017 = new L.LayerGroup();
let year_2018 = new L.LayerGroup();

// We define an object contains all of our overlays.
// This overlay will be visible all the time.
let overlays= {
  "Year_2010": layer_group_2010,
  "Year_2011": layer_group_2011,
  "Year_2012": layer_group_2012,
  "Year_2013": layer_group_2013,
  "Year_2014": layer_group_2014,
  "Year_2015": layer_group_2015,
  "Year_2016": layer_group_2016,
  "Year_2017": layer_group_2017,
  "Year_2018": layer_group_2018,
};

// Create the map object with center, zoom level and default layer.
let map = L.map('mapid', {
  center: [39.5, -98.5],
  zoom: 4,
  layers: [satelliteStreets]
})

// Add a control to the map that will allow the user to change
// which layers are visible. add the variable overlays to the Layers Control object.
L.control.layers(baseMaps, overlays).addTo(map);

// Then we add our 'graymap' tile layer to the map.
streets.addTo(map)