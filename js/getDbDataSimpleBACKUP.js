
function getDbDataSimpleBACKUP(AwaitProveData,TableName,Database) {

    return new Promise((resolve, _reject) => {
    
    console.log(AwaitProveData)

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { preGetDbDataSimple } = require(path.join(currentWorkingDirectory, "./js/preGetDbDataSimple"));




    let DataGotten=preGetDbDataSimple(AwaitProveData,TableName,Database)

    console.log(DataGotten)

    resolve(DataGotten)


    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    

    // let MyDocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)

    // let resultDatabase=MyDocumentsDbPath

    // let DoneGet= await getDbData(resultDatabase,TableName,Database,currentWorkingDirectory,MyDocumentsDbPath)

    // console.log(DoneGet)


    // return DoneGet
    }

    )

}

exports.getDbDataSimpleBACKUP = getDbDataSimpleBACKUP;