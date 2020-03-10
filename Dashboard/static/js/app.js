function buildMap(data){
    // some code here for the map
}

function handleClick() {
    // Grab the year value from the filter
    let year = d3.select("#datetime").property("value");
    let filteredData = mapData;  // Need to figure out how to set up mapData

    // Check to see if a year was entered and filter the data
    // using that year
    if (year) {
        // Apply `filter` to the table data to only keep the
        // rows where the year value matches the filter value
        filteredData = filteredData.filter(row => row.datetime === year);
    }

    // Rebuild the map using the filtered data
    // @NOTE: If no year was entered, then filteredData will
    // just be the map of US migration.
    
    buildMap(filteredData);
}

// Attach an event to listen for the form button
d3.selectAll("#filter-btn").on("click", handleClick);
// Build the map when the page loads
buildMap(mapData);