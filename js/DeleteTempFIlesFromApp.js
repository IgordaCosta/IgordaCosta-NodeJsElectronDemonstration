
function DeleteTempFIlesFromApp(callback){

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();
  
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    let filename='RunDeleteAllTempFilesFromApp.py';

    


    RunPythonFile(filename,callback, gotResultsFuction=false);


    };


exports.DeleteTempFIlesFromApp = DeleteTempFIlesFromApp;


