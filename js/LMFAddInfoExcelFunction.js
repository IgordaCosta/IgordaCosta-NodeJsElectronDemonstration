function LMFAddInfoExcelFunction() {


    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();

    const { gotResults } = require(path.join(currentWorkingDirectory, './js/gotResults'));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));

    const { LMFAddInfoExcelResults } = require(path.join(currentWorkingDirectory, './js/LMFAddInfoExcelResults'));

    gotResults();

    // console.log("inside LMFAddInfoExcel function");

    // console.log("before LMFAddInfoExcelResults callback");

    let filename = 'LMFAddInfoExcel.py';
    let callback = LMFAddInfoExcelResults;

    RunPythonFile(filename, callback);

}
exports.LMFAddInfoExcelFunction = LMFAddInfoExcelFunction;
