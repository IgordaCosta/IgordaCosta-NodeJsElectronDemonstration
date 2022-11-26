

function LMFRunOpenDeleteRecreateSheet(){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()



    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { loadMultipleFileResults } = require(path.join(currentWorkingDirectory, "./js/loadMultipleFileResults"));

    let filename = 'RunOpenDeleteRecreateSheet.py'

    RunPythonFile(filename,loadMultipleFileResults);

}