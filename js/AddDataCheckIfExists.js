// const { TypeJobNameReload } = require("./js/LSFCheckIfFileNameExists");


function AddDataCheckIfExists(results) {

    AddDataCheckIfExists2(results);

}


async function AddDataCheckIfExists2(results) {

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { TypeJobNameReload } = require(path.join(currentWorkingDirectory, "./js/LSFCheckIfFileNameExists"));


    const { LoadToSingleFileDetailsReturn } = require(path.join(currentWorkingDirectory, "./js/LoadToSingleFileDetailsReturn"));






    let ifExists = await results[results.length - 1];


    if (ifExists == "True") {

        TypeJobNameReload();

        // console.log("variable is TRUE");

        // console.log("back to old window to try again");

        // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        // // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        // document.getElementsByClassName("input-group")[0].classList.remove('hidden');
        document.getElementById("FileExists").classList.remove('hidden');


    } else if (ifExists == "False") {

        // console.log("variable is False.... continue to next part from here");


        let filename = "LoadToSingleFileDetails.py";

        let callback = LoadToSingleFileDetailsReturn;


        RunPythonFile(filename, callback);

        // OpenExcelDocument();
    } else {

        // TypeJobNameReload();
        // console.log("Last Variable must be either True or False and it is neither. Check last Python function output!");


        // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        // document.getElementsByClassName("input-group")[0].classList.remove('hidden');
    };




}
exports.AddDataCheckIfExists = AddDataCheckIfExists;
