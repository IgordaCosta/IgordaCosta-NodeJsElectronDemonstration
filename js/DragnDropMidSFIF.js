// const { require } = require("./DragnDrop");


function SelectText(){
    location.replace("SelectText.html");

}


async function DragnDropMidSFIF(pathUsed) {

    var iconv = require('iconv-lite');

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));

    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));


 
    


    // let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory);


    let TableName = '';

    let Database = '';


    let buff = Buffer.from(pathUsed, 'utf8');


    let fileLocation = iconv.decode(buff, 'utf8');


    let data = fileLocation;

    let dataName = 'fileLocation';


    let Done = await insertIntoDatabase(data, dataName, currentWorkingDirectory, TableName, Database);

    // console.log(Done);



    let filename = 'GetLocationName.py'
    
    let callback = SelectText
  
    RunPythonFile(filename, callback)



    


    // DragnDropMidSFIF0(pathUsed);
}
exports.DragnDropMidSFIF = DragnDropMidSFIF;
