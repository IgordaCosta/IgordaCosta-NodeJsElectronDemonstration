

async function AddToDatabaseReturn(results) {

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();

    // console.log(results);


    const { gotResults } = require(path.join(currentWorkingDirectory, "./js/gotResults"));

    // const { RerunReturnFromSameFileInside } = require(path.join(currentWorkingDirectory, "./js/RerunReturnFromSameFileInside"));

    const { RerunReturnFromSameFileInsideFunction } = require(path.join(currentWorkingDirectory, "./js/RerunReturnFromSameFileInsideFunction"));

    gotResults();

    // console.log('check ok now')

    let IfExists = await results[results.length - 1];



    if (IfExists == "FileDoesNOTExist") {
        // console.log("this will run function directly");
        RerunReturnFromSameFileInsideFunction();

    } else if (IfExists == "FileAlreadyExist") {

        // console.log("fileAlready Exists. Run program here");


        const { getDbData } = require(path.join(currentWorkingDirectory, "./js/getDbData"));

        const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

        const { fileAlreadyExists } = require(path.join(currentWorkingDirectory, "./js/fileAlreadyExists"));


        let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory);

        // console.log('this is my document db path, (this must appear last)')

        let resultDatabsse = MydocumentsDbPath;

        let TableName = '';

        let Database = '';


        let DastabaseData = await getDbData(resultDatabsse, TableName, Database, currentWorkingDirectory, MydocumentsDbPath);

        // console.log('after get db data (this should appear last)')

        // console.log(DastabaseData);


        fileAlreadyExists();






    } else {
        // console.log("The last print statemt can only acept values FileDoesNOTExist or FileAlreadyExist, something is wrong")
    }
    // console.log("Finished Python File before ReturnFromSameFileInside.py ");
};

exports.AddToDatabaseReturn = AddToDatabaseReturn;
