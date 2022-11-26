

function ForceCloseExcelResultsPVF(results){

    // this is the first run of the file at rw = 0

 
    RunPlaceValuesInFile();

}


function RunPlaceValuesInFile(){

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { placeValuesInFileReturn } = require(path.join(currentWorkingDirectory, "./js/placeValuesInFileReturn"));


    let filename = "placeValuesInFile.py";

    let callback = placeValuesInFileReturn;


    RunPythonFile(filename, callback, gotResultsFuction = false);  // unblock this after the test

}




async function placeValuesInFile() {
   
    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();

    
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
   
    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));

    const { CheckIfValueExistsInDb } = require(path.join(currentWorkingDirectory, "./js/CheckIfValueExistsInDb"));


    // const d = new Date();
    // let JsInitTimeInMliSeconds = d.getTime();


    // [datafillName, dbPath,typeOfButton];


    
    // let AwaitProveData = "AddToTable has started";

    // let data = 0;

    // let data = [0, JsInitTimeInMliSeconds];

    // let dataName = ['rw', 'JsInitTimeInMliSeconds'];


    let TableName = '';

    let Database = '';

    let dataName2 = 'rw';

    let ValueExists = await CheckIfValueExistsInDb(TableName, Database, dataName2);

    
    if (ValueExists) { 
    
        RunPlaceValuesInFile();

    }
    else {

        const d = new Date();
        let JsInitTimeInMliSeconds = d.getTime();

        let HalfPassed = 'False'

        // let data = [0, JsInitTimeInMliSeconds, HalfPassed];

        // let dataName = ['rw', 'JsInitTimeInMliSeconds', 'HalfPassed'];

        let data = [JsInitTimeInMliSeconds, HalfPassed];

        let dataName = ['JsInitTimeInMliSeconds', 'HalfPassed'];

        let AwaitProveData = "AddToTable has started";
            
        let Done = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

           
        let filename='CloseWorkbook.py';
        
        let callback=ForceCloseExcelResultsPVF;


        RunPythonFile(filename,callback, gotResultsFuction = false);


    }


}
exports.placeValuesInFile = placeValuesInFile;
