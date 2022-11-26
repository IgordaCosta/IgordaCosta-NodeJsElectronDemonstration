async function StartTableData(AwaitProveData,data, dataName, TableName,Database) {
    
    // console.log(AwaitProveData)

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    // const { getDbData } = require(path.join(currentWorkingDirectory, "./js/getDbData"));

    const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));

    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    

    // let MyDocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)

    
    // console.log(data)
    

    // console.log('data after if above')
    

    // console.log(dataName)

    // console.log('dataName after if above')

    
    Done= await insertIntoDatabase(data, dataName, currentWorkingDirectory,TableName,Database)

    // console.log(Done)
    

    // console.log('Done above')

    return Done


}
exports.StartTableData = StartTableData;