
// create variables for the billionaires and counting data

var bUrl ="js/bgeojsoncountdc1.js";
var cUrl = "js/bgeojsoncountdc1.js";

// read the data
d3.json(bUrl, function(data) {
  let bData = data.features
  d3.json(cUrl, function(data) {
    let countData = data.features

    createMap(bData,countData)
  })
})
// create map function
function createMap(bData,countData) {
// create variable for markers
    let bMarkers = bData.map((feature) =>
      L.circleMarker([feature.geometry.coordinates[1],feature.geometry.coordinates[0]],{
          radius: nwCheck(feature.properties.NetWorth), 
          stroke: true,
          color: 'black',
          opacity: 0.9,
          weight: 0.9,
          fill: true,
          fillColor: nwColor(feature.properties.NetWorth), 
          fillOpacity: 0.9   
      })
      .bindPopup("<h1> Net Worth : $" + feature.properties.NetWorth +
      
      "</h1><hr><h3> Name: " + feature.properties.Name +
      "</h1><hr><h3> Age: " + feature.properties.Age +
      "</h3><hr><p>" + (feature.properties.Country) + "</p>")
    )



// bilionaires markers
    let billionaires = L.layerGroup(bMarkers);




// xxxxxxxxxxxxxx
    function makePolyline(feature, layer){
      L.polyline([feature.geometry.coordinates[1],feature.geometry.coordinates[0]]
  
  );
    }

 // billionaires locations     
    let bcounting = L.geoJSON(countData, {
  
      onEachFeature: makePolyline,
        style: {
          color: 'white',
          opacity: 0.9
        }
    })



// xxxxxxxxxxxx

//   var heatpoints = {
//   "radius": 2,
//   "maxOpacity": .8,
//   "scaleRadius": true,
//   "useLocalExtrema": true,
//   latField: feature.geometry.coordinates[1],
//   lngField: feature.geometry.coordinates[0],
//   valueField: feature.properties.Counts
// };

// xxxxxxxxxxxx

// xxxxxxxxxxxx
// let bcounting = L.HeatmapOverlay(heatpoints);

//  var heatmappoints =[];
// countData.features.forEachFeature(function(feature){
// heatmappoints.push([feature.geometry.coordinates[1],feature.geometry.coordinates[0],feature.properties.Counts]);
// console.log(heatmappoints)
// var heat = L.heatLayer(heatmappoints, {radius:25}).addTo(myMap)

// })

// xxxxxxxxxxxx



  // Define map layers
  var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
  });

  var darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 19,
    id: "dark-v10",
    accessToken: API_KEY
  });


  var satellite =  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 19,
    id: "mapbox.satellite",
    accessToken: API_KEY
  });




  var outdoors =  L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 19,
    id: "outdoors-v11",
    accessToken: API_KEY
  });

  var baseMaps = {
    "Street Map": streetmap,
    "Dark Map": darkmap,
    "Satellite Map": satellite,
    "Outdoors Map": outdoors
  };

  var overlayMaps = {
    Billionaires_Net_Worth: billionaires,
    Location : bcounting
  };

  var myMap = L.map("map", {
    center: [47.6038321,-122.3300624],
    zoom: 4,
    layers: [streetmap, billionaires]
  });

var legend = L.control({ position: "bottomright" });

legend.onAdd = function(myMap){
    var div = L.DomUtil.create("div","legend");
    div.innerHTML = [
        "<k class='nwl1'></k><span>0-1</span><br>",
        "<k class='nwl50'></k><span>1-50</span><br>",
        "<k class='nwl100'></k><span>50-100</span><br>",
        "<k class='nwl150'></k><span>100-150</span><br>",
        "<k class='nwg150'></k><span>150+</span><br>"
      ].join("");
    return div;
}

legend.addTo(myMap);
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);
}


     function nwColor(NetWorth) {
      var color = "";
      if (NetWorth <= 1) { color = "gold"; }
      else if (NetWorth <= 50) {color = "yellow"; }
      else if (NetWorth <= 100) { color = "green"; }
      else if (NetWorth <= 150) {color = "blue"; }
      else { color = "darkblue"; }
    
    return color;
    
    };
function nwCheck(NetWorth){
  if (NetWorth <= 1){
      return 0.2
  }
  return NetWorth * 0.2;
}
