// By Dominic Eggerman
// Crawler to fetch data for locroles

//////////
// USER //
//////////
// User must select the target pipeline from the dropdown on page load
// Select dates (YYYY, MM, DD)
startDay = new Date(2018, 08, 15);
endDay = new Date(2018, 08, 20);

// // // // //

// 
// Get date range
// 
// Returns an array of dates between the two dates
var getDates = function(startDate, endDate) {
    var dates = [],
        currentDate = startDate,
        addDays = function(days) {
            var date = new Date(this.valueOf());
            date.setDate(date.getDate() + days);
            return date;
        };
    while (currentDate <= endDate) {
        dates.push(currentDate);
        currentDate = addDays.call(currentDate, 1);
    }
    return dates;
}
// Generate range
var dates = getDates(startDay, endDay);
var dateArr = [];                                                                                                          
dates.forEach(function(date) {
    var day = date.getMonth() + "/" + date.getDate() + "/" + date.getFullYear();
    dateArr.push(day);
});

// Get page items we will use
var dateBox = document.getElementById("txtFFDateIn");  // Date input box
var table = document.getElementById("reportResultTable");  // table of results
var numOps = table.children[1].children.length;  // Number of options in dataset
var input;  // Input button for dataset
var fetcher = document.getElementById("cmdFF");  // Fetch button

// For date in array
for (var i = 0; i < dateArr.length; i++) {

    // Set date
    dateBox.value = dateArr[i];

    //
    // Select opavail run
    //
    // Loop to get the correct input
    for (var i = 0; i <= numOps; i++) {
        var args = table.children[1].children[i].children[2].textContent;
        if (args.includes("manualRun=true")) {
            // Get input button and break
            input = table.children[1].children[i].children[0].children[0];
            break;
        }
    }

    // Mimic click on input
    input.click();

    // Fetch
    fetcher.click();

    //
    // Look for status message
    //
    wait = true
    var statusTable = document.getElementsByTagName("table")[0];
    while (wait) {
        if (typeof statusTable.children[0].children[2] == "undefined") {}
        else {wait = false}
    }

    running = true
    while (running) {
        // Check status
        var status = statusTable.children[0].children[2].children[2].textContent;
        if (status.includes("progress") || status.includes("not yet")) {
            console.log(status)
            status = statusTable.children[0].children[2].children[2].textContent;
        } else if (status.includes("completed")) {
            outputDetail = document.getElementsByTagName("textarea")[0].textContent;
        }

        // Check output and close window
        var close = document.getElementsByClassName("close-window")[0];
        if (outputDetail.includes("errors=0;")) {
            console.log("Completed: " + dateArr[i])
            close.click();
        } else {
            console.log("Encountered error: " + dateArr[i]);
            close.click();
        }

        // Stop running while loop
        running = false
    }

}