// Read data from input file: data.js
// Manipulating index.html by appending new tags "tr" and "td"
// Then load data to the table

// d3.csv("/data/test.csv").then(function populateTable(billData) {
//     var tbody = d3.select("tbody");
//     billData.forEach((tableRow) => {
//         // console.log("this is function ufo", ufoData);
//         var row = tbody.append("tr");
//         Object.entries(tableRow).forEach(([key, value]) =>{
//             var tableCell = row.append("td");
//             tableCell.text(value);
//         });
//     });

// });

function isNotEmpty( el ){
    var x = !$.trim(el.html());
    // console.log("isEmpty function",x);
    return x;
}


// Filter data based on user input or search type and search strings
function filter() {
    // Prevent the page from refreshing
    d3.event.preventDefault();


    // Remove all "tr" that had been added previously by d3
    d3.select("tbody").selectAll('tr').remove();
    console.log("This is function filter");

    // Catch the scenario when user just hit button "Filter Data" without select the search engine in the dropdown list
    if (d3.select('.form-control').empty() == true)
        {
        console.log("Empty input box ");
        var fifilteredData = tableData;
        alertBox();
    } 
    
    // Filter data based on user input and selected search engine
    else {
        console.log("Else statement ....")
        var dropdownItem = d3.select("#selFilter").node().value;
        var count  = $("#inputBoxDiv div").length;
        console.log("dropdownItem: ", dropdownItem, "with size: ", count);

        var iname = d3.select("#sname.form-control");
        var irank = d3.select("#srank.form-control");
        var iindustries = d3.select("#sindustries.form-control");
        var icountry = d3.select("#scountry.form-control");

        switch(dropdownItem) {
            case "sname":
                if ((iname.empty()==false) && (iname.property("value")));
                {
                    console.log("case sname" );
                    console.log("user entered: selectedName: ", iname.property("value"));    
                }               
            case "srank":
                if ((irank.empty()==false) && (irank.property("value")));
                {
                    console.log("case srank");
                    console.log("user entered: selectedRank: ", irank.property("value"));
                }
            case "sindustries":
                if ((iindustries.empty()==false) && (iindustries.property("value")));
                {
                    console.log("case sindustries");
                    console.log("user entered: selecteIndustries: ", iindustries.property("value"));
                }            
            case "scountry":
                if ((icountry.empty()==false) && (icountry.property("value")));
                {
                    console.log("case scountry");
                    console.log("user entered: selectedCountry: ", icountry.property("value"));
                }
        }

        var fifilteredData =  data.filter(bill =>{
            console.log("Filter with OR AND operands");
            return  (bill.name === iname.property("value") || !iname.property("value"))  
                    && (bill.rank === irank.property("value") || !irank.property("value"))
                    && (bill.industries=== iindustries.property("value") || !iindustries.property("value"))
                    && (bill.country === icountry.property("value") || !icountry.property("value")) 
           })

        console.log("This value to be returned", fifilteredData);
    }

    // Call alert when the search string is invalid
    if ((!iname.property("value") && !irank.property("value") 
        && !iindustries.property("value") 
        && !icountry.property("value")) )
        {
            console.log("Return empty array", fifilteredData);
            alertReturnEmptyData();
        }

    // Call function to display the filtered data
    populateTable(fifilteredData)
}


// Clear user input input and remove all the "tr" that had been appended previously
function clearBoxFilter() {
    location.reload();
    populateTable(tableData)
}


// Create alert function to catch the default scenario when no search string had been entered
function alertBox() {
    var lines = '\u2500'.repeat(40);

    alert(lines + "\nWARNING!\n" + "Insufficient search information had been entered.\r\n"
        + "The table will be refreshed with default data.\r\n" 
        + "Please click on 'Reset Filter' and try again.\r\n" + lines);
}


// Create alert function to catch invalid search entry that return empty search array
function alertReturnEmptyData() {
    var boxes = '\u25AA'.repeat(50);
    alert(boxes + "\nWARNING\u203C\n" + "Invalid search data had been entered.\r\n"
        + "Please try again.\r\n" + boxes);
}


// Generate dynamic html input boxes based on the number of dropdown list selection items
function addNodes() {
    var multipleValues = $("#selFilter").val() || "";
    var inputBoxDiv = "";
    var allBoxes = ['sname','srank','sindustries','scountry'];
    var searchBox =[];

    // Case of multiple selections, generate correspondent input boxes
    if (multipleValues != "") {
        var aVal = multipleValues.toString().split(",");
        $.each(aVal, function(i, value) {
            console.log("if condition: ", allBoxes[i], "value: ", value.trim());
            inputBoxDiv += "<div>";
            inputBoxDiv += "<input type='text' class='form-control'"
                        + "id='" + value.trim() + "' placeholder='Enter " +  value.trim().slice(1) +"'" + " autocomplete='off'>";
                        inputBoxDiv += "</div>";
            searchBox = aVal
            })

        // Generate hidden input boxes
        for (var j =0; j < 4; j++)
            {
                if (allBoxes[j] != searchBox[j])
                {inputBoxDiv += "<div>";
                inputBoxDiv += "<input type='hidden' class='form-control'"
                            + "id='" + allBoxes[j] + "' placeholder='Enter " +  allBoxes[j].slice(1) +"'>";
                            inputBoxDiv += "</div>";}
            }
    }

    //Set inputBoxDiv 
    $("#inputBoxDiv").html(inputBoxDiv);
}


/* **************************************************************************** */
// Populate data with default values, i.e. all data from the data.js file
// populateTable(tableData);

// Call functions that triggered by the click button
d3.select("#selFilter").on("change", addNodes)
d3.select("#filter-btn").on("click", filter)
d3.select("#clear-btn").on("click", clearBoxFilter)
/* **************************************************************************** */

