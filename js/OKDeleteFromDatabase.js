

function DeleteItemJason(){

    const path = require('path');

    const process = require("process");

    const CurrentWorkingPath = process.cwd()
    

    const { RunPythonFile } = require(path.join(CurrentWorkingPath,"./js/RunPythonFile"));

    const { OperationComplete } = require(path.join(CurrentWorkingPath,"./js/OperationComplete"));

    

    let filename ="DeleteFromDataFillName.py"

    RunPythonFile(filename,OperationComplete)

}


