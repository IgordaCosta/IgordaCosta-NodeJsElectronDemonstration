

function decodeBase64(stringToDecode){


  let buff = Buffer.from(stringToDecode, 'base64');

  // decode buffer as UTF-8
  let Decodedstr = buff.toString('utf-8');

return Decodedstr

}



function getDbData (resultDatabase,TableName,Database,CurrentWorkingPath,MydocumentsDbPath) {

  return new Promise((resolve, _reject) => {

  let valueGotten = getDbData0 (resultDatabase,TableName,Database,CurrentWorkingPath,MydocumentsDbPath)

    resolve(valueGotten);

  }

  )

}


async function getDbData0 (resultDatabase,TableName,Database,CurrentWorkingPath,MydocumentsDbPath) {

    // return new Promise((resolve, _reject) => {
    
    // this gets the data in a dictionary format
    // I must turn it from a string into a dictionary 
    // after getting the data in javascript


    console.log(resultDatabase);

    // var process = require("process");

    var path = require("path")

    // const currentWorkingDirectory=process.cwd()

    const { RunPythonFile } = require(path.join(CurrentWorkingPath, "./js/RunPythonFile"));


    if (TableName == ''){


      TableName = 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq';

      Database = 'None';


    }



    let filename = 'CallgetDbData.py';

    let callback = '';

    let dataUsed = [ "[" + TableName + ', '+ Database + ', '+ CurrentWorkingPath +']' ];

    let NoArgs = false;

    console.log(dataUsed);

    console.log('dataUsed is above before funciton')

    // filename=filename, callback=callback, gotResultsFuction=true, dataUsed = dataUsed, NoArgs=NoArgs);

    let results = await RunPythonFile(filename=filename, callback=callback, gotResultsFuction=true, dataUsed = dataUsed, NoArgs=NoArgs);
    

    console.log(results);

    let names00 = results[results.length - 1];

    let Datalist00 = results[results.length - 2];

    let names0 = decodeBase64(names00);

    let Datalist0 = decodeBase64(Datalist00);

    console.log(names0);

    console.log(Datalist0);

    console.log('names0 and datalist0 on javascrit part of the program')


    commaReplaceData1 = '%$1&*&' 
    commaReplaceData1 = '%$2&*&' 

    realCommaReplace = '$#@&5$' 

    // OutputValueToAppend2 = OutputValueToAppend.replace(commaReplaceData1, ', ').replace(commaReplaceData2, ',')



    let namesList = names0.replace("'",'').replace('"','').replace('[','').replace(']','').split(', ');

    // let DataList = Datalist0.replace("'",'').replace('"','').replace('[','').replace(']','').split(', ');

    let DataList = Datalist0.replace("'",'').replace('"','').replace('[','').replace(']','').replace(', ',realCommaReplace).replace(commaReplaceData1,', ' ).replace(commaReplaceData2,',').split(realCommaReplace);


    var columns = namesList;
    var rows = DataList;
    var result =  rows.reduce(function(result, field, index) {
      result[columns[index]] = field;
      return result;
    }, {})
    
    console.log(result);


    return result











    // var columns = ["Date", "Number", "Size", "Location", "Age"];
    // var rows = ["2001", "5", "Big", "Sydney", "25"];
    // var result =  rows.reduce(function(result, field, index) {
    //   result[columns[index]] = field;
    //   return result;
    // }, {})
    
    // console.log(result);


    
    
    
    
    // if(TableName==''){
    //     TableName="qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq"
    // }else{}

    // if(Database==''){
    //     Database='./AutoFormFiller.db'
    // }else{}

    // return new Promise((resolve,reject) =>{

    // var process = require('process');
    // process.chdir(MydocumentsDbPath);

    // console.log(resultDatabase)

    // console.log("this is the resultDatabase above")

    // const sqlite3 = require('sqlite3').verbose();

    // // open the database
    // let db = new sqlite3.Database(Database);

    // let sql = `SELECT * FROM ${TableName}`;
    
    // try{

    //     db.get(sql, (err, row) => {
    //         if (err) {

    //             process.chdir(CurrentWorkingPath);

    //             reject(err)

    //             console.log(err)
    
    //         }else{
            
    //         process.chdir(CurrentWorkingPath);

    //         console.log(row)

    //         console.log("above is the row within the function")
    
    //         resolve(row);
    
    //         }

    //     });

        
    // }catch(e){

    //     console.log(e)

    // }
    

    // // close the database connection
    // db.close();


    // }

    // )

}
exports.getDbData = getDbData;
