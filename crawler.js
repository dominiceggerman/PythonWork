// By Dominic Eggerman
// Crawler to fetch data for locroles

// Navigate to page
window.location = "http://gcc.genscape.com/GCCcontent/intranet/manual_normalization.php";

// Select form
mainForm = document.getElementsByName("frmMain")[0];

// Select pipeline
pipeMenu = document.getElementById("selFFPipeline");
pipeMenu.value = 248;

////////////////////////
// Select opavail run //
////////////////////////
// Get the data table
var table = document.getElementById("reportResultTable")
// Check which input has manual run = True
var numOps = table.children[1].children.length;
// Instantiate input
var input
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
input.click()

// Fetch
var fetcher = document.getElementById("cmdFF");
fetcher.click();