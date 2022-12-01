


async function returnFromRunReturnFromSameFileInside(results) {

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();

    const { TypeJobName } = require(path.join(currentWorkingDirectory, "./js/TypeJobName"));

    const { AlteredOrOpenedDocument } = require(path.join(currentWorkingDirectory, "./js/AlteredOrOpenedDocument"));


    
    // let copiedDoc = results[results.length - 2];

    let copiedDoc = await results[results.length - 1];

    // let newFileLocation0 = results[results.length - 1];
    if (copiedDoc == "True") {
        // console.log('copiedDoc=="True"');
        // console.log("continue from here copiedDoc is true");
        TypeJobName();

        // continue to the next part from here
    } else if (copiedDoc == "False") {


        AlteredOrOpenedDocument();



    } else {
        let message = "error with print statement in the last python program run! " +
            "The program uses a False/True only values (in print statment) " +
            "and it is something else!";

        // console.log(message);
        // logger.info(message);
    }


}
exports.returnFromRunReturnFromSameFileInside = returnFromRunReturnFromSameFileInside;
