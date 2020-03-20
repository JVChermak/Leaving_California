// import the data from data.js
const tableData = data;
// Reference the HTML table using d3
var tbody = d3.select("#migration-table");

// Create a function to build the dynamic table
function buildTable(data) {
  // First, clear out any existing data
  tbody.html("");
  // Next, loop through each object in the data and append a row and cells for each value in the row
  data.forEach((dataRow) => {
    // Append a row to the table body
    let row = tbody.append("tr");
    // Loop through each field in teh dataRow and add each value as a table cell
    Object.values(dataRow).forEach((val) => {
      let cell = row.append("td");
      cell.text(val);
      }
    );
  });
}


// Keep track of all filters
var filters = {};

// This function will replace your handleClick function
function updateFilters() {

  // Save the element, value, and id of the filter that was changed
  let year = d3.select("#year").property("value");
  let state = d3.select("#state").property("value");
  
  // If a filter value was entered then add that filterId and value
  // to the filters list. Otherwise, clear that filter from the filters object
  if (year) {
    filters["Year"] = year;
  }  else {
      delete filters["Year"];
  }
  if (state) {
    filters["State"] = state;
  }  else {
       delete filters["State"];
  }
  
  // Call function to apply all filters and rebuild the table
  filterTable(filters);
}

function filterTable(filters) {

  // Set the filteredData to the tableData
  let filteredData = tableData;
  // Loop through all of the filters and keep any data that
  // matches the filter values
  Object.entries(filters).forEach(([key, value]) => {
    filteredData = filteredData.filter(row => row[key] === value);
  })
  console.log(Object.entries(filters));
  // Finally, rebuild the table using the filtered Data
  buildTable(filteredData);
}

// Attach an event to listen for changes to each filter
d3.selectAll("#filter-btn").on("click", updateFilters);
// Build the table when the page loads
buildTable(tableData);