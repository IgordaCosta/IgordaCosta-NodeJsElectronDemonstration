




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

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));


    const { LoadToSingleFileDetailsP3Return } = require(path.join(currentWorkingDirectory, './js/LoadToSingleFileDetailsP3Return'));

    // console.log("add here connection back to LoadToSingleFileDetailsP3")


    let filename = "LoadToSingleFileDetailsP3.py";

    let callback = LoadToSingleFileDetailsP3Return;


    RunPythonFile(filename, callback, gotResultsFuction = false);



    // const { LMFAddInfoExcelFunction } = require(path.join(currentWorkingDirectory, './js/LMFAddInfoExcelFunction'));



}


function AfterManualClosing(){

    results="File was Manually Closed"

    ForceCloseExcelResults(results)
   
}