
async function ResultsOfExist(results) {
    var path = require("path")
    var process = require("process")
    CurrrentWorkingDirectory=process.cwd()

    const { DelOptionsForIfExists } = require(path.join(CurrrentWorkingDirectory,"./js/DelOptionsForIfExists"));

    const { getDbData } = require(path.join(CurrrentWorkingDirectory,"./js/getDbData"));

    const { MyDocumentsDatabasePath } = require(path.join(CurrrentWorkingDirectory,"./js/MyDocumentsDatabasePath"));

    // console.log(results)

    // console.log('result of python function')


    let ifExists = await results[results.length - 1];


    let MydocumentsDbPath = await MyDocumentsDatabasePath(CurrrentWorkingDirectory)
    

    let TableName=''

    let Database=''

    let CurrentWorkingPath=CurrrentWorkingDirectory

    let resultDatabase = MydocumentsDbPath


    let DatabaseData= await getDbData(resultDatabase,TableName,Database,CurrentWorkingPath,MydocumentsDbPath);

    let typeOfButton = DatabaseData.typeOfButton


    if (typeOfButton=="Del"){

        DelOptionsForIfExists(ifExists);

    }else if(typeOfButton=="LMF"){

        // TODO

    }else if(typeOfButton=="LSF"){

        // TODO

    }else{ 

        // console.log("typeOfButton value is worng");
        // console.log(typeOfButton);
        // console.log('typeOfButton value above');

    }

    // 'typeOfButton'


    

    
    

    // DelOptionsForIfExists(ifExists)


}
exports.ResultsOfExist = ResultsOfExist;




