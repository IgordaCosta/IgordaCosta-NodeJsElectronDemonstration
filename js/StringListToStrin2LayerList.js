

function MakeListOfLists(ListOfDataframeValues){

    return new Promise((resolve,_reject) =>{


    let separator2="', '";

    let ListofValuesListOfList=[];

    let row=[];

    let i;

    for (i=0; i < ListOfDataframeValues.length ; i++){

    
        row[i]=ListOfDataframeValues[i].split(separator2)

        ListofValuesListOfList.push(row[i])

    }

    resolve(ListofValuesListOfList);


}
    )

}




async function StringListToStrin2LayerList(){

    var path = require("path");
    var process = require("process");

    const currentWorkingDirectory=process.cwd()

    const { getDbData } = require(path.join(currentWorkingDirectory,"./js/getDbData"));
    const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory,"./js/MyDocumentsDatabasePath"));


    let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)

    let resultsDatabase="ok lets start"

    let TableName=''

    Database=''


    let DbGotten=await getDbData(resultsDatabase,TableName,Database,currentWorkingDirectory,MydocumentsDbPath)


    let ListOfDataframeValues = DbGotten.dataframe

    ListOfDataframeValues = ListOfDataframeValues.slice(3, -3);


    separator1="'], ['"

    let ListOfDataframeValues0=ListOfDataframeValues.split(separator1)


    let NewListofValuesListOfList = await MakeListOfLists(ListOfDataframeValues0)

    // console.log(NewListofValuesListOfList)

    // console.log('NewListofValuesListOfList above')


}
exports.StringListToStrin2LayerList = StringListToStrin2LayerList;



