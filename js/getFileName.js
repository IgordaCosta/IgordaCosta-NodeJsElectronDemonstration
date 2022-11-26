



async function getFileName(htmlBodyObject) {


    var process = require('process');

    var path = require('path');

    let CurrentWorkingDirectory = process.cwd();

    // console.log(CurrentWorkingDirectory);

    // console.log('CurrentWorkingDirectory is above');

    const { gotResults } = require(path.join(CurrentWorkingDirectory, "./js/gotResults"));

    const { getDbData } = require(path.join(CurrentWorkingDirectory, "./js/getDbData"));

    const { MyDocumentsDatabasePath } = require(path.join(CurrentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    const { LMFItemCheckedHTML } = require(path.join(CurrentWorkingDirectory, "./js/LMFItemCheckedHTML"));

    const { placeInHTMLId } = require(path.join(CurrentWorkingDirectory, "./js/placeInHTMLId"));

    gotResults();

    const TableName = '';

    const Database = '';

    let CurrentWorkingPath = CurrentWorkingDirectory;

    const MydocumentsDbPath = await MyDocumentsDatabasePath(CurrentWorkingPath);


    let resultDatabase = MydocumentsDbPath;

    let databaseData = await getDbData(resultDatabase, TableName, Database, CurrentWorkingPath, MydocumentsDbPath);

    // console.log(databaseData);

    // console.log('databaseData gotten on second screen above');


    fileNameOnly = databaseData['fileNameOnly'];


    let ID = "FilenameOnlyID";

    HtmlAdded = await LMFItemCheckedHTML(fileNameOnly, htmlBodyObject);

    Done = await placeInHTMLId(HtmlAdded, fileNameOnly, ID);

    // console.log("Finished placing variable on HTML:", Done);

    process.chdir(CurrentWorkingDirectory)





    // console.log('continue from here split files in different folders ')



    // let textSelected = getSelectionText()

    // console.log(textSelected)

    



}
exports.getFileName = getFileName;
