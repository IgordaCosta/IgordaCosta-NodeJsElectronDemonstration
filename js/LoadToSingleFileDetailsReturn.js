

async function LoadToSingleFileDetailsReturn() {

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { ProgressBarGotResults } = require(path.join(currentWorkingDirectory, "./js/ProgressBarGotResults"));

    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, "./js/getDbDataSimple"));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { LoadToSingleFileDetailsP2Return } = require(path.join(currentWorkingDirectory, "./js/LoadToSingleFileDetailsP2Return"));


    let AwaitProveData = "getting data";

    let TableName = '';

    let Database = '';


    TableGotten = await getDbDataSimple(AwaitProveData, TableName, Database);

    FinalSaveLocation = TableGotten['NextFileToCome'];

    rw = TableGotten['rw'];

    numberOfRows = TableGotten['numberOfStepsTotal'];

    percentDone = TableGotten['percentileComplete'];


    ProgressBarGotResults(FinalSaveLocation, rw, numberOfRows, percentDone);


    let filename = "LoadToSingleFileDetailsP2.py";

    let callback = LoadToSingleFileDetailsP2Return;


    RunPythonFile(filename, callback, gotResultsFuction = false);

}
exports.LoadToSingleFileDetailsReturn = LoadToSingleFileDetailsReturn;
