
async function preGetDbDataSimple(AwaitProveData,TableName,Database) {
    
    // console.log(AwaitProveData)

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { getDbData } = require(path.join(currentWorkingDirectory, "./js/getDbData"));


    const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    

    let MyDocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)

    let resultDatabase=MyDocumentsDbPath

    let DoneGet= await getDbData(resultDatabase,TableName,Database,currentWorkingDirectory,MyDocumentsDbPath)

    // console.log(DoneGet)


    return DoneGet

}

exports.preGetDbDataSimple = preGetDbDataSimple;