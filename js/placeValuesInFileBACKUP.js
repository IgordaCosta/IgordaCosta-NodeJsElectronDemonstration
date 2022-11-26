

function ForceCloseExcelResultsPVF(results){

    console.log(results)

    console.log("ForceCloseExcelResultsPVF function ran")

    RunPlaceValuesInFile()

}


function RunPlaceValuesInFile(){

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { placeValuesInFileReturn } = require(path.join(currentWorkingDirectory, "./js/placeValuesInFileReturn"));



    let filename = "placeValuesInFile.py";

    let callback = placeValuesInFileReturn;

    console.log("before placeValuesInFileReturn callback")


    RunPythonFile(filename, callback, gotResultsFuction = false);  // unblock this after the test

}




async function placeValuesInFile() {
    // before is LMFAddInfoExcelResults
    console.log("here it will run the python file for placeValuesInFile function");

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();

    // const { StringListToStrin2LayerList } = require(path.join(currentWorkingDirectory, "./js/StringListToStrin2LayerList"));
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    // const { AddToTable } = require(path.join(currentWorkingDirectory, "./js/AddToTable"));

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));

    const { CheckIfValueExistsInDb } = require(path.join(currentWorkingDirectory, "./js/CheckIfValueExistsInDb"));

    // const { placeValuesInFileReturn } = require(path.join(currentWorkingDirectory, "./js/placeValuesInFileReturn"));


    


    // StringListToStrin2LayerList()
    let AwaitProveData = "AddToTable has started";

    let data = 0;

    let dataName = 'rw';

    let TableName = '';

    let Database = '';

    let ValueExists = await CheckIfValueExistsInDb(TableName, Database, dataName);


    // ValueExists=false // block this after the test

    if (ValueExists) { 

        console.log("ValueExists is true here")
        
        RunPlaceValuesInFile()


    }
    else {

        console.log("ValueExists is false here")

        // Done = await AddToTable(AwaitProveData, data, dataName, TableName, Database);

        let Done = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

        console.log(Done);

        // close excel file if open below

        let filename='CloseWorkbook.py';


        
        let callback=ForceCloseExcelResultsPVF;

        RunPythonFile(filename,callback)


        // close excel file if open above

    }





    // let filename = "placeValuesInFile.py";

    // let callback = placeValuesInFileReturn;

    // console.log("before placeValuesInFileReturn callback")


    // // RunPythonFile(filename, callback, false);  // unblock this after the test




}
exports.placeValuesInFile = placeValuesInFile;
