
async function getLocationSaved(htmlBodyObject) {


    var process = require('process');

    var path = require('path');

    let CurrentWorkingDirectory = process.cwd();

    // console.log(CurrentWorkingDirectory);

    // console.log('CurrentWorkingDirectory is above');

    const { gotResults } = require(path.join(CurrentWorkingDirectory, "./js/gotResults"));

    const { getDbData } = require(path.join(CurrentWorkingDirectory, "./js/getDbData"));

    const { MyDocumentsDatabasePath } = require(path.join(CurrentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    const { LMFItemCheckedHTML } = require(path.join(CurrentWorkingDirectory, "./js/LMFItemCheckedHTML"));

    const { placeInHTML2Id } = require(path.join(CurrentWorkingDirectory, "./js/placeInHTML2Id"));

    gotResults();

    const TableName = '';

    const Database = '';

    let CurrentWorkingPath = CurrentWorkingDirectory;

    const MydocumentsDbPath = await MyDocumentsDatabasePath(CurrentWorkingPath);


    let resultDatabase = MydocumentsDbPath;

    let databaseData = await getDbData(resultDatabase, TableName, Database, CurrentWorkingPath, MydocumentsDbPath);

    // console.log(databaseData);

    // console.log('databaseData gotten on second screen above');


     


    let item1 = databaseData['FolderSaveLocation'];
    let ID1 = "SaveLocationID";

    let datafillName = item1

    let item2 = databaseData['nameOfNewFile'];
    let ID2 = "SaveNameID";

    HtmlAdded = await LMFItemCheckedHTML(datafillName, htmlBodyObject);
    Done = await placeInHTML2Id(HtmlAdded, item1,item2, ID1, ID2);

    // console.log("Finished placing variable on HTML:", Done);




   

    





    process.chdir(CurrentWorkingDirectory)








}
exports.getLocationSaved = getLocationSaved;
