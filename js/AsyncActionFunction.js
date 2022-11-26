


async function AsyncActionFunction2(ItemChecked,ItemNOTchecked,typeOfButton){


    var process = require("process");

    var path = require("path");

    const currentDirectory = process.cwd();

    
    const { MyDocumentsDatabasePath } = require(path.join(currentDirectory, "./js/MyDocumentsDatabasePath"));

    const { CurrentWorkingPathFunc } = require(path.join(currentDirectory, "./js/CurrentWorkingPathFunc"));

    const { continuationLoadMultipleFilesFromDatabase } = require(path.join(currentDirectory, "./js/continuationLoadMultipleFilesFromDatabase"));

    
    try {

        const CurrenWorkingPath = await CurrentWorkingPathFunc();

        const MydocumentsDbPath = await MyDocumentsDatabasePath(CurrenWorkingPath);

        continuationLoadMultipleFilesFromDatabase(MydocumentsDbPath, CurrentWorkingPath, ItemChecked, ItemNOTchecked,typeOfButton);

    }
    catch (err) {

        // console.log(err);

    }



};




function AsyncActionFunction(ItemChecked,ItemNOTchecked,typeOfButton){
    var process = require("process");

    var path = require("path");

    const currentDirectory = process.cwd();

    const { DeleteTempFIlesFromApp } = require(path.join(currentDirectory, "./js/DeleteTempFIlesFromApp"));
    
    let ContinueTofunction = ''

    DeleteTempFIlesFromApp(ContinueTofunction);



    AsyncActionFunction2(ItemChecked,ItemNOTchecked,typeOfButton);

};








exports.AsyncActionFunction = AsyncActionFunction;
