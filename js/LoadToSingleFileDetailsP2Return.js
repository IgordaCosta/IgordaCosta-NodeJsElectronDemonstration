


async function LoadToSingleFileDetailsP2Return(results) {

    let PossibleOptions = awaitresults[results.length - 1];

    let percentDone = await results[results.length - 2];

    let numberOfStepsTotal = await results[results.length - 3];

    let rw = await results[results.length - 4];

    let FinalSaveLocation = await results[results.length - 5];




    // console.log(FinalSaveLocation);

    // console.log('FinalSaveLocation above');

    // console.log(rw);

    // console.log('rw above');

    // console.log(numberOfStepsTotal);

    // console.log('numberOfStepsTotal above');

    // console.log(percentDone);

    // console.log('percentDone above');


    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();

    var round = Math.round;



    const { ProgressBarGotResultsPromise } = require(path.join(currentWorkingDirectory, "./js/ProgressBarGotResultsPromise"));

    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, "./js/getDbDataSimple"));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { LoadToSingleFileDetailsP3Return } = require(path.join(currentWorkingDirectory, "./js/LoadToSingleFileDetailsP3Return"));



    // console.log(FinalSaveLocation);

    // console.log(rw);

    // console.log(numberOfStepsTotal);

    // console.log(percentDone);


    let numberOfRows = numberOfStepsTotal;

    let startPrintCommad = "html will be changed";


    let Done = await ProgressBarGotResultsPromise(startPrintCommad, FinalSaveLocation, rw, numberOfRows, percentDone);

    // console.log(Done);


    if (PossibleOptions == 'InformationAdded') {

        let filename = "LoadToSingleFileDetailsP2.py";

        let callback = LoadToSingleFileDetailsP2Return;


        RunPythonFile(filename, callback, gotResultsFuction = false);



    } else if (PossibleOptions == 'DoneGettingFileData') {

        let filename = "LoadToSingleFileDetailsP3.py";

        let callback = LoadToSingleFileDetailsP3Return;


        RunPythonFile(filename, callback, gotResultsFuction = false);




    } else {

        // console.log("the value is not on of the above check why, the value is bellow");

        // console.log(PossibleOptions);


    }






}
exports.LoadToSingleFileDetailsP2Return = LoadToSingleFileDetailsP2Return;
