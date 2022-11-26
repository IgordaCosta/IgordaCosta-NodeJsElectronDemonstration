function placeValuesInFileReturn(results) {

    placeValuesInFileReturnfunction(results);

}





async function placeValuesInFileReturnfunction(results) {

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();

    // console.log(results);


    const { LMF_AIE_AlteredOrOpenedDocument } = require(path.join(currentWorkingDirectory, "./js/LMF_AIE_AlteredOrOpenedDocument"));

    const { ProgressBarGotResults } = require(path.join(currentWorkingDirectory, "./js/ProgressBarGotResults"));

    const { OperationComplete } = require(path.join(currentWorkingDirectory, "./js/OperationComplete"));

    const { Cancel } = require(path.join(currentWorkingDirectory, "./js/CancelFunction"));

    const { placeValuesInFile } = require(path.join(currentWorkingDirectory, "./js/placeValuesInFile"));


    let PossibleOptions = await results[results.length - 1];

    // console.log(PossibleOptions)

    // console.log('PossibleOptions above')

    if (PossibleOptions == "ItemSaved") {

        let AproxTotalTimeComplete = await results[results.length - 2];

        let JsInitTimeInMliSeconds = await results[results.length - 3];

        let NewEndTimeOfCompletion = await results[results.length - 4];

        // let percentDone = await results[results.length - 5];


        const CompareTimeNow = new Date().getTime();
        

        // ProgressBarGotResults(NewEndTimeOfCompletion, rw, numberOfRows, percentDone);
        ProgressBarGotResults(NewEndTimeOfCompletion, AproxTotalTimeComplete, JsInitTimeInMliSeconds,CompareTimeNow);

        placeValuesInFile();
        

    }else if (PossibleOptions == "DocNOTsaved") {

        LMF_AIE_AlteredOrOpenedDocument();

    }else if (PossibleOptions == "SheetIsOpenAndHasChanges") {

        LMF_AIE_AlteredOrOpenedDocument();

    }else if (PossibleOptions == "AllDONE") {

        document.getElementById("PercentMark").innerHTML = 100 + ' %';

        document.getElementById("progressBarUsed").ariaValueNow = 100;

        document.getElementById("progressBarUsed").style.width = 100 +'%';

        document.getElementById("Timer").innerHTML = "DONE";


        setTimeout(OperationComplete(), 500)

        // OperationComplete(); // unblock this after the test

    }else{

        Cancel();

    };

}


exports.placeValuesInFileReturn = placeValuesInFileReturn;
