// By Dominic Eggerman
// Crawler to fetch data for locroles

// Navigate to page
window.location = "http://gcc.genscape.com/GCCcontent/intranet/manual_normalization.php";

// Select form
mainForm = document.getElementsByName("frmMain")[0]

// Select pipeline
pipeMenu = document.getElementById("selFFPipeline");
pipeMenu.value = 248

// Grab all the pipeline ids and associated indexes
for (var i = 0; i <= pipeMenu.length; i++) {
    pipeMenu.selectedIndex = i;
    var pipeID = pipeMenu.value;
    console.log(i + ":" + pipeID)
}

// Select opavail run
table = document.getElementById("reportResultTable");

// Fetch
fetcher = document.getElementsByName("cmdFF")[0]