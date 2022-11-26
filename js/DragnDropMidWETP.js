// const { require } = require("./DragnDrop");


async function DragnDropMidWETP(pathUsed) {



    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));

    const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    const { DragnDropMidWETP0 } = require(path.join(currentWorkingDirectory, "./js/DragnDropMidWETP0"));


    // let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory);


    let TableName = '';

    let Database = '';

    let data = 'false';

    let dataName = 'PDFfile';

    let Done = await insertIntoDatabase(data, dataName, currentWorkingDirectory, TableName, Database);

    // console.log(Done);


    DragnDropMidWETP0(pathUsed);
}
exports.DragnDropMidWETP = DragnDropMidWETP;
