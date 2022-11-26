function DelOptionsForIfExists(ifExists) {

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { DelTypeJobNameReload } = require(path.join(currentWorkingDirectory, "./js/DelTypeJobNameReload"));

    const { OperationComplete } = require(path.join(currentWorkingDirectory, "./js/OperationComplete"));



    if (ifExists == "True") {


        let filename = "DeleteFromDataFillName.py";

        RunPythonFile(filename, OperationComplete);


    }
    else if (ifExists == "False") {


        // console.log("variable is False.... going back");
        DelTypeJobNameReload();

        document.getElementById("FileExists").classList.remove('hidden');


    }
    else {


        DelTypeJobNameReload();
        // console.log("Last Variable must be either True or False and it is neither. Check last Python function output!");


    };


}
exports.DelOptionsForIfExists = DelOptionsForIfExists;
