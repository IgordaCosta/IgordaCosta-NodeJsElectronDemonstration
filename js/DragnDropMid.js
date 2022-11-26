
async function DragnDropMid(pathUsed) {

    const process = require("process");
    const path = require("path");
    const currentWorkingDirectory = process.cwd();


    const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));
    const { DragnDropMid0 } = require(path.join(currentWorkingDirectory, "./js/DragnDropMid0"));

    let TableName = '';
    let Database = '';
    let data = 'false';
    let dataName = 'PDFfile';

    let Done = await insertIntoDatabase(data, dataName, currentWorkingDirectory, TableName, Database);
    
    DragnDropMid0(pathUsed);

}
exports.DragnDropMid = DragnDropMid;
