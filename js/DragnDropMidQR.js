// const { require } = require("./DragnDrop");


async function DragnDropMidQR(pathUsed) {



    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));

    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    const { DragnDropMidQR0 } = require(path.join(currentWorkingDirectory, "./js/DragnDropMidQR0"));


    // let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory);


    let TableName = '';

    let Database = '';

    let data = 'false';

    let dataName = 'PDFfile';

    let Done = await insertIntoDatabase(data, dataName, currentWorkingDirectory, TableName, Database);

    // console.log(Done);


    DragnDropMidQR0(pathUsed);
}
exports.DragnDropMidQR = DragnDropMidQR;
