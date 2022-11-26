
function LMFAlteredOrOpenedDocument(){
    // after is LMFRunOpenDeleteRecreateSheet

    location.replace("LMFAlteredOrOpenedDocument.html");

}

function LMFAddInfoSave(){
    
    location.replace("LMFAddInfoSave.html");

}



function loadMultipleFileResults(results) {

    loadMultipleFileResults2(results);

}




async function loadMultipleFileResults2(results) {


    // before is LoadMutipleFileJason

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    // const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
    const { LMFAddInfoSave } = require(path.join(currentWorkingDirectory, "./js/LMFAddInfoSave"));

    // LMFAddInfoSave


    Message = await (results[results.length - 1]).trim();

    if (Message == "did NOT save") {
        // console.log("this document did not save and will go to a new screen telling the user it has an excel sheet open");
        // console.log("afterwards it will run the RunOpenDeleteRecreateSheet program to do this part of the code again");


        LMFAlteredOrOpenedDocument();

        // let filename = 'RunOpenDeleteRecreateSheet.py'
        // RunPythonFile(filename,loadMultipleFileResults);
    }
    else if (Message == "Saved OK") {

        // console.log("this item saved ok and will go to the next part of the program");

        LMFAddInfoSave()

        // then LMFAddInfoExcel.js



    }
}
exports.loadMultipleFileResults = loadMultipleFileResults;
