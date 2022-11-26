

function LSF_AlteredOrOpenedDocument(){
    
    location.replace("LSF_AlteredOrOpenedDocument.html");

}

async function LoadToSingleFileDetailsP3Return(results) {

    let PossibleOptions = await results[results.length - 1];

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();

    const { OperationComplete } = require(path.join(currentWorkingDirectory, "./js/OperationComplete"));


    // console.log(PossibleOptions);



    if (PossibleOptions == 'FileNotSaved') {

        // console.log("file not saved this part must be made");

        LSF_AlteredOrOpenedDocument()




    } else if (PossibleOptions == 'OperationCompleted') {

        // console.log("Operation Completed")

        OperationComplete();

    } else {

        // console.log('FinalReturnValue is different from the above option the value is listed bellow');

        // console.log(FinalReturnValue);

    }

}
exports.LoadToSingleFileDetailsP3Return = LoadToSingleFileDetailsP3Return;
