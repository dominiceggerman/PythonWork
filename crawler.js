// By Dominic Eggerman
// Crawler to fetch data for locroles

// Navigate to page
window.location = "http://gcc.genscape.com/GCCcontent/intranet/manual_normalization.php";

// Select form
mainForm = document.getElementsByName("frmMain")[0];

// Select pipeline
pipeMenu = document.getElementById("selFFPipeline");
pipeMenu.value = 248;

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
// Usage - dates are YYYY, MM, DD
var dates = getDates(new Date(2013,10,22), new Date(2013,11,25));
var dateArr = [];                                                                                                          
dates.forEach(function(date) {
    var day = date.getMonth() + "/" + date.getDate() + "/" + date.getFullYear();
    dateArr.push(day);
});

//
// Select date range
//
dates = ["08/08/2018", "08/09/2018", "08/10/2018"];
dateEntry = document.getElementById("txtFFDateIn");
for (var i = 0; i < date.length; i++) {
    dateEntry.value = dates[i];
}
//
// Select opavail run
//
// Get the data table
var table = document.getElementById("reportResultTable");
// Check which input has manual run = True
var numOps = table.children[1].children.length;
// Instantiate input
var input;
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
var fetcher = document.getElementById("cmdFF");
fetcher.click();

//
// Look for status message
//
var statusTable = document.getElementsByTagName("table")[0];
var status = statusTable.children[0].children[2].children[2].textContent;
if (status.includes("completed")) {
    outputDetail = document.getElementsByTagName("textarea")[0].textContent;
    if (outputDetail.includes("errors=0;")) {
        console.log(outputDetail);
    }
}