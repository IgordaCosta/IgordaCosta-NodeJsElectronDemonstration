
async function getDatafillName(htmlBodyObject) {


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

    let spaceReplaceDataUserImput = '$%78&*&';


    datafillName = databaseData.datafillName.replace(spaceReplaceDataUserImput, ' ');

    // console.log(datafillName);

    // console.log('datafillName above');

    let ID = "datafillNameID";

    HtmlAdded = await LMFItemCheckedHTML(datafillName, htmlBodyObject);

    Done = await placeInHTMLId(HtmlAdded, datafillName, ID);

    // console.log("Finished placing variable on HTML:", Done);

    process.chdir(CurrentWorkingDirectory)

}
exports.getDatafillName = getDatafillName;
