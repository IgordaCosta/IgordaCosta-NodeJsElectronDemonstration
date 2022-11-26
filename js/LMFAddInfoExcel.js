




function RunOpenFolderLocation(){


    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));


    let filename = 'OpenFolderLocation.py';

    let callback = '';


    RunPythonFile(filename, callback, gotResultsFuction = false);  // unblock this after the test

    
}


async function LMFPregetFileNames(){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { getDbData } = require(path.join(currentWorkingDirectory, './js/getDbData'));

    const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, './js/MyDocumentsDatabasePath'));

    // const { AddToTable } = require(path.join(currentWorkingDirectory, './js/AddToTable'));

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));

    const { LMFNotValidFileNames } = require(path.join(currentWorkingDirectory, './js/LMFNotValidFileNames'));




    let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)

    let CurrentWorkingPath = currentWorkingDirectory

    let Database=''

    let TableName=''

    let resultDatabase = MydocumentsDbPath

    let DbDataGotten =await getDbData(resultDatabase,TableName,Database,CurrentWorkingPath,MydocumentsDbPath)

    let databaseGotten=DbDataGotten;

    let codeBlock= await LMFgetCodeBlock(databaseGotten)


    let data = codeBlock
    
    let dataName = 'codeBlock'

    // MydocumentsDbPath

    // CurrentWorkingPath

    // TableName

    // Database

    AwaitProveData=codeBlock

    // let AddToTable= await AddToTable(AwaitProveData,data, dataName, MydocumentsDbPath,CurrentWorkingPath,TableName,Database)

    let AddToTable = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);
            
    LMFNotValidFileNames()


}



async function LMFgetCodeBlock(databaseGotten){

    // console.log(databaseGotten)

    return new Promise((resolve, _reject) => {


    let ListofInlist=databaseGotten.ListofInlist



    let spacedComa =  "', '"
    // console.log(ListofInlist.length)

    // console.log('above is ListofInlist.length')

    // console.log(ListofInlist)
    // console.log('ListofInlist string is above')

    let CorrectedText=ListofInlist.slice(1, -1);
          
    ListofInlist=CorrectedText.split(spacedComa);

    // console.log(ListofInlist)

    // console.log('ListofInlist as a list is above')

    let j=0;

    if (ListofInlist.constructor === Array){

    codeBlock =
    '<tr>'+
        '<th scope="row center">'+[j+1]+'</th>'+   
    
        // '<td>'+jobNameList[0][j]+'</td>'+
        '<td>'+ListofInlist[j]+'</td>'+
    
    '</tr>'

    
    for (j = 1; j < ListofInlist.length; j++) {



        codeBlock1=codeBlock;
        codeBlock =
        '<tr>'+
            '<th scope="row center">'+[j+1]+'</th>'+   
        
            // '<td>'+jobNameList[0][j]+'</td>'+
            '<td>'+ListofInlist[j]+'</td>'+
        
        '</tr>'


            codeBlock=codeBlock1+codeBlock;

    }

}else{

    codeBlock =
    '<tr>'+
        '<th scope="row center">'+[j+1]+'</th>'+   
    
        // '<td>'+jobNameList[0][j]+'</td>'+
        '<td>'+ListofInlist+'</td>'+
    
    '</tr>'

}



    resolve(codeBlock)

}
    )
}









function LMFAddInfoExcel(){
    //  before is LMFAddInfoSave
    

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    // const { gotResults } = require(path.join(currentWorkingDirectory, './js/gotResults'));


    const { LMFAddInfoExcelFunction } = require(path.join(currentWorkingDirectory, './js/LMFAddInfoExcelFunction'));


    LMFAddInfoExcelFunction()

    // const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));

    // const { LMFAddInfoExcelResults } = require(path.join(currentWorkingDirectory, './js/LMFAddInfoExcelResults'));

    // gotResults()

    // console.log("inside LMFAddInfoExcel function")

    // console.log("before LMFAddInfoExcelResults callback")

    // let filename='LMFAddInfoExcel.py';
    // let callback=LMFAddInfoExcelResults;

    // RunPythonFile(filename,callback)



}


