function MarkWordSheet (){

    location.replace("MarkWordSheet.html");
}


function GetOldWordStamp(){


    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    let filename="GetOldStamp.py"
    


    // let callback = MarkExcellSheet
    let callback = MarkWordSheet

    RunPythonFile(filename,callback)

    }
    exports.GetOldWordStamp = GetOldWordStamp;

