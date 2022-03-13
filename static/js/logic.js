// Creating map object
var myMap = L.map("map", {
    center: [47.6038321, -122.3300624],
    zoom: 10
  });
  
  // Adding tile layer
  L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
  }).addTo(myMap);
  

// Define a markerSize function that will give each billionair a different radius based on its net worth
function markerSize(NetWorth) {
    return NetWorth *10;
  }
  
  // Each billionair object contains the billionair's name, location and NetWorth
  var billionaires = [
    {
      Name: "Jeff Bezos",
      location: [47.6038321, -122.3300624],
      NetWorth: 177.0
    },
    {
      Name: "Elon Musk",
      location: [30.2711286, -97.74369950000001],
      NetWorth: 151.0
    },
    {
      Name: "Bernard Arnault & family",
      location: [48.8566969, 153.0260],
      NetWorth: 150
    },
    {
      Name: "Bill Gates",
      location: [-20.7264, 2.3514616],
      NetWorth: 124.0
    },
    {
      Name: "Mark Zuckerberg",
      location: [47.620548, -122.2264453],
      NetWorth: 97.0
    }
  ];
  
  // Loop through the billionaires array and create one marker for each billionair object
  for (var i = 0; i < billionaires.length; i++) {
    L.circle(billionaires[i].location, {
      fillOpacity: 0.75,
      color: "darkblue",
      fillColor: "green",
      radius: 1000,
      // Setting our circle's radius equal to the output of our markerSize function
      // This will make our marker's size proportionate to its networth
      radius: markerSize(billionaires[i].NetWorth)
    }).bindPopup("<h1>" + billionaires[i].Name + "</h1> <hr> <h3>Net Worth: " + billionaires[i].NetWorth + "</h3>").addTo(myMap);
  }
  

