




function ForceCloseExcel(){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));

    // console.log("inside ForceCloseExcel function")

    let filename='CloseWorkbook.py';
    let callback=ForceCloseExcelResults;

    RunPythonFile(filename,callback)




}


function ForceCloseExcelResults(results){

    // console.log(results)

    // console.log("Excel was forced closed")


    let locationToGo='LMFAlteredOrOpenedDocumentContinuation.html'

    location.replace(locationToGo);



}