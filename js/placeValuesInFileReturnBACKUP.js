function placeValuesInFileReturn(results) {

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { LMF_AIE_AlteredOrOpenedDocument } = require(path.join(currentWorkingDirectory, "./js/LMF_AIE_AlteredOrOpenedDocument"));


    const { ProgressBarGotResults } = require(path.join(currentWorkingDirectory, "./js/ProgressBarGotResults"));

    const { OperationComplete } = require(path.join(currentWorkingDirectory, "./js/OperationComplete"));

    const { Cancel } = require(path.join(currentWorkingDirectory, "./js/CancelFunction"));

    const { placeValuesInFile } = require(path.join(currentWorkingDirectory, "./js/placeValuesInFile"));



    console.log(results);

    let PossibleOptions = results[results.length - 1];

    console.log(PossibleOptions);



    if (PossibleOptions == "ItemSaved") {

        // console.log("ItemSaved option gotten");

        // console.log("here item was saved but not done");
        // console.log("from here it will go back to the same python funtion it came from");

        // console.log("the program will get the last 4 print variables and show them on the progress bar");
        // console.log("percent of completeness will be found and shown");

        let FinalSaveLocation0 = results[results.length - 2];

        console.log(FinalSaveLocation0);

        // console.log('FinalSaveLocation0 above !!!');

        // let rw = parseInt(results[results.length - 3]);
        let rw = results[results.length - 3];

        console.log(rw);

        // console.log('rw above !!!');

        // let numberOfRows = parseInt(results[results.length - 4]);
        let numberOfRows = results[results.length - 4];

        console.log(numberOfRows);

        // console.log('numberOfRows above !!!');

        // let percentDone = parseInt(results[results.length - 5]);
        let percentDone = results[results.length - 5];

        console.log(percentDone);

        // console.log('percentDone above');

        ProgressBarGotResults(FinalSaveLocation0, rw, numberOfRows, percentDone);

        placeValuesInFile();





    }
    else if (PossibleOptions == "DocNOTsaved") {

        console.log("DocNOTsaved option gotten");

        console.log('a sheet with the same name was created without the consent of the program and its currently open');
        console.log("the program will ask the user to close the excel sheet");

        console.log("the user will be directed to a page saying to close program used excel sheet");

        LMF_AIE_AlteredOrOpenedDocument();



    }
    else if (PossibleOptions == "SheetIsOpenAndHasChanges") {

        console.log("SheetIsOpenAndHasChanges option gotten");

        console.log("a excel sheet that will be used is open");
        console.log("the user must close this excel sheet");

        console.log("the user will be directed to the same window as the function above");

        console.log("the user will be directed to a page saying to close program used excel sheet");

        LMF_AIE_AlteredOrOpenedDocument();




    }
    else if (PossibleOptions == "AllDONE") {

        console.log("AllDONE option gotten");

        console.log("the user will be directed to the action completed html page");

        OperationComplete(); // unblock this after the test


    }
    else {

        console.log("else option gotten");

        console.log("check last variable in python function,");
        console.log("it must be one of the above");

        console.log("the old html page will be restored");

        Cancel();

    }






}


exports.placeValuesInFileReturn = placeValuesInFileReturn;
