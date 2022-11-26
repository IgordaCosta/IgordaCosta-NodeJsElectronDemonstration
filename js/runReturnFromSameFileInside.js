function runReturnFromSameFileInside() {

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { returnFromRunReturnFromSameFileInside } = require(path.join(currentWorkingDirectory, "./js/returnFromRunReturnFromSameFileInside"));

    let filename = 'ReturnFromSameFileInside.py';

    let callback = returnFromRunReturnFromSameFileInside;



    RunPythonFile(filename, callback);

    // console.log('here')



}
exports.runReturnFromSameFileInside = runReturnFromSameFileInside;
